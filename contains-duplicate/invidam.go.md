# Intuition
등장 여부를 기록하는 배열을 이용하여 중복을 검사한다.
# Approach
1. 등장 여부를 저장하는 배열 (`apperead`)를 선언한 후, 원본 배열(`nums`)를 순회하며 등장 여부를 갱신한다.
2. 등장한 수들의 종류(`len(appeared)`)와 갯수(`len(nums)`)가 다르다면, 중복이 있는 경우로 처리하고 같다면, 중복이 없는 경우로 처리한다.

# Complexity
- Time complexity: $O(n)$
    - 배열의 길이를 n이라고 했을 때, 모든 원소를 순회하는 비용 `O(n)`이 소모된다.
- Space complexity: $O(n)$
    - 배열의 길이를 n이라고 했을 때, 원소들을 저장하는 배열이 `O(n)`을 소모한다.

# Code
```go
func containsDuplicate(nums []int) bool {
	appeared := make(map[int]bool, len(nums))

	for _, num := range nums {
		appeared[num] = true
	}

	return len(appeared) != len(nums)
}

```

# Learned
솔루션을 참고하였는데, map 선언시 초기 용량을 설정하여 성능을 향상시킬 수 있다는 것을 배웠다.


# 여담
솔루션을 참고하여 최종 반환문을 수정하였다. 좀 더 가독성이 높아졌다.