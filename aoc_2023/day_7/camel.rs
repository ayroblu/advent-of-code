use lazy_static::lazy_static;
use std::{cmp::Ordering, collections::HashMap};

#[path = "../../utils/file.rs"]
mod file;

fn main() {
    let contents = file::read_file(file_abs!());
    let mut lines = contents
        .split("\n")
        .filter(|v| !v.is_empty())
        .map(|line| {
            let mut parts = line.split(" ");
            let (cards, bid) = (parts.next().unwrap(), parts.next().unwrap());
            return (
                cards
                    .split("")
                    .filter(|v| !v.is_empty())
                    .collect::<Vec<_>>(),
                bid.parse::<i64>().unwrap(),
            );
        })
        .collect::<Vec<_>>();
    let mut sum = 0;
    lines.sort_by(|a, b| compare_hands(&a.0, &b.0));
    for (i, line) in lines.iter().enumerate() {
        sum += ((i as i64) + 1) * line.1
    }
    println!("Result: {}", sum)
}

fn compare_hands(a: &Vec<&str>, b: &Vec<&str>) -> Ordering {
    let ra = group_rank(a);
    let rb = group_rank(b);
    if ra > rb || ra < rb {
        return ra.cmp(&rb);
    }
    let matched_cards = a.iter().zip(b.iter());
    for (ca, cb) in matched_cards {
        let cra = card_rank(ca);
        let crb = card_rank(cb);
        if cra > crb || cra < crb {
            return cra.cmp(&crb);
        }
    }
    return Ordering::Equal;
}
fn group_rank(a: &Vec<&str>) -> i32 {
    let dups = get_dups(a);
    if dups[0] == 5 {
        return 6;
    } else if dups[0] == 4 {
        return 5;
    } else if dups[0] == 3 {
        if dups[1] == 2 {
            return 4;
        }
        return 3;
    } else if dups[0] == 2 {
        if dups[1] == 2 {
            return 2;
        }
        return 1;
    }
    return 0;
}
fn get_dups(a: &Vec<&str>) -> Vec<i32> {
    let mut dups: HashMap<&str, i32> = HashMap::new();
    for c in a {
        dups.insert(c, dups.get(c).unwrap_or_else(|| &0) + 1);
    }
    let mut values = dups.values().map(|v| *v).collect::<Vec<i32>>();
    values.sort();
    values.reverse();
    return values;
}
lazy_static! {
    static ref CARD_RANKS: HashMap<&'static str, i32> = HashMap::from([
        ("A", 14),
        ("K", 13),
        ("Q", 12),
        ("J", 11),
        ("T", 10),
        ("9", 9),
        ("8", 8),
        ("7", 7),
        ("6", 6),
        ("5", 5),
        ("4", 4),
        ("3", 3),
        ("2", 2),
    ]);
}
fn card_rank(c: &str) -> i32 {
    return *CARD_RANKS.get(c).unwrap();
}
