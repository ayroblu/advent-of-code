package utils

import (
	"strconv"
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
