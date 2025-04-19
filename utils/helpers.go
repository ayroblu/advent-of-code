package utils

import (
	"slices"
	"strconv"

	"github.com/samber/lo"
)

func MustAtoi(text string) int {
	num, err := strconv.Atoi(text)
	if err != nil {
		panic(err)
	}
	return num
}

func Abs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

// Clones the array and removes one item
func Delete[S ~[]E, E any](origArr S, i int) S {
	arr := make(S, len(origArr))
	copy(arr, origArr)
	arr = slices.Delete(arr, i, i+1)
	return arr
}

func MustAtoiSlice(slice []string) []int {
	return lo.Map(slice, func(value string, _ int) int { return MustAtoi(value) })
}
