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
    let mut result = Vec::new();
    input.iter().reduce(|prev, next| {
        result.push(next - prev);
        return next;
    });
    let last = input.last().unwrap();
    let inc: i64 = match !result.iter().all(|v| *v == 0) {
        true => predict(result),
        false => 0,
    };
    return last + inc;
}
