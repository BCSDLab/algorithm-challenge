func containsDuplicate(nums []int) bool {
	appeared := make(map[int]bool, len(nums))

	for _, num := range nums {
		appeared[num] = true
	}

	return len(appeared) != len(nums)
}
