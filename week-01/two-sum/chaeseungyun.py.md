# Intuition
리스트 내 두 수를 더했을 때 target이 되는 인덱스를 구한다.

# Approach
1. 브루트포스 방식을 사용했다
2. 중복을 없애기 위해 시작 인덱스와 다음 인덱스를 비교했다.


# Complexity
- Time complexity: $O(n^2)$
이중 반복분

- Space complexity: $O(n)$
리스트의 크기

# Code
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        
        return []
```
# Learned
-

# 여담
리트코드 1등 문제 풀이 방식이 어떤 건지 모르겠다.