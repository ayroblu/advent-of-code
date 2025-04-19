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
			if v != 'X' {
				continue
			}
			for _, dirRow := range []int{-1, 0, 1} {
				for _, dirCol := range []int{-1, 0, 1} {
					if dirRow == 0 && dirCol == 0 {
						continue
					}
					text, err := grid.slice(r, c, dirRow, dirCol)
					if err != nil {
						continue
					}
					if text == "XMAS" {
						total += 1
					}
				}
			}
		}
	}
	println("total", total)
}

func (grid Grid) slice(r, c, dirRow, dirCol int) (string, error) {
	r1 := r + dirRow*3
	if r1 < 0 || r1 >= len(grid) {
		return "", errors.New("Row doesn't have enough room")
	}
	c1 := c + dirCol*3
	if c1 < 0 || c1 >= len(grid[r]) {
		return "", errors.New("Column doesn't have enough room")
	}
	return string([]rune{grid[r][c], grid[r+dirRow][c+dirCol], grid[r+dirRow*2][c+dirCol*2], grid[r+dirRow*3][c+dirCol*3]}), nil
}
