#!/usr/bin/env node
import fs from 'node:fs';

const path = process.argv[2];
const data = JSON.parse(fs.readFileSync(path, 'utf8'));
const agg = new Map();
for (const item of data) {
  if (!agg.has(item.category)) {
    agg.set(item.category, { count: 0, value_sum: 0, weight_sum: 0, active_count: 0 });
  }
  const bucket = agg.get(item.category);
  bucket.count += 1;
  bucket.value_sum += item.value;
  bucket.weight_sum += item.weight;
  bucket.active_count += item.active ? 1 : 0;
}
const categories = Object.fromEntries(agg.entries());
console.log(JSON.stringify({ total_records: data.length, categories }));
