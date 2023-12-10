use std::collections::{HashMap, HashSet};

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
    let mut pipe: HashMap<(usize, usize), (usize, usize)> = HashMap::new();
    search(&lines, r, c, &mut pipe);
    let mut seen = HashSet::new();
    pipe.iter().for_each(|(&p, _next)| {
        seen.insert(p);
    });
    let mut sum = 0;
    for (p, next) in &pipe {
        let mut traverse: Vec<(usize, usize)> = Vec::new();
        let (r, c) = *p;
        match lines[r][c] {
            '|' => {
                if next.0 < r {
                    traverse.push((r, c + 1));
                } else {
                    traverse.push((r, c - 1));
                }
            }
            '-' => {
                if next.1 > c {
                    traverse.push((r + 1, c))
                } else {
                    traverse.push((r - 1, c))
                }
            }
            'L' => {
                if next.1 > c {
                    traverse.push((r + 1, c));
                    traverse.push((r, c - 1));
                }
            }
            'J' => {
                if next.0 < r {
                    traverse.push((r + 1, c));
                    traverse.push((r, c + 1));
                }
            }
            '7' => {
                if next.1 < c {
                    traverse.push((r - 1, c));
                    traverse.push((r, c + 1));
                }
            }
            'F' => {
                if next.0 > r {
                    traverse.push((r, c - 1));
                    traverse.push((r - 1, c));
                }
            }
            _ => (),
        };
        loop {
            let mut temp: Vec<(usize, usize)> = Vec::new();
            for pos in traverse {
                if seen.contains(&pos) {
                    continue;
                }
                seen.insert(pos);
                let (r, c) = pos;
                sum += 1;
                let search = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)];
                search.iter().filter(|p| !seen.contains(p)).for_each(|p| {
                    temp.push(*p);
                });
            }
            if temp.len() == 0 {
                break;
            }
            traverse = temp;
        }
    }
    println!("Result: {}", sum)
}

fn search(
    input: &Vec<Vec<char>>,
    start_r: usize,
    start_c: usize,
    pipe: &mut HashMap<(usize, usize), (usize, usize)>,
) -> usize {
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
    let mut current_loc = (start, locations[0]);
    pipe.insert(start, locations[0]);
    pipe.insert(locations[1], start);
    // let mut current_loc = (start, locations[1]);
    // pipe.insert(start, locations[1]);
    // pipe.insert(locations[0], start);
    let mut counter = 0;
    'outer: loop {
        counter += 1;
        let (prev, pos) = &current_loc;
        // println!("start: {:?}, pos: {:?}", start, pos);
        let next_pos = search_loc(input, *pos)
            .iter()
            .copied()
            .filter(|v| *v != *prev)
            .next()
            .unwrap();
        pipe.insert(*pos, next_pos);
        if next_pos == start {
            break 'outer;
        }
        current_loc = (*pos, next_pos);
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
