# Intuition

x의맨 왼쪽이나 오른쪽에서 비트 하나 떼내면 x보다 작아질 것이고, x보다 작아진 수의 1의 개수는 dp에 적혀있을것이다. 따라서 'dp[x보다 작은 어떤 수] + 떼어낸 비트'가 될 것이다.

# Approach

| idx | decimal | binary |
| :-: | :-----: | :----: |
|  0  |    0    |  000   |
|  1  |    1    |  001   |
|  2  |    2    |  010   |
|  3  |    3    |  011   |
|  4  |    4    |  100   |
|  5  |    5    |  101   |
|  6  |    6    |  110   |
|  7  |    7    |  111   |

## 1번 풀이

1. 맨 왼쪽 비트 → $x^{\lfloor \log_{2}{x} \rfloor}$ → 항상 1이다.
2. 맨 왼쪽 비트를 떼어낸다. → $x - x^{\lfloor \log_{2}{x} \rfloor}$
3. $f(x) = f(x - x^{\lfloor \log_{2}{x} \rfloor}) + 1$

## 2번 풀이

맨 오른쪽의 비트를 떼어낸다.

1. x >> 1은 x를 2로 나눈 몫이다. 이는 x의 이진 표현에서 마지막 비트를 제외한 수와 같다.
2. x & 1은 x의 마지막 비트가 1인지 0인지를 나타낸다 (홀수면 1, 짝수면 0).
3. dp[x]는 dp[x >> 1] (x를 2로 나눈 몫의 1의 개수) + (x & 1) (마지막 비트가 1인지 여부)와 같다.
4. $f(x) = f(\lfloor x \div 2 \rfloor) + (x \mod 2)$

- dp[3] = dp[1] + (3 & 1) = 1 + 1 = 2
- dp[5] = dp[2] + (5 & 1) = 1 + 1 = 2
- dp[6] = dp[3] + (6 & 1) = 2 + 0 = 2
- dp[7] = dp[3] + (7 & 1) = 2 + 1 = 3

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(N)$$

# Code
## 1번 풀이
```python
class Solution:
	def countBits(self, n: int) -> List[int]:
		dp = [0] * (n+1)
		for x in range(1, n+1):
			dp[x] = dp[x - 2**int(math.log2(x))] + 1

return dp
```

## 2번 풀이
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for x in range(1, n+1):
            dp[x] += dp[x >> 1] + (x & 1)
        
        return dp
```

