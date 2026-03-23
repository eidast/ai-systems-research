use serde::Serialize;
use std::env;
use std::thread;

#[derive(Serialize)]
struct ResultPayload { item_count: i32, value_sum: i32, workers: i32 }
fn transform(x: i32) -> i32 { (x * 7 + 11) % 1000 }

fn main() {
    let item_count: i32 = env::args().nth(1).and_then(|v| v.parse().ok()).unwrap_or(200000);
    let workers = 4;
    let chunk = ((item_count as f64) / (workers as f64)).ceil() as i32;
    let mut handles = vec![];
    for start in (0..item_count).step_by(chunk as usize) {
        let end = std::cmp::min(start + chunk, item_count);
        handles.push(thread::spawn(move || {
            let mut count = 0;
            let mut total = 0;
            for i in start..end { total += transform(i); count += 1; }
            (count, total)
        }));
    }
    let mut total_count = 0; let mut total_sum = 0;
    for h in handles { let (c,s) = h.join().unwrap(); total_count += c; total_sum += s; }
    println!("{}", serde_json::to_string(&ResultPayload { item_count: total_count, value_sum: total_sum, workers }).unwrap());
}
