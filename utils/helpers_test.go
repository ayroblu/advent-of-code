package utils

import (
	"reflect"
	"testing"
)

func TestDelete(t *testing.T) {
	arr := []int{3, 2, 1}
	newArr := Delete(arr, 0)
	deepEqual(t, &newArr, &[]int{2, 1})
	deepEqual(t, &arr, &[]int{3, 2, 1})
}

func deepEqual[S any](t *testing.T, a *S, b *S) {
	if !reflect.DeepEqual(*a, *b) {
		t.Error(*a, "is not deep equal to", *b)
	}
}
