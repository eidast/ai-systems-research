package main

import (
    "fmt"
    "os"
    "strconv"
)

func countPrimes(limit int) int {
    if limit < 2 {
        return 0
    }
    sieve := make([]bool, limit+1)
    for i := 2; i <= limit; i++ {
        sieve[i] = true
    }
    for p := 2; p*p <= limit; p++ {
        if sieve[p] {
            for multiple := p * p; multiple <= limit; multiple += p {
                sieve[multiple] = false
            }
        }
    }
    count := 0
    for i := 2; i <= limit; i++ {
        if sieve[i] {
            count++
        }
    }
    return count
}

func main() {
    upper := 100000
    if len(os.Args) > 1 {
        if parsed, err := strconv.Atoi(os.Args[1]); err == nil {
            upper = parsed
        }
    }
    fmt.Println(countPrimes(upper))
}
