#[path = "../../utils/file.rs"]
mod file;
use regex::Regex;
use std::collections::HashMap;

fn main() {
    let text_digits = HashMap::from([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);
    let keys = text_digits
        .keys()
        .map(|s| &**s)
        .collect::<Vec<_>>()
        .join("|");
    let pat = r"(\d|".to_owned() + &keys + r")";
    let pat_end = r".*".to_owned() + &pat + r".*?$";
    let re = Regex::new(&pat).unwrap();
    let re_end = Regex::new(&pat_end).unwrap();

    let contents = file::read_file(file_abs!());
    let lines = contents.split("\n").filter(|v| !v.is_empty());
    let mut sum = 0;
    for line in lines {
        let (_, [first]) = re.captures(line).unwrap().extract();
        let (_, [last]) = re_end.captures(line).unwrap().extract();
        let mapped_first = if text_digits.contains_key(first) {
            text_digits[first]
        } else {
            first
        };
        let mapped_last = if text_digits.contains_key(last) {
            text_digits[last]
        } else {
            last
        };
        let num = (mapped_first.to_owned() + mapped_last)
            .parse::<i32>()
            .unwrap();
        sum += num
    }
    println!("Result: {}", sum)
}
