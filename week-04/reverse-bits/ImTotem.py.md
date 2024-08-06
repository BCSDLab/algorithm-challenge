# Intuition

2진수 문자열로 변환하여 뒤집은 후 정수로 변환한다.

# Approach

1. `format(n, "032b")`를 사용하여 정수 n을 32비트 이진 문자열로 변환한다.
	- `032`는 전체 길이를 32로 지정하고, 필요하면 앞에 0을 채운다.
	- `b`는 이진수 형식을 나타낸다.
2. `[::-1]`로 문자열을 뒤집는다.
3. `int(..., 2)`로 뒤집은 이진 문자열을 다시 정수로 변환한다.

# Complexity
- Time complexity: $$O(1)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)
```

