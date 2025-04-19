//go:build ignore

package main

import (
	"aoc/utils"
	"regexp"
)

const doStr string = "do()"
const dontStr string = "don't()"

func main() {
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`)
	total := 0
	isEnabled := true
	for line := range utils.MustReadInput() {
		matches := re.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			switch match[0] {
			case doStr:
				isEnabled = true
			case dontStr:
				isEnabled = false
			default:
				if isEnabled {
					total += utils.MustAtoi(match[1]) * utils.MustAtoi(match[2])
				}
			}
		}
	}
	println("total", total)
}
