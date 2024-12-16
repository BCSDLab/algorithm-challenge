# Intuition
브루트포스 밖에 생각이 안났다. 이러면 시간 초과인데..

# Approach

# Complexity
- Time complexity: $$O(n)$$
  

- Space complexity: $$O(n)$$
  

# Code
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        up = [1] * len(nums)

        for i in range(len(nums) - 1):
            up[i + 1] = up[i] * nums[i]

        down = [1] * len(nums)

        for i in range(len(nums) - 1, 0, -1):
            down[i - 1] = down[i] * nums[i]

        result = []
        for x in zip(up, down):
            result.append(x[0] * x[1])
        
        return result
```

# learn
풀이를 보고 풀었다. 이걸 dp라고 할 수 있는지 좀 더 탐구해봐야겠다