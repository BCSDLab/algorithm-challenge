# Intuition
파이썬 메소드를 활용한다.

# Approach
1. 파이썬 메소드를 활용해 이진수 문자열로 만들고 1의 개수를 센다.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
count() 함수가 문자열 내부를 돌 것이므로 n
- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

# learned
bin() 메소드는 십진수를 이진수 문자열로 변환해준다.
count()는 문자열 내에 해당 문자가 몇 번 나타났는지 보여준다.