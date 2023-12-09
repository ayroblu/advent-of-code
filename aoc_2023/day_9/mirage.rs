#[path = "../../utils/file.rs"]
mod file;

fn main() {
    let contents = file::read_file(file_abs!());
    let result = contents
        .split("\n")
        .filter(|v| !v.is_empty())
        .map(|line| {
            let values = line
                .split(" ")
                .filter(|v| !v.is_empty())
                .map(|v| v.parse::<i64>().unwrap())
                .collect::<Vec<_>>();
            return predict(values);
        })
        .reduce(|acc, next| acc + next)
        .unwrap();
    println!("Result: {}", result)
}

fn predict(input: Vec<i64>) -> i64 {
    let mut current = input;
    let mut sum = 0;
    while !current.iter().all(|v| *v == 0) {
        sum += current.last().unwrap();
        current = current[1..]
            .iter()
            .enumerate()
            .map(|(i, next)| next - current[i])
            .collect();
    }
    return sum;
}
