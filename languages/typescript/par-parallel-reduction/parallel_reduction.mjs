#!/usr/bin/env node
const itemCount = Number(process.argv[2] || 200000);
const workers = 4;
function transform(x) { return (x * 7 + 11) % 1000; }
function reduceRange(start, end) {
  let total = 0;
  let count = 0;
  for (let i = start; i < end; i += 1) {
    total += transform(i);
    count += 1;
  }
  return { count, total };
}
const chunk = Math.ceil(itemCount / workers);
const tasks = [];
for (let i = 0; i < itemCount; i += chunk) {
  tasks.push(new Promise((resolve) => setImmediate(() => resolve(reduceRange(i, Math.min(i + chunk, itemCount))))));
}
const results = await Promise.all(tasks);
const item_count = results.reduce((a, x) => a + x.count, 0);
const value_sum = results.reduce((a, x) => a + x.total, 0);
console.log(JSON.stringify({ item_count, value_sum, workers }));
