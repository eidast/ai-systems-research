use serde::Serialize;
use std::env;
use std::sync::mpsc::sync_channel;
use std::thread;

#[derive(Serialize)]
struct ResultPayload {
    item_count: i32,
    value_sum: i32,
    workers: i32,
    queue_capacity: i32,
}

fn transform(x: i32) -> i32 { (x * 3 + 7) % 1000 }

fn main() {
    let item_count: i32 = env::args().nth(1).and_then(|v| v.parse().ok()).unwrap_or(100000);
    let workers = 4;
    let queue_capacity = 256;
    let (tx, rx) = sync_channel::<Option<i32>>(queue_capacity as usize);
    let rx = std::sync::Arc::new(std::sync::Mutex::new(rx));
    let mut handles = vec![];

    for _ in 0..workers {
        let rx = rx.clone();
        handles.push(thread::spawn(move || {
            let mut count = 0;
            let mut sum = 0;
            loop {
                let msg = rx.lock().unwrap().recv().unwrap();
                match msg {
                    Some(v) => { count += 1; sum += transform(v); }
                    None => break,
                }
            }
            (count, sum)
        }));
    }

    for i in 0..item_count { tx.send(Some(i)).unwrap(); }
    for _ in 0..workers { tx.send(None).unwrap(); }

    let mut total_count = 0;
    let mut total_sum = 0;
    for h in handles {
        let (c, s) = h.join().unwrap();
        total_count += c;
        total_sum += s;
    }

    println!("{}", serde_json::to_string(&ResultPayload { item_count: total_count, value_sum: total_sum, workers, queue_capacity }).unwrap());
}
