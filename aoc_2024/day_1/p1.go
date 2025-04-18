package main

import (
	"aoc/utils"
	"slices"
	"strings"
)

func main() {
	lines := utils.MustReadLines("input")
	left, right := []int{}, []int{}
	for line := range lines {
		parts := strings.Split(line, "   ")
		a, b := utils.MustAtoi(parts[0]), utils.MustAtoi(parts[1])
		left, right = append(left, a), append(right, b)
	}
	slices.Sort(left)
	slices.Sort(right)
	total := 0
	for i, leftNum := range left {
		rightNum := right[i]
		total += utils.Abs(rightNum - leftNum)
	}
	println("total", total)
}
