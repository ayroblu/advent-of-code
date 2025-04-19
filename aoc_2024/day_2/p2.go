//go:build ignore

package main

import (
	"aoc/utils"
	"strings"

	"github.com/samber/lo"
)

func main() {
	numSafe := 0
	for line := range utils.MustReadInput() {
		numStrs := strings.Split(line, " ")
		nums := lo.Map(numStrs, func(text string, _ int) int { return utils.MustAtoi(text) })

		if safe(nums, false) {
			numSafe += 1
		}
	}
	println("num safe", numSafe)
}

func safe(nums []int, skip bool) bool {
	isAscending := true
	for i, num := range nums[1:] {
		previous := nums[i]
		diff := utils.Abs(num - previous)
		if diff < 1 || diff > 3 {
			if skip {
				return false
			}
			return safe(utils.Delete(nums, i), true) || safe(utils.Delete(nums, i+1), true)
		}
		if i == 0 {
			isAscending = num > previous
		} else {
			if isAscending != (num > previous) {
				if skip {
					return false
				}
				if i == 1 && safe(utils.Delete(nums, 0), true) {
					return true
				}
				return safe(utils.Delete(nums, i), true) || safe(utils.Delete(nums, i+1), true)
			}
		}
	}
	return true
}
