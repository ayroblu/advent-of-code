//go:build ignore

package main

import (
	"aoc/utils"
	"strings"
)

func main() {
	grid := [][]rune{}
	gr, gc := 0, 0
	for line := range utils.MustReadInput() {
		if idx := strings.IndexRune(line, '^'); idx != -1 {
			gr, gc = len(grid), idx
		}
		grid = append(grid, []rune(line))
	}
	total := 0
	for r, line := range grid {
		for c, v := range line {
			if v != '#' && v != '^' && checkLoop(grid, []int{gr, gc}, []int{r, c}) {
				total += 1
			}
		}
	}
	println("total", total)
}

func turn90(dir []int) []int {
	// Rotation matrix:
	//  0 1
	// -1 0
	return []int{dir[1], -dir[0]}
}

func checkLoop(grid [][]rune, guardPos []int, obstruction []int) bool {
	dir := []int{-1, 0}
	seen := map[Position]bool{}
	for {
		idx := Position{guardPos[0], guardPos[1], dir[0], dir[1]}
		if _, ok := seen[idx]; ok {
			return true
		}
		seen[idx] = true
		r, c := guardPos[0]+dir[0], guardPos[1]+dir[1]
		if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[r]) {
			return false
		}
		if grid[r][c] == '#' || (r == obstruction[0] && c == obstruction[1]) {
			dir = turn90(dir)
		} else {
			guardPos[0], guardPos[1] = r, c
		}
	}
}

type Position struct {
	r  int
	c  int
	dr int
	dc int
}
