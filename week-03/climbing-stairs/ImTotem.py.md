# Intuition

시작 값이 다른 피보나치 수열이다.

# Approach

1. 두 변수 a와 b를 사용하여 피보나치 수열의 연속된 두 항을 저장한다.
2. n번 반복하면서 a와 b를 갱신한다.
3. 각 반복에서 a는 이전의 b가 되고, b는 이전의 a와 b의 합이 된다.
4. n번 반복 후 b가 n번째 계단에 도달하는 방법의 수가 된다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        
        return b

```