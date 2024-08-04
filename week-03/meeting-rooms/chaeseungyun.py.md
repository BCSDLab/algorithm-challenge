# Intuition
특별한 생각이 안들어서 아쉽지만 브루트포스 방법 사용

# Approach
1. 이중 반복문을 사용해서 모든 경우에 대해 겹치는 시간이 있는지 파악
2. 있으면 false 리턴

# Complexity
- Time complexity: $$O(n^2)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(N)$$ (worst case for  skewed tree)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(N: size of node.)

# Code
```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
          for j in range(i + 1, len(intervals)):
            if (
              intervals[i][0] < intervals[j][1]
              and intervals[j][0] < intervals[i][1]
            ):
              return False
        return True
```

# learn
-