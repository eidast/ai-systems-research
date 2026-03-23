#!/usr/bin/env node
import fs from 'node:fs';
import readline from 'node:readline';

const path = process.argv[2];
const agg = new Map();
let total = 0;
const rl = readline.createInterface({ input: fs.createReadStream(path), crlfDelay: Infinity });
for await (const line of rl) {
  if (!line) continue;
  const [, category, value, weight, active] = line.split(',');
  if (!agg.has(category)) {
    agg.set(category, { count: 0, value_sum: 0, weight_sum: 0, active_count: 0 });
  }
  const bucket = agg.get(category);
  bucket.count += 1;
  bucket.value_sum += Number(value);
  bucket.weight_sum += Number(weight);
  bucket.active_count += Number(active);
  total += 1;
}
console.log(JSON.stringify({ total_records: total, categories: Object.fromEntries(agg.entries()) }));
