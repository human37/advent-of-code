package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func readInput(path string) ([]int, []int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var left []int
	var right []int
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		leftNum, err := strconv.Atoi(parts[0])
		if err != nil {
			return nil, nil, err
		}
		rightNum, err := strconv.Atoi(parts[1]) 
		if err != nil {
			return nil, nil, err
		}
		left = append(left, leftNum)
		right = append(right, rightNum)
	}
	return left, right, nil
}

func sort(arr []int) []int {
	sorted := make([]int, len(arr))
	copy(sorted, arr)
	for i := 0; i < len(sorted)-1; i++ {
		for j := 0; j < len(sorted)-i-1; j++ {
			if sorted[j] > sorted[j+1] {
				sorted[j], sorted[j+1] = sorted[j+1], sorted[j]
			}
		}
	}
	return sorted
}

func abs(a int, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func solve(left []int, right []int) int {
	leftSorted := sort(left)
	rightSorted := sort(right)

	var distances []int
	for i := 0; i < len(leftSorted); i++ {
		distances = append(distances, abs(leftSorted[i], rightSorted[i]))
	}

	sum := 0
	for _, distance := range distances {
		sum += distance
	}

	return sum

}

func main() {
	left, right, err := readInput("example-input.txt")
	if err != nil {
		panic(err)
	}

	println(solve(left, right))

}
