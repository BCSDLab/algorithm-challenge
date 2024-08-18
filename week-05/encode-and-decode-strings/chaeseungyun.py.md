# Intuition
간단해보인다!

# Approach
1. 아스키 문자가 아닌 문자를 구분자로 두고 인코딩한다
2. 사용한 구분자를 통해 디코딩한다


# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        return "😄".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("😄")
```
