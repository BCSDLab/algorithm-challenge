# Intuition

투 포인터를 사용한다. 양 끝에서 시작하여 더 작은 높이를 가진 쪽을 이동시키면서 최대 면적을 갱신한다.

# Approach

1. 두 포인터 l과 r을 각각 배열의 시작과 끝에 위치시킨다.
2. 두 높이 중 작은 값과 두 포인터 사이의 거리를 곱하여 현재 면적을 계산한다.
3. 계산된 면적이 지금까지의 최대 면적보다 크면 갱신한다.
4. 두 높이 중 작은 쪽의 포인터를 안쪽으로 이동시킨다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        l, r = 0, len(height) - 1
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans

```

