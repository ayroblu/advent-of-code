package utils

import (
	"bufio"
	"os"
)

func MustReadInput() <-chan string {
	return MustReadLines("input")
}

func MustReadLines(path string) <-chan string {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	out := make(chan string)
	scanner := bufio.NewScanner(file)
	go func() {
		for scanner.Scan() {
			line := scanner.Text()
			out <- line
		}
		close(out)
		file.Close()
	}()

	// if err := scanner.Err(); err != nil {
	//   panic(err)
	// }
	return out
}

func MustReadFile(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return string(content)
}

func MustReadFileInput() string {
	return MustReadFile("input")
}
