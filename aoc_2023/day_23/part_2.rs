use std::collections::HashMap;
use std::collections::HashSet;

#[path = "../../utils/file.rs"]
mod file;

fn main() {
    let contents = file::read_file(file_abs!());
    //     let contents = "#.#####################
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
    traverse_graph(start, &grid, &mut graph, &mut seen);

    println!("running longest path algo...");
    if false {
        // takes around 6s
        let mut seen: HashSet<(usize, usize)> = HashSet::new();
        let result = longest_recur(start, &graph, &mut seen, end, 0);
        println!("Result: {}", result);
    }

    println!("using no hashing...");
    let (mut vec_graph, tuple_to_idx) = hash_to_vec_graph(&graph);
    let start_idx = tuple_to_idx[&start];
    let end_idx = tuple_to_idx[&end];

    let mut seen_vec = vec![false; vec_graph.len()];
    // let mut counter = 0;
    let result = longest_recur_vec(
        start_idx,
        &mut vec_graph,
        &mut seen_vec,
        end_idx,
        // &mut counter,
        0,
    );
    // println!("counter: {:?}", counter);
    println!("Result: {}", result)
}

type VecGraph = Vec<Vec<(usize, usize)>>;
fn hash_to_vec_graph(graph: &Graph) -> (VecGraph, HashMap<(usize, usize), usize>) {
    let mut vec_graph: VecGraph = Vec::new();
    let mut tuple_to_idx: HashMap<(usize, usize), usize> = HashMap::new();
    let mut get_with_default = |x: &(usize, usize), v: &mut Vec<Vec<(usize, usize)>>| -> usize {
        tuple_to_idx.get(x).copied().unwrap_or_else(|| {
            let result = v.len();
            tuple_to_idx.insert(*x, result);
            v.push(Vec::new());
            return result;
        })
    };
    for (k, v) in graph {
        let k_idx = get_with_default(k, &mut vec_graph);
        for (item, dist) in v {
            let edge_idx = get_with_default(item, &mut vec_graph);
            vec_graph[k_idx].push((edge_idx, *dist));
        }
    }
    return (vec_graph, tuple_to_idx);
}

type Graph = HashMap<(usize, usize), Vec<((usize, usize), usize)>>;
fn traverse_graph(
    start_point: (usize, usize),
    grid: &Vec<Vec<char>>,
    graph: &mut Graph,
    seen: &mut HashSet<(usize, usize)>,
) {
    // get all possible routes, filter by not previous
    // if routes.count > 1, done
    // go to next
    let points = get_points(start_point, grid);
    for point in points {
        if seen.contains(&point) {
            continue;
        }
        seen.insert(point);
        traverse_path(start_point, point, grid, graph, seen);
    }
}
fn traverse_path(
    start_point: (usize, usize),
    current_point: (usize, usize),
    grid: &Vec<Vec<char>>,
    graph: &mut Graph,
    seen: &mut HashSet<(usize, usize)>,
) {
    let mut prev_point = start_point;
    let mut last_point = current_point;
    let mut dist = 0;
    loop {
        dist += 1;
        let points = get_points(last_point, grid)
            .iter()
            .filter(|&p| *p != prev_point)
            .copied()
            .collect::<Vec<_>>();
        if points.len() != 1 {
            graph
                .entry(last_point)
                .or_insert(Vec::new())
                .push((start_point, dist));
            graph
                .entry(start_point)
                .or_insert(Vec::new())
                .push((last_point, dist));
            if !seen.contains(&last_point) {
                seen.insert(last_point);
                if points.len() > 1 {
                    traverse_graph(last_point, grid, graph, seen);
                }
            }
            return;
        }
        prev_point = last_point;
        seen.insert(last_point);
        last_point = *points.first().unwrap();
    }
}
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
    // counter: &mut usize,
    dist: usize,
) -> usize {
    // *counter += 1;
    if point == end_point {
        return dist;
    }
    let mut max = 0;
    seen.insert(point);
    for &(next_point, next_dist) in &graph[&point] {
        if seen.contains(&next_point) {
            continue;
        }
        let l = longest_recur(
            next_point,
            graph,
            seen,
            end_point,
            // counter,
            dist + next_dist,
        );
        max = max.max(l);
    }
    seen.remove(&point);
    max
}

fn longest_recur_vec(
    point: usize,
    graph: &VecGraph,
    seen: &mut Vec<bool>,
    end_point: usize,
    // counter: &mut usize,
    dist: usize,
) -> usize {
    // *counter += 1;
    if point == end_point {
        return dist;
    }
    let mut max = 0;
    seen[point] = true;
    for &(next_point, next_dist) in &graph[point] {
        if seen[next_point] {
            continue;
        }
        let l = longest_recur_vec(
            next_point,
            graph,
            seen,
            end_point,
            // counter,
            dist + next_dist,
        );
        max = max.max(l);
    }
    seen[point] = false;
    max
}
