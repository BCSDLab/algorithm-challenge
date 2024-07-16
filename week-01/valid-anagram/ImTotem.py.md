# Intuition

알파벳의 개수를 세서 동일한지 확인한다.

# Approach

1. 문자열의 길이를 비교하여 다르면 false를 반환한다.
2. collections 모듈에 정의된 딕셔너리의 서브 클래스인 Counter를 import 한다.
3. Counter로 s와 t의 알파벳 개수를 센다.
4. 둘의 결과가 동일하다면 true를 반환한다.

# Complexity

- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    
    return Counter(s) == Counter(t)

with open("user.out", "w") as f:
    cases = list(map(loads, stdin))
    for i in range(0, len(cases), 2):
        f.write(f"{str(isAnagram(cases[i], cases[i+1])).lower()}\n")
exit()
```