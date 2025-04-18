package main

import (
	"aoc/utils"
	"github.com/samber/lo"
	"strings"
)

func main() {
	numSafe := 0
	for line := range utils.MustReadInput() {
		numStrs := strings.Split(line, " ")
		nums := lo.Map(numStrs, func(text string, _ int) int { return utils.MustAtoi(text) })

		isSafe := true
		isAscending := true
		for i, num := range nums[1:] {
			previous := nums[i]
			diff := utils.Abs(num - previous)
			if diff < 1 || diff > 3 {
				isSafe = false
				break
			}
			if i == 0 {
				isAscending = num > previous
			} else {
				if isAscending != (num > previous) {
					isSafe = false
					break
				}
			}
		}
		if isSafe {
			numSafe += 1
		}
	}
	println("num safe", numSafe)
}
