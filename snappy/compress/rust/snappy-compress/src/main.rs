extern crate snap;

use std::io::{Cursor, Read, Result, Seek, SeekFrom, copy};
use std::env;
use std::fs::File;
use std::time::{SystemTime, UNIX_EPOCH};

fn read_file_as_bytes(file_name: &String, times: i32) -> Result<Vec<u8>> {
    let mut f = File::open(file_name)?;
    let mut fbytes = Vec::new();
    for _ in 0..times {
        let _ = f.read_to_end(&mut fbytes);
        let _ = f.seek(SeekFrom::Start(0));
    }
    Ok(fbytes)
}

fn compress<'a>(data: Vec<u8>, iterations: i32) {
    let mut cursor = Cursor::new(data);
    for _ in 0..iterations {
        let mut v: Vec<u8> = Vec::new();
        let mut compressor = snap::Writer::new(v);
        let _ = copy(&mut cursor, &mut compressor);
        cursor.set_position(0);
    }
}

fn main() {
    let mut args = env::args();
    let file_name = args.nth(1).unwrap();
    let concat_repetitions = args.nth(0).unwrap().parse::<i32>().unwrap();
    let iterations = args.nth(0).unwrap().parse::<i32>().unwrap();
    let data = read_file_as_bytes(&file_name, concat_repetitions).unwrap();
    let start = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let start_secs = start.as_secs();
    let start_nanos = start.subsec_nanos();
    let start = (start_secs as f64) + (start_nanos as f64) / 1e9;
    println!("{:.6}", start);
    compress(data, iterations);
    let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let end_secs = end.as_secs();
    let end_nanos = end.subsec_nanos();
    let end = (end_secs as f64) + (end_nanos as f64) / 1e9;
    println!("{:.6}", end);
}
