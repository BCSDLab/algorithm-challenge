# Intuition

각 숫자가 수열의 시작점인지 확인하고 그 수열의 길이를 계산한다.

# Approach

1. 주어진 숫자들을 set으로 변환하여 중복을 제거한다.
2. 각 숫자 n에 대해:
	- n-1이 set에 없다면, n은 수열의 시작점이다.
	- n부터 시작하여 연속된 숫자가 set에 있는지 확인하며 수열의 길이를 계산한다.
3. 가장 긴 수열의 길이를 저장하고 최종적으로 반환한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(N)$$

# Code
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        nums = set(nums)

        for n in nums:
            if n-1 not in nums:
                streak = 1

                while n + streak in nums:
                    streak += 1
                
                ans = max(ans, streak)
        
        return ans
```

