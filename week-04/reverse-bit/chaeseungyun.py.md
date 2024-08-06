# Intuition
파이썬 메소드를 활용한다.

# Approach
1. input을 32비트 이진수 형태의 문자열로 저장한다.
2. 슬라이싱을 통해 문자열을 뒤집고 십진수로 변환한다.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, '032b')[::-1], 2)
```

# learned
format() 이라는 메소드를 배웠다. 숫자를 문자열로 바꿀 수 있는 문자열인데, 두 번째 인자로 형식을 줄 수 있다. 코드에선 32비트의 이진수의 형태로 변환했다.