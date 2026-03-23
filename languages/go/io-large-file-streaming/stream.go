package main

import (
    "bufio"
    "encoding/json"
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Bucket struct {
    Count       int `json:"count"`
    ValueSum    int `json:"value_sum"`
    WeightSum   int `json:"weight_sum"`
    ActiveCount int `json:"active_count"`
}

type Summary struct {
    TotalRecords int               `json:"total_records"`
    Categories   map[string]Bucket `json:"categories"`
}

func main() {
    path := os.Args[1]
    f, err := os.Open(path)
    if err != nil { panic(err) }
    defer f.Close()

    agg := map[string]Bucket{}
    total := 0
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        line := strings.TrimSpace(scanner.Text())
        if line == "" { continue }
        parts := strings.Split(line, ",")
        category := parts[1]
        value, _ := strconv.Atoi(parts[2])
        weight, _ := strconv.Atoi(parts[3])
        active, _ := strconv.Atoi(parts[4])
        b := agg[category]
        b.Count++
        b.ValueSum += value
        b.WeightSum += weight
        b.ActiveCount += active
        agg[category] = b
        total++
    }
    out, _ := json.Marshal(Summary{TotalRecords: total, Categories: agg})
    fmt.Println(string(out))
}
