//go:build ignore

package main

import (
	"aoc/utils"
	"strconv"
	"strings"
)

func main() {
	total := 0
	for line := range utils.MustReadInput() {
		parts := strings.Split(line, ": ")
		ans := utils.MustAtoi(parts[0])
		nums := utils.MustAtoiSlice(strings.Split(parts[1], " "))
		if operate(ans, nums[1:], nums[0]) {
			total += ans
		}
	}
	println("total", total)
}

func operate(ans int, nums []int, work int) bool {
	if len(nums) > 0 {
		return operate(ans, nums[1:], work+nums[0]) ||
			operate(ans, nums[1:], work*nums[0]) ||
			operate(ans, nums[1:], utils.MustAtoi(strconv.Itoa(work)+strconv.Itoa(nums[0])))
	}
	return ans == work
}
