extern crate snap;

use std::io::{Read, Result, Seek, SeekFrom};
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

fn decompress(data: Vec<u8>, iterations: i32) {
    let mut decoder = snap::Decoder::new();
    for _ in 0..iterations {
        if let Err(e) = decoder.decompress_vec(&data) {
            println!("{:?}", e);
        }
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
    let start = start_secs * 1_000_000_000 + start_nanos as u64;
    println!("{}", start);
    decompress(data, iterations);
    let end = SystemTime::now().duration_since(UNIX_EPOCH).unwrap();
    let end_secs = end.as_secs();
    let end_nanos = end.subsec_nanos();
    let end = end_secs * 1_000_000_000 + end_nanos as u64;
    println!("{}", end);
}
