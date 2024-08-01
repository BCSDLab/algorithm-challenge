# Intuition

2진 문자열로 변환해서 1의 개수를 센다.

# Approach

1. Python 3.10부터 도입된 int.bit_count() 메소드를 사용한다.

# Complexity
- Time complexity: $$O(1)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

```

