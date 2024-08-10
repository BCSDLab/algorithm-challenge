# Intuition

각 위치의 결과는 그 위치를 제외한 왼쪽의 모든 숫자들의 곱과 오른쪽의 모든 숫자들의 곱의 곱이다.

# Approach

1. 왼쪽에서 오른쪽으로 순회하며 각 위치까지의 왼쪽 누적 곱을 계산한다.
2. 오른쪽에서 왼쪽으로 순회하며 오른쪽 누적 곱을 계산하고, 이를 기존 결과와 곱한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        
        r = 1
        for i in range(n-1, -1, -1):
            ans[i] *= r
            r *= nums[i]
            
        return ans
```

