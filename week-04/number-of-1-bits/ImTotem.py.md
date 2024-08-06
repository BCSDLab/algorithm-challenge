# Intuition

2진 문자열로 변환해서 1의 개수를 센다.

# Approach

## 1번 풀이
1. Python 3.10부터 도입된 int.bit_count() 메소드를 사용한다.

## 2번 풀이
1. n의 가장 오른쪽 비트가 1인지 확인하고, 1이면 카운트를 증가시킨다.
2. n을 오른쪽으로 1비트 시프트한다.
3. n이 0이 될 때까지 1-2 과정을 반복한다.

# Complexity
- Time complexity: $$O(1)$$

- Space complexity: $$O(1)$$

# Code

## 1번 풀이
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

```

## 2번 풀이
```python
class Solution:
	def hammingWeight(self, n: int) -> int:
		cnt = 0
		while n:
			cnt += n & 1
			n >>= 1
		
		return cnt
```