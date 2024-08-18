# Intuition
two sum의 투 포인터를 활용한다

# Approach
1. 주어진 배열을 정렬한다.
2. low, high 포인터를 만들고 세 숫자의 합을 기준으로 좁혀나간다.
3. 합이 0보다 작으면 low를 증가시켜 0에 가깝게 하고 반대는 high를 감소하며 0에 가깝도록 한다.
4. 합이 0이면 튜플을 결과 set에 추가한다.
5. i를 배열의 길이 - 2 만큼 순회하면 끝

# Complexity
- Time complexity: $$O(n^2)$$
  - 입력 배열의 길이 n에 대하여, `i`, `j와 k`를 순회한다.

- Space complexity: $$O(n)$$
  
# Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                three = nums[i] + nums[low] + nums[high]
                if three < 0:
                    low += 1
                elif three > 0:
                    high -= 1
                else:
                    result.add((nums[i], nums[low], nums[high]))
                    low, high = low + 1, high - 1
        return list(result)
```

# learn
투 포인터에 대한 개념을 확실히 잡아간 듯하다. 다른 문제에도 적용할 수 있으면 좋겠다