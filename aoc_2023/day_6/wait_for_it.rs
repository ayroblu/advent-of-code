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
    let times = re_whitespace
        .split(times_str)
        .filter(|x| !x.is_empty())
        .map(|x| x.parse::<i32>().unwrap());
    let distances = re_whitespace
        .split(distances_str)
        .filter(|x| !x.is_empty())
        .map(|x| x.parse::<i32>().unwrap());
    let races = times.zip(distances);
    let mut total = 1;
    for (time, distance) in races {
        let mut subtotal = 0;
        for i in 1..time {
            if (time - i) * i > distance {
                subtotal += 1;
            }
        }
        total *= subtotal;
    }
    println!("{}", total);
}
