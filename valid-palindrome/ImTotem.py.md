# Intuition
알파벳, 숫자만 남겨서 새로운 문자열을 만들고 소문자로 바꾼다.
새롭게 만든 문자를 뒤집어서 동일한지 판별한다.

# Approach
1. `filter(str.isalnum, s)`: 알파벳과 숫자만 남기고 다른 문자 제거
2. `''.join(...)`: 필터링된 문자들을 하나의 문자열로 결합
3. `.lower()`: 모든 문자를 소문자로 변환
4. 필터링된 문자열과 그 역순을 비교

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

with open("user.out", "w") as f:
    for case in map(loads, stdin):
        f.write(f"{str(isPalindrome(case)).lower()}\n")
exit()
```