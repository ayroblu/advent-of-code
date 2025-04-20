//go:build ignore

package main

import (
	"aoc/utils"
	"slices"
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
		fail := false
		for i := range len(update) {
		START:
			num := update[i]
			required := rules[num]
			inter := utils.SetIntersection(required, updateSet)
			seenSet := utils.SliceToSet(update[:i])
			for item := range inter {
				if _, ok := seenSet[item]; !ok {
					fail = true
					idx := slices.Index(update, item)
					if idx == -1 {
						panic("item not found")
					}
					update = slices.Delete(update, idx, idx+1)
					update = slices.Insert(update, i, item)
					goto START
				}
			}
		}
		if fail {
			total += update[len(update)/2]
		}
	}
	println("total", total)
}
