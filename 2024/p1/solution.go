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

func solve(left []int, right []int) int {

	rightMap := make(map[int]int)
	for i := 0; i < len(right); i++ {
		if _, ok := rightMap[right[i]]; !ok {
			rightMap[right[i]] = 0
		}
		rightMap[right[i]]++
	}

	var similarities []int
	for i := 0; i < len(left); i++ {
		if _, ok := rightMap[left[i]]; ok {
			similarities = append(similarities, left[i]*rightMap[left[i]])
		} else {
			similarities = append(similarities, 0)
		}
	}

	sum := 0
	for _, similarity := range similarities {
		sum += similarity
	}

	return sum
}

func main() {
	left, right, err := readInput("input.txt")
	if err != nil {
		panic(err)
	}

	println(solve(left, right))
}
