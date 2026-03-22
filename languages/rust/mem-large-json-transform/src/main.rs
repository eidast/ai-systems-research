use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;
use std::env;
use std::fs;

#[derive(Deserialize)]
struct Record {
    id: i32,
    category: String,
    value: i32,
    weight: i32,
    active: bool,
    name: String,
}

#[derive(Serialize, Default)]
struct Bucket {
    count: i32,
    value_sum: i32,
    weight_sum: i32,
    active_count: i32,
}

#[derive(Serialize)]
struct Summary {
    total_records: usize,
    categories: BTreeMap<String, Bucket>,
}

fn main() {
    let path = env::args().nth(1).expect("dataset path required");
    let raw = fs::read_to_string(path).expect("read dataset");
    let data: Vec<Record> = serde_json::from_str(&raw).expect("parse dataset");
    let mut agg: BTreeMap<String, Bucket> = BTreeMap::new();
    for item in &data {
        let bucket = agg.entry(item.category.clone()).or_default();
        bucket.count += 1;
        bucket.value_sum += item.value;
        bucket.weight_sum += item.weight;
        if item.active {
            bucket.active_count += 1;
        }
    }
    let summary = Summary { total_records: data.len(), categories: agg };
    println!("{}", serde_json::to_string(&summary).unwrap());
}
