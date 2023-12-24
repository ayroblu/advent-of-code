use std::cmp::max;
use std::collections::HashMap;
use std::collections::HashSet;

#[path = "../../utils/file.rs"]
mod file;

fn main() {
    let contents = file::read_file(file_abs!());
    // let contents = "#.#####################
    // #.......#########...###
    // #######.#########.#.###
    // ###.....#.>.>.###.#.###
    // ###v#####.#v#.###.#.###
    // ###.>...#.#.#.....#...#
    // ###v###.#.#.#########.#
    // ###...#.#.#.......#...#
    // #####.#.#.#######.#.###
    // #.....#.#.#.......#...#
    // #.#####.#.#.#########v#
    // #.#...#...#...###...>.#
    // #.#.#v#######v###.###v#
    // #...#.>.#...>.>.#.###.#
    // #####v#.#.###v#.#.###.#
    // #.....#...#...#.#.#...#
    // #.#########.###.#.#.###
    // #...###...#...#...#.###
    // ###.###.#.###v#####v###
    // #...#...#.#.>.>.#.>.###
    // #.###.###.#.###.#.#v###
    // #.....###...###...#...#
    // #####################.#";

    let grid = contents
        .split("\n")
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let sc = grid[0].iter().position(|&x| x == '.').unwrap();
    let start = (0, sc);
    let ec = grid.last().unwrap().iter().position(|&x| x == '.').unwrap();
    let end = (grid.len() - 1, ec);

    let mut graph: Graph = HashMap::new();
    let mut seen: HashSet<(usize, usize)> = HashSet::new();
    println!("traversing for graph...");
    traverse_graph(start, &grid, &mut graph, &mut seen, end);
    let mut seen: HashSet<(usize, usize)> = HashSet::new();
    println!("running longest path algo...");
    let result = longest_recur(start, &mut graph, &mut seen, end);
    println!("Result: {}", result)
}

type Graph = HashMap<(usize, usize), Vec<((usize, usize), usize)>>;
fn traverse_graph(
    start_point: (usize, usize),
    grid: &Vec<Vec<char>>,
    graph: &mut Graph,
    seen: &mut HashSet<(usize, usize)>,
    end_point: (usize, usize),
) {
    let points = get_points(start_point, grid);
    for point in points {
        // technically should have this
        // if is_node(point, grid) {
        //     graph
        //         .entry(point)
        //         .or_insert(Vec::new())
        //         .push((start_point, 1));
        //     graph
        //         .entry(start_point)
        //         .or_insert(Vec::new())
        //         .push((point, 1));
        //     if !seen.contains(&point) {
        //         traverse_graph(point, grid, graph, seen, end_point);
        //     }
        //     continue;
        // }
        if seen.contains(&point) {
            continue;
        }
        seen.insert(point);
        let mut last_point = start_point;
        let mut current_point = point;
        let mut counter = 0;
        loop {
            counter += 1;
            let new_points = get_points(current_point, grid);
            if new_points.len() > 2 || current_point == end_point {
                graph
                    .entry(current_point)
                    .or_insert(Vec::new())
                    .push((start_point, counter));
                graph
                    .entry(start_point)
                    .or_insert(Vec::new())
                    .push((current_point, counter));
                if new_points.iter().filter(|&p| !seen.contains(p)).count() > 0 {
                    traverse_graph(current_point, grid, graph, seen, end_point);
                }
                break;
            }
            assert_eq!(new_points.len(), 2);
            let temp = current_point;
            current_point = *new_points
                .iter()
                .filter(|&p| last_point != *p)
                .next()
                .unwrap();
            last_point = temp;
            seen.insert(current_point);
        }
    }
}
// fn is_node((r, c): (usize, usize), grid: &Vec<Vec<char>>) -> bool {
//     return get_points((r, c), grid).len() > 2;
// }
fn get_points((r, c): (usize, usize), grid: &Vec<Vec<char>>) -> Vec<(usize, usize)> {
    let dirs: [(isize, isize); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
    return dirs
        .iter()
        .filter_map(|(rd, cd)| {
            let (nr, nc) = (r.checked_add_signed(*rd), c.checked_add_signed(*cd));
            if let (Some(nr), Some(nc)) = (nr, nc) {
                if nr >= grid.len() || nc >= grid[0].len() {
                    return None;
                }
                if grid[nr][nc] == '#' {
                    return None;
                }
                return Some((nr, nc));
            }
            return None;
        })
        .collect::<Vec<_>>();
}

fn longest_recur(
    point: (usize, usize),
    graph: &Graph,
    seen: &mut HashSet<(usize, usize)>,
    end_point: (usize, usize),
) -> isize {
    // 55s run time
    if point == end_point {
        return 0;
    }
    let mut max_dist = -1000000000;
    seen.insert(point);
    for (next_point, next_dist) in &graph[&point] {
        if seen.contains(next_point) {
            continue;
        }
        let l = longest_recur(*next_point, graph, seen, end_point);
        let total_dist = l + *next_dist as isize;
        max_dist = max(total_dist, max_dist);
    }
    seen.remove(&point);
    return max_dist;
}
