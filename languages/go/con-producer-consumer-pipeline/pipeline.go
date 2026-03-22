package main

import (
    "encoding/json"
    "fmt"
    "os"
    "strconv"
    "sync"
)

type Result struct {
    Count int `json:"item_count"`
    Sum   int `json:"value_sum"`
    Workers int `json:"workers"`
    QueueCapacity int `json:"queue_capacity"`
}

func transform(x int) int { return (x*3 + 7) % 1000 }

func main() {
    itemCount := 100000
    if len(os.Args) > 1 {
        if v, err := strconv.Atoi(os.Args[1]); err == nil { itemCount = v }
    }
    workers := 4
    queueCapacity := 256
    ch := make(chan int, queueCapacity)
    var wg sync.WaitGroup
    results := make(chan [2]int, workers)

    for i := 0; i < workers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            count, sum := 0, 0
            for item := range ch {
                count++
                sum += transform(item)
            }
            results <- [2]int{count, sum}
        }()
    }

    for i := 0; i < itemCount; i++ { ch <- i }
    close(ch)
    wg.Wait()
    close(results)

    totalCount, totalSum := 0, 0
    for r := range results {
        totalCount += r[0]
        totalSum += r[1]
    }
    out, _ := json.Marshal(Result{Count: totalCount, Sum: totalSum, Workers: workers, QueueCapacity: queueCapacity})
    fmt.Println(string(out))
}
