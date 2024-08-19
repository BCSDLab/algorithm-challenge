# Intuition

제약조건
- `strs[i]` contains any possible characters out of `256` valid ASCII characters.

ASCII 에 포함되어 있지 않은 아무 문자로 연결한다.

# Approach

'ㄱ'을 구분자로 둔다.

1. 인코딩 (encode):
	- 리스트의 모든 문자열을 'ㄱ'으로 연결한다.

2. 디코딩 (decode):
	- 인코딩된 문자열을 'ㄱ'을 기준으로 분리하여 원래의 문자열 리스트로 복원한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(N)$$

# Code
```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        return "ㄱ".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("ㄱ")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

