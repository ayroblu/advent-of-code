#[path = "../../utils/file.rs"]
mod file;
use std::collections::HashMap;

use regex::Regex;

fn main() {
    let contents = file::read_file(file_abs!());
    let mut lines = contents.split("\n").filter(|v| !v.is_empty());
    let dir = lines
        .next()
        .unwrap()
        .split("")
        .filter(|v| !v.is_empty())
        .collect::<Vec<_>>();
    let mut graph: HashMap<&str, (&str, &str)> = HashMap::new();
    let re = Regex::new(r"(\w+) = \((\w+), (\w+)\)").unwrap();
    for line in lines {
        // build a graph
        let (_, [node, left, right]) = re.captures(line).unwrap().extract();
        graph.insert(node, (left, right));
    }
    let mut count = 0;
    let mut current = "AAA";
    while current != "ZZZ" && count < 1000000000 {
        match dir[count % dir.len()] {
            "L" => current = graph[current].0,
            "R" => current = graph[current].1,
            _ => {}
        };
        count += 1;
    }
    println!("Result: {}", count)
}
