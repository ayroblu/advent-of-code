//go:build ignore

package main

import (
	"aoc/utils"
	"errors"
)

type Grid [][]rune

func main() {
	grid := Grid{}
	for line := range utils.MustReadInput() {
		runes := []rune(line)
		grid = append(grid, runes)
	}
	total := 0
	for r, line := range grid {
		for c, v := range line {
			if v != 'A' {
				continue
			}
			subtotal := 0
			for _, dirRow := range []int{-1, 1} {
				for _, dirCol := range []int{-1, 1} {
					text, err := grid.slice(r, c, dirRow, dirCol)
					if err != nil {
						continue
					}
					if text == "MAS" {
						subtotal += 1
					}
				}
			}
			if subtotal == 2 {
				total += 1
			}
		}
	}
	println("total", total)
}

func (grid Grid) slice(r, c, dirRow, dirCol int) (string, error) {
	r1 := r + dirRow
	r2 := r - dirRow
	if r1 < 0 || r1 >= len(grid) || r2 < 0 || r2 >= len(grid) {
		return "", errors.New("Row doesn't have enough room")
	}
	c1 := c + dirCol
	c2 := c - dirCol
	if c1 < 0 || c1 >= len(grid[r]) || c2 < 0 || c2 >= len(grid[r]) {
		return "", errors.New("Column doesn't have enough room")
	}
	return string([]rune{grid[r1][c1], grid[r][c], grid[r2][c2]}), nil
}
