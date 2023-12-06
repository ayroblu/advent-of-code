#[path = "../../utils/file.rs"]
mod file;

use regex::Regex;

fn main() {
    let contents = file::read_file(file_abs!());
    let re = Regex::new(
        r"Time:(.*)
Distance:(.*)",
    )
    .unwrap();
    let re_whitespace = Regex::new(r"\s+").unwrap();
    let (_, [times_str, distances_str]) = re.captures(&*contents).unwrap().extract();
    let time = re_whitespace
        .replace_all(times_str, "")
        .parse::<i64>()
        .unwrap();
    let distance = re_whitespace
        .replace_all(distances_str, "")
        .parse::<i64>()
        .unwrap();
    let mut total = 0;
    for i in 1..time {
        if (time - i) * i > distance {
            total += 1;
        }
    }
    println!("{}", total);
}
