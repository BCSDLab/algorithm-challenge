# Intuition
리스트를 정렬하면 숫자가 순서대로 배치되는데 이때 인덱스를 이용하면 될 것 같다.

# Approach
1. 어느 숫자가 비었는지 접근하기 쉽도록 리스트를 정렬한다.
2. emnumerate를 이용해서 인덱스와 값을 가져온다.
3. 인덱스와 값이 일치하지 않으면 해당하는 인덱스의 값이 부재인 것이다.
4. 따라서 인덱스를 반환한다.
5. 반복문 내에서 찾지 못하면 마지막값이 부재인 것이다.
6. 따라서 리스트의 길이를 반환한다.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if (num != i): return i
        
        return len(nums)
```

# learned
정렬된 리스트는 순서가 보장되어 있으므로 인덱스로 쉽게 찾을 수 있었다.