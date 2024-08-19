# Intuition

정렬된 배열이 회전된 상태에서 최소값을 찾는 문제이다. 흔히 알고 있는 이분 탐색의 응용(?)이다.

# Approach

1. 두 포인터 lo와 hi를 배열의 시작과 끝에 위치시킨다.
2. 중간 지점 mid를 계산한다.
3. `nums[mid]`와 `nums[hi]`를 비교한다:
	- 만약 `nums[mid] < nums[hi]`라면, 최소값은 mid를 포함한 왼쪽 부분에 있다.
	- 그렇지 않다면, 최소값은 mid 오른쪽에 있다.
1. 탐색 범위를 좁혀가며 2-3 과정을 반복한다.

# Complexity
- Time complexity: $$O(\log N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo]

```

