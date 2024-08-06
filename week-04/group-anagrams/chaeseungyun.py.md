# Intuition
정렬을 통해 묶여질 수 있는 문자열을 찾고 그룹별로 카운트한다. 해시 테이블로 관리하면 좋겠다.

# Approach
1. 리스트를 순회하며 각 문자열을 정렬 후 딕셔너리에 저장한다.
2. 이미 있는 key라면 값을 추가하고 아니면 새롭게 만든다.
3. 딕셔너리의 value를 꺼내면 그것이 바로 정답

# Complexity
- Time complexity: $$O(nlogn)$$
반복문 n * 파이썬의 정렬 log n
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
딕셔너리 크기만큼 차지할 것이다.

# Code
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = {}

        for str in strs:
            sortedStr = ''.join(sorted(str))
            if (sortedStr in word):
                word[sortedStr].append(str)
            else:
                word[sortedStr] = [str]

        return word.values()
```

# learned
딕셔너리의 key로 list를 사용할 수 없다는 것을 배웠다. immutable만 값만 들어갈 수 있다.
join이라는 메소드를 배웠다. 리스트를 문자열로 변환할 수 있다.