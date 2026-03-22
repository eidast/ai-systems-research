# Testing Strategy — Cesar

## Resumen
El repo ya tiene una base funcional de ejecución, captura de ambiente, agregación y reporting para `cpu-prime-count` y `mem-large-json-transform`, pero la validación actual todavía es débil para sostener cambios con confianza.

Hallazgos relevantes del estado actual:
- `scripts/bench/run.sh` sí genera resultados estructurados y marca `correctness_passed`, pero hoy solo valida:
  - `cpu-prime-count`: que la salida final sea numérica.
  - `mem-large-json-transform`: que la salida final sea JSON parseable.
- `scripts/bench/verify.sh` solo verifica presencia de algunos archivos base; no cubre `mem-large-json-transform`, datasets, implementaciones ni fixtures.
- `scripts/report/render_report.py` y `render_mem_report.py` hardcodean `trials` y `warmups`, mientras `results/curated/latest/result-summary.json` mezcla corridas y ya muestra grupos con `6` trials para `cpu-prime-count`.
- Existe evidencia real en `results/raw/`, `results/curated/latest/`, `results/charts/latest/` y `results/reports/latest/`, pero no hay una puerta mínima automatizada que garantice que un cambio no rompió semántica o empaquetado.

## Riesgo principal
El mayor riesgo no es performance sino **comparar benchmarks incorrectos o reportar resultados inválidos** por falta de checks semánticos, consistencia de artefactos y validación post-cambio.

## Qué probar primero

### Prioridad 1 — Correctness semántico de benchmark outputs
Esto debe probarse antes que cualquier validación de performance.

#### 1. `cpu-prime-count`
Probar la función/implementación con vectores pequeños y determinísticos.

Casos mínimos:
- `0 -> 0`
- `1 -> 0`
- `2 -> 1`
- `3 -> 2`
- `10 -> 4`
- `100 -> 25`
- `1000 -> 168`
- `300000 -> 25997`

**Invariantes críticos:**
- La salida debe ser entero no negativo.
- El conteo debe ser monótono: si `b > a`, entonces `count(b) >= count(a)`.
- Todas las implementaciones deben devolver exactamente el mismo valor para el mismo input.

#### 2. `mem-large-json-transform`
Probar con fixture pequeño y con el dataset generado real.

Checks mínimos sobre el dataset actual `benchmarks/datasets/generated/mem-large-json-transform-medium.json`:
- `total_records = 50000`
- número de categorías = `20`
- suma de `count` por categoría = `50000`
- suma de `active_count` por categoría = `16667`
- suma total de `value_sum` = `24975000`
- suma total de `weight_sum` = `2399943`
- ejemplos de buckets:
  - `cat-0 = {count: 2500, value_sum: 1225000, weight_sum: 120003, active_count: 834}`
  - `cat-1 = {count: 2500, value_sum: 1242500, weight_sum: 120008, active_count: 833}`
  - `cat-19 = {count: 2500, value_sum: 1257500, weight_sum: 120001, active_count: 833}`

**Invariantes críticos:**
- `total_records == sum(category.count)`
- `0 <= active_count <= count` por categoría
- `categories` debe contener exactamente las categorías presentes en el input
- Python y TypeScript deben producir payload equivalente

## Estrategia mínima de unit testing

### A. Tests de lógica pura
Crear primero tests unitarios sobre funciones reutilizables, no sobre `stdout`:
- extraer `count_primes()` donde aún no sea fácilmente testeable por harness
- extraer `transform_dataset(data)` en Python/TypeScript para testear sin I/O

Objetivo:
- validar reglas semánticas con fixtures pequeños
- reducir dependencia de shell/scripts para detectar regresiones

### B. Tests de golden output / cross-language
Añadir un harness pequeño que ejecute cada implementación y compare contra expected outputs:
- `cpu-prime-count`: comparar contra tabla conocida
- `mem-large-json-transform`: normalizar JSON y comparar contra golden fixture esperado

