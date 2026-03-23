package main

import (
    "encoding/json"
    "fmt"
    "math"
    "os"
    "strconv"
    "sync"
)

type Result struct { ItemCount int `json:"item_count"`; ValueSum int `json:"value_sum"`; Workers int `json:"workers"` }
func transform(x int) int { return (x*7 + 11) % 1000 }
func main() {
    itemCount := 200000
    if len(os.Args) > 1 { if v, err := strconv.Atoi(os.Args[1]); err == nil { itemCount = v } }
    workers := 4
    chunk := int(math.Ceil(float64(itemCount) / float64(workers)))
    ch := make(chan [2]int, workers)
    var wg sync.WaitGroup
    for start := 0; start < itemCount; start += chunk {
        end := start + chunk; if end > itemCount { end = itemCount }
        wg.Add(1)
        go func(s, e int) {
            defer wg.Done(); count, total := 0, 0
            for i := s; i < e; i++ { total += transform(i); count++ }
            ch <- [2]int{count, total}
        }(start, end)
    }
    go func(){ wg.Wait(); close(ch) }()
    totalCount, totalSum := 0, 0
    for r := range ch { totalCount += r[0]; totalSum += r[1] }
    out, _ := json.Marshal(Result{ItemCount: totalCount, ValueSum: totalSum, Workers: workers})
    fmt.Println(string(out))
}
