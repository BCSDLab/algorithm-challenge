# Intuition
문자열 순서를 바꿨을 때 두 문자열이 서로 같은지 판별

# Approach
1. 각 문자열의 내 문자 개수를 센다
2. 문자열의 개수가 다르면 False
3. 서로 다른 문자가 발견되면 False


# Complexity
- Time complexity: $O(n)$
반복분

- Space complexity: $O(n)$
문자열의 크기

# Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictOfS= {}
        dictOfT = {}

        if (len(s) != len(t)): return False

        for item in s:
            if (item in dictOfS): dictOfS[item] += 1
            else: dictOfS[item] = 1

        for item in t:
            if (dictOfS.get(item) == None): return False
            if (item in dictOfT): dictOfT[item] += 1
            else: dictOfT[item] = 1

        keyOfT = list(dictOfT.keys())

        for item in keyOfT:
            if (dictOfS.get(item) == None): return False
            if (dictOfS[item] != dictOfT[item]): return False

        
        return True
```
# Learned
in 을 통해 딕셔너리에 존재하는 key인지 알아내기
딕셔너리 키를 리스트로 만들기

# 여담
실행 시킬 때마다 속도 차이가 큰 코드