Objetivo:
- asegurar equivalencia entre implementaciones
- detectar cambios silenciosos en formato o semántica

### C. Tests de pipeline mínimo
Probar scripts de pipeline con smoke scope:
- `scripts/bench/verify.sh`
- `scripts/bench/run.sh` con 1 trial y warmups mínimos
- `scripts/report/aggregate.py`
- `scripts/report/build_charts.py` / `build_mem_charts.py`
- `scripts/report/render_report.py` / `render_mem_report.py`

Objetivo:
- verificar que una corrida produce artefactos esperados
- validar que aggregation/reporting no se rompen por cambios de formato

## Validación post-cambio recomendada

### Gate rápido en PR
Correr siempre:
1. **Repo verify**
   - expandir `scripts/bench/verify.sh` para cubrir:
     - benchmark definitions de CPU y MEM
     - schemas
     - dataset generado requerido
     - existencia de `run.sh` por benchmark/language soportado
2. **Correctness suite**
   - vectores conocidos de `cpu-prime-count`
   - equivalencia de `mem-large-json-transform` en fixture pequeño + dataset medium
3. **Smoke pipeline**
   - 1 run por benchmark representativo:
     - `cpu-prime-count`: Python o TypeScript, `input_size=100000`, `trials=1`, `warmups=0/1`
     - `mem-large-json-transform`: Python o TypeScript, dataset medium, `trials=1`, `warmups=0/1`
   - luego `aggregate.py` + render de reporte
4. **Artifact assertions**
   - JSON de corrida parseable y conforme al schema
   - `quality.correctness_passed == true`
   - `exit_code == 0`
   - `wall_time_ms >= 0`, `mem_peak_mb >= 0`
   - summary, charts y report markdown generados

### Gate más pesado (manual o nightly)
- matriz más amplia por lenguaje
- trials completos según protocolo
- regeneración de curated summary/charts/reports
- revisión de consistencia entre raw results y reportes

## Cambios concretos que recomiendo implementar primero
1. **Fortalecer `run.sh` correctness gate**
   - `cpu-prime-count`: validar valor esperado, no solo “es número”.
   - `mem-large-json-transform`: validar estructura + invariantes + golden output normalizado.

2. **Ampliar `verify.sh`**
   - incluir `benchmarks/definitions/memory/mem-large-json-transform.yaml`
   - verificar dataset `benchmarks/datasets/generated/mem-large-json-transform-medium.json`
   - verificar presencia de implementaciones declaradas en la matriz

3. **Separar lógica de negocio de CLI/I-O**
   - facilitar unit tests reales en Python/TypeScript

4. **Eliminar hardcodes en reports**
   - tomar `trials` y `warmups` desde datos reales o metadata de corrida
   - evitar reportes inconsistentes con `result-summary.json`

## Smoke checklist mínimo
- `verify.sh` pasa
- ambas implementaciones de `cpu-prime-count` bajo prueba devuelven outputs esperados en vectores base
- Python y TypeScript de `mem-large-json-transform` producen resultado equivalente en fixture pequeño
- `run.sh` genera:
  - `env.json`
  - `logs/`
  - `runs/*.json`
- `aggregate.py` genera `result-summary.json`
- scripts de chart/report generan archivos esperados sin fallar

## Criterio de éxito mínimo
Un cambio al repo solo debería considerarse seguro si:
- no rompe equivalencia semántica de benchmarks
- no rompe el contrato del benchmark run JSON
- no rompe el pipeline de agregación/reporte
- no permite publicar resultados con metadata inconsistente o correctness no validado

## Nota QA
Hoy el repo está más cerca de un **pipeline funcional de benchmarking** que de un **sistema con gates de calidad reproducibles**. La mejor inversión inmediata es asegurar correctness/equivalence y luego proteger el pipeline con smoke automation ligera.