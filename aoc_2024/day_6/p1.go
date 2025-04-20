//go:build ignore

package main

import (
	"aoc/utils"
	"strings"
)

func main() {
	grid := [][]rune{}
	guardPos := []int{0, 0}
	for line := range utils.MustReadInput() {
		if idx := strings.IndexRune(line, '^'); idx != -1 {
			guardPos = []int{len(grid), idx}
		}
		grid = append(grid, []rune(line))
	}
	dir := []int{-1, 0}
	seen := map[int64]bool{}
	for {
		idx := int64(guardPos[0]<<32) | int64(guardPos[1])
		seen[idx] = true
		r, c := guardPos[0]+dir[0], guardPos[1]+dir[1]
		if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[r]) {
			break
		}
		if grid[r][c] == '#' {
			dir = turn90(dir)
		} else {
			guardPos[0], guardPos[1] = r, c
		}
	}
	println("total", len(seen))
}

func turn90(dir []int) []int {
	// Rotation matrix:
	//  0 1
	// -1 0
	return []int{dir[1], -dir[0]}
}
