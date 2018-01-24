extern crate snap;

use std::io::{Cursor, Read, Result, Seek, SeekFrom, copy};
use std::env;
use std::fs::File;
use std::time::SystemTime;

fn read_file_as_bytes(file_name: &String, times: i32) -> Result<Vec<u8>> {
    let mut f = File::open(file_name)?;
    let mut fbytes = Vec::new();
    for _ in 0..times {
        f.read_to_end(&mut fbytes);
        f.seek(SeekFrom::Start(0));
    }
    Ok(fbytes)
}

fn compress(cursor: &mut Cursor<Vec<u8>>, iterations: i32) {
    for _ in 0..iterations {
        let mut v: Vec<u8> = Vec::new();
        let mut compressor = snap::Writer::new(v);
        copy(cursor, &mut compressor);
        cursor.set_position(0);
        println!("{:?}", &v);
    }
}

fn main() {
    let mut args = env::args();
    let file_name = args.nth(1).unwrap();
    let concat_repetitions = args.nth(2).unwrap().parse::<i32>().unwrap();
    let iterations = args.nth(3).unwrap().parse::<i32>().unwrap();
    let data = read_file_as_bytes(&file_name, concat_repetitions).unwrap();
    let start = SystemTime::now();
    let mut data_cursor = Cursor::new(data);
    compress(&mut data_cursor, iterations);
    let end = SystemTime::now();
}
