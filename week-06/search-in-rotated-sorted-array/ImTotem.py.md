# Intuition

일반적인 이진 탐색을 변형하여, 회전된 배열의 특성을 고려해야 한다.

# Approach

1. 두 포인터 lo와 hi를 배열의 시작과 끝에 위치시킨다.
2. 중간 지점 mid를 계산한다.
3. `nums[mid]`가 target과 일치하면 mid를 반환한다.
4. 배열의 회전 여부에 따라 두 가지 경우로 나눈다:
	1. `nums[mid] < nums[hi]`: 오른쪽 부분이 정렬되어 있는 경우
		- `target`이 `nums[mid]`와 `nums[hi]` 사이에 있으면 왼쪽 포인터를 이동
		- 그렇지 않으면 오른쪽 포인터를 이동
	2. 그 외의 경우 (왼쪽 부분이 정렬되어 있는 경우)
		- `target`이 `nums[lo]`와 `nums[mid]` 사이에 있으면 오른쪽 포인터를 이동
		- 그렇지 않으면 왼쪽 포인터를 이동
5. `target`을 찾지 못하면 -1을 반환한다.

# Complexity
- Time complexity: $$O(log N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
        return -1

```

