#[path = "../../utils/file.rs"]
mod file;
use regex::Regex;

fn main() {
    let contents = file::read_file(file_abs!());
    let lines = contents.split("\n").filter(|v| !v.is_empty());
    let re = Regex::new(r"^\d$").unwrap();
    let mut sum = 0;
    for line in lines {
        let chars: Vec<_> = line.split("").filter(|char| re.is_match(char)).collect();
        let num = (chars[0].to_owned() + chars.last().unwrap())
            .parse::<i32>()
            .unwrap();
        sum += num
    }
    println!("Result: {}", sum)
}
