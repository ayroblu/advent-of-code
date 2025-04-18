package main

import (
	"aoc/utils"
	"strings"
)

func main() {
	lines := utils.MustReadLines("input")
	rightCount := make(map[int]int)
	left, right := []int{}, []int{}
	for line := range lines {
		parts := strings.Split(line, "   ")
		a, b := utils.MustAtoi(parts[0]), utils.MustAtoi(parts[1])
		left, right = append(left, a), append(right, b)
		rightCount[b]++
	}
	total := 0
	for _, leftNum := range left {
		count := rightCount[leftNum]
		total += count * leftNum
	}
	println("total", total)
}
