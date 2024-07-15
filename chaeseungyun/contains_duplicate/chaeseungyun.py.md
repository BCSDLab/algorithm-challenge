# Intuition
리스트 내에 중복이 있는 지 검사한다.

# Approach
1. 리스트를 순회하며 값에 접근한다
2. 딕셔너리에 값을 key로 사용해서 저장
3. 딕셔너리에 이미 존재하는 key라면 True 반환


# Complexity
- Time complexity: $O(n)$
리스트 순회
딕셔너리 조회 및 삽입 -> O(n)

- Space complexity: $O(n)$
딕셔너리에 가장 많이 할당받아도 n

# Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        itemDict = {}

        for item in nums:
            if (item in itemDict): return True
            itemDict[item] = item
        
        return False
```
# Learned
딕셔너리를 그냥 사용하기만 했는데 내부가 해시 테이블로 구성되어있다는 것을 이제 알았다. 조회, 삽입, 삭제가 O(1)이라니 좋구나

# 여담
파이썬 자료구조에 대한 시간 복잡도 공부를 오랜만에 했다