use serde::Serialize;
use std::collections::BTreeMap;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

#[derive(Serialize, Default)]
struct Bucket {
    count: i32,
    value_sum: i32,
    weight_sum: i32,
    active_count: i32,
}

#[derive(Serialize)]
struct Summary {
    total_records: i32,
    categories: BTreeMap<String, Bucket>,
}

fn main() {
    let path = env::args().nth(1).expect("dataset path required");
    let file = File::open(path).expect("open file");
    let reader = BufReader::new(file);
    let mut agg: BTreeMap<String, Bucket> = BTreeMap::new();
    let mut total = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        if line.trim().is_empty() { continue; }
        let parts: Vec<&str> = line.split(',').collect();
        let category = parts[1].to_string();
        let value: i32 = parts[2].parse().unwrap();
        let weight: i32 = parts[3].parse().unwrap();
        let active: i32 = parts[4].parse().unwrap();
        let bucket = agg.entry(category).or_default();
        bucket.count += 1;
        bucket.value_sum += value;
        bucket.weight_sum += weight;
        bucket.active_count += active;
        total += 1;
    }

    println!("{}", serde_json::to_string(&Summary { total_records: total, categories: agg }).unwrap());
}
