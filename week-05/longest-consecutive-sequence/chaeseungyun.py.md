# Intuition
정렬을 하면 접근하기 쉬울 것 같다

# Approach
1. 리스트를 정렬한다.
2. 대소관계가 확실하므로 자신과 다음 원소를 비교하며 차가 1이면 h에 현재 가장 큰 연속된 수의 길이를 저장한다.
3. 현재 가장 긴 연속된 수의 길이와 지금까지 저장한 가장 큰 연속된 수의 길이를 비교해서 더 큰 값을 반환한다.

# Complexity
- Time complexity: $$O(nlog(n))$$

- Space complexity: $$O(n+m)$$

# Code
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## 파이썬 정렬함수 n log n
        if len(nums) == 0:
            return 0
        nums.sort()
        h = 1
        result = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                h += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                result = max(h, result)
                h = 1
        result = max(h, result)
        return result
```