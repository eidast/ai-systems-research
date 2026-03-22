package main

import (
    "encoding/json"
    "fmt"
    "os"
)

type Record struct {
    ID       int    `json:"id"`
    Category string `json:"category"`
    Value    int    `json:"value"`
    Weight   int    `json:"weight"`
    Active   bool   `json:"active"`
    Name     string `json:"name"`
}

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
    raw, err := os.ReadFile(path)
    if err != nil {
        panic(err)
    }
    var data []Record
    if err := json.Unmarshal(raw, &data); err != nil {
        panic(err)
    }
    agg := map[string]Bucket{}
    for _, item := range data {
        bucket := agg[item.Category]
        bucket.Count += 1
        bucket.ValueSum += item.Value
        bucket.WeightSum += item.Weight
        if item.Active {
            bucket.ActiveCount += 1
        }
        agg[item.Category] = bucket
    }
    out, _ := json.Marshal(Summary{TotalRecords: len(data), Categories: agg})
    fmt.Println(string(out))
}
