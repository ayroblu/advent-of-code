//go:build ignore

package main

import (
	"aoc/utils"
	"strings"
)

func main() {
	contents := utils.MustReadFileInput()
	contentsParts := strings.Split(contents, "\n\n")
	rulesContents, updatesContents := contentsParts[0], contentsParts[1]
	rulesText := strings.Split(rulesContents, "\n")
	rules := map[int]map[int]bool{}
	for _, text := range rulesText {
		rule := strings.Split(text, "|")
		after := utils.MustAtoi(rule[1])
		if rules[after] == nil {
			rules[after] = map[int]bool{utils.MustAtoi(rule[0]): true}
		} else {
			rules[after][utils.MustAtoi(rule[0])] = true
		}
	}

	total := 0
	for updateText := range strings.SplitSeq(updatesContents, "\n") {
		update := utils.MustAtoiSlice(strings.Split(updateText, ","))
		updateSet := utils.SliceToSet(update)
		for i, num := range update {
			required := rules[num]
			inter := utils.SetIntersection(required, updateSet)
			for _, item := range update[:i] {
				if _, ok := inter[item]; !ok {
					goto DONE
				}
			}
		}
		total += update[len(update)/2]
	DONE:
	}
	println("total", total)
}
