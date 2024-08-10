# Intuition

각 요소의 빈도수를 계산하고, 빈도수에 따라 정렬한 후 상위 k개를 선택한다.

# Approach

1. collections.Counter를 사용하여 각 요소의 빈도수를 계산한다.
2. Counter의 most_common() 메소드를 사용하여 빈도수가 높은 순으로 k개의 요소를 선택한다.
3. 선택된 요소들의 키(값)만 리스트로 반환한다.

# Complexity
- Time complexity: $$O(N \log k)$$
	- Counter를 생성하는데 $O(N)$ 시간이 소요된다.
	- most_common(k)는 내부적으로 힙을 사용하여 $O(N \log k)$시간이 소요된다.

- Space complexity: $$O(N + k)$$
	- Counter 크기 N
	- 내부 힙 크기 k
# Code
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return list(dict(count.most_common(k)))
```

