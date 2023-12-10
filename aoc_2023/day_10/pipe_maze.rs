#[path = "../../utils/file.rs"]
mod file;

fn main() {
    let contents = file::read_file(file_abs!());
    let lines = contents
        .split("\n")
        .filter(|v| !v.is_empty())
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let (r, c) = lines
        .iter()
        .enumerate()
        .find_map(|(i, line)| line.iter().position(|&c| c == 'S').map(|c| (i, c)))
        .unwrap();
    let result = search(&lines, r, c);
    println!("Result: {}", result)
}

fn search(input: &Vec<Vec<char>>, start_r: usize, start_c: usize) -> usize {
    // look for connected pipes
    let search = [
        (start_r - 1, start_c),
        (start_r, start_c - 1),
        (start_r, start_c + 1),
        (start_r + 1, start_c),
    ];
    let start = (start_r, start_c);
    let locations = search
        .iter()
        .filter(|&&pos| search_loc(input, pos).contains(&start))
        .copied()
        .collect::<Vec<_>>();
    // for two connected pipes, take a step
    let mut current_locs = vec![(start, locations[0]), (start, locations[1])];
    let mut counter = 0;
    'outer: loop {
        counter += 1;
        let mut next = Vec::new();
        let curr = &current_locs;
        for (start, pos) in curr {
            // println!("start: {:?}, pos: {:?}", start, pos);
            let next_pos = search_loc(input, *pos)
                .iter()
                .copied()
                .filter(|v| *v != *start)
                .next()
                .unwrap();
            next.push((*pos, next_pos));
            if curr.iter().any(|v| v.1 == next_pos || v.0 == next_pos) {
                break 'outer;
            }
        }
        current_locs = next;
    }
    return counter;
}

fn search_loc(input: &Vec<Vec<char>>, (r, c): (usize, usize)) -> [(usize, usize); 2] {
    match input[r][c] {
        '|' => [(r - 1, c), (r + 1, c)],
        '-' => [(r, c - 1), (r, c + 1)],
        'L' => [(r - 1, c), (r, c + 1)],
        'J' => [(r - 1, c), (r, c - 1)],
        '7' => [(r, c - 1), (r + 1, c)],
        'F' => [(r, c + 1), (r + 1, c)],
        _ => [(r, c), (r, c)],
        // S and .
    }
}
