package utils

import (
	"slices"

	"github.com/samber/lo"
)

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

func SliceToSet[S ~[]E, E comparable](slice S) map[E]bool {
	result := make(map[E]bool, len(slice))
	for _, item := range slice {
		result[item] = true
	}
	return result
}

func SetIntersection[S ~map[E]bool, E comparable](a, b S) map[E]bool {
	result := make(map[E]bool, len(a))
	for k := range a {
		if b[k] {
			result[k] = true
		}
	}
	return result
}
