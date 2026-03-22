#!/usr/bin/env node
const itemCount = Number(process.argv[2] || 100000);
const workers = 4;
const queue = [];
let produced = 0;
let doneProducing = false;

function transform(x) {
  return (x * 3 + 7) % 1000;
}

async function producer() {
  while (produced < itemCount) {
    if (queue.length < 256) {
      queue.push(produced);
      produced += 1;
    } else {
      await new Promise((r) => setImmediate(r));
    }
  }
  doneProducing = true;
}

async function consumer() {
  let count = 0;
  let sum = 0;
  while (!doneProducing || queue.length > 0) {
    if (queue.length === 0) {
      await new Promise((r) => setImmediate(r));
      continue;
    }
    const item = queue.shift();
    sum += transform(item);
    count += 1;
  }
  return { count, sum };
}

(async () => {
  const producerPromise = producer();
  const consumers = Array.from({ length: workers }, () => consumer());
  await producerPromise;
  const results = await Promise.all(consumers);
  const item_count = results.reduce((acc, x) => acc + x.count, 0);
  const value_sum = results.reduce((acc, x) => acc + x.sum, 0);
  console.log(JSON.stringify({ item_count, value_sum, workers, queue_capacity: 256 }));
})();
