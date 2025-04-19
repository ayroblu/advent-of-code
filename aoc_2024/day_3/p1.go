package main

import (
	"aoc/utils"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	total := 0
	for line := range utils.MustReadInput() {
		matches := re.FindAllStringSubmatch(line, -1)
		for _, match := range matches {
			total += utils.MustAtoi(match[1]) * utils.MustAtoi(match[2])
		}
	}
	println("total", total)
}
