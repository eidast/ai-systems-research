use std::env;

fn count_primes(limit: usize) -> usize {
    if limit < 2 {
        return 0;
    }
    let mut sieve = vec![true; limit + 1];
    sieve[0] = false;
    sieve[1] = false;
    let mut p = 2;
    while p * p <= limit {
        if sieve[p] {
            let mut multiple = p * p;
            while multiple <= limit {
                sieve[multiple] = false;
                multiple += p;
            }
        }
        p += 1;
    }
    sieve.iter().skip(2).filter(|&&v| v).count()
}

fn main() {
    let upper = env::args()
        .nth(1)
        .and_then(|v| v.parse::<usize>().ok())
        .unwrap_or(100000);
    println!("{}", count_primes(upper));
}
