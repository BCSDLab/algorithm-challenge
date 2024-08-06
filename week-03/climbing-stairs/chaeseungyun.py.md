# Intuition
각 단계별로 공식이 있을 것 같다.

# Approach
1. 1, 2번째 계단은 올라가는 개수를 한 눈에 파악할 수 있다.
2. 3번째 계단부터는 앞 두 단계 방법의 합으로 구할 수 있다.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(N)$$ (worst case for  skewed tree)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(N: size of node.)

# Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1: return 0
        if n == 1: return 1
        if n == 2: return 2

        tmp = [1, 2]
        for i in range(2, n):
            result = tmp[i - 1] + tmp[i - 2]
            tmp.append(result)
        
        return tmp[n-1]
```

# learn
-