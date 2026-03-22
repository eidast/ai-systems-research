#!/usr/bin/env node
const upper = Number(process.argv[2] || 100000);

function countPrimes(limit) {
  if (limit < 2) return 0;
  const sieve = new Uint8Array(limit + 1);
  sieve.fill(1);
  sieve[0] = 0;
  sieve[1] = 0;
  for (let p = 2; p * p <= limit; p += 1) {
    if (sieve[p]) {
      for (let multiple = p * p; multiple <= limit; multiple += p) {
        sieve[multiple] = 0;
      }
    }
  }
  let count = 0;
  for (let i = 2; i <= limit; i += 1) {
    count += sieve[i];
  }
  return count;
}

console.log(countPrimes(upper));
