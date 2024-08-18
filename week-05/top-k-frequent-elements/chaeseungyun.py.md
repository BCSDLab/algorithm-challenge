# Intuition
사전을 이용하면 빈도수 체크하는데 편할 것 같다.

# Approach
1. 해시테이블을 만들고 key에 숫자를 넣고 value에 빈도수를 저장한다.
2. 값을 기준으로 정렬한다.
3. 뒤에서 k개를 뽑는다

# Complexity
- Time complexity: $$O(nlog(n))$$

- Space complexity: $$O(n+k)$$

# Code
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sortedList = sorted(freq, key=lambda num: freq[num])
        return sortedList[-k:]
```

