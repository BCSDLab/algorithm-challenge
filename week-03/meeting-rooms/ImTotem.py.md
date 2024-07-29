# Intuition

정렬된 회의 목록에서 각 회의의 종료 시간이 다음 회의의 시작 시간보다 늦지 않아야 한다.

# Approach

1. 회의 시간 간격을 시작 시간 기준으로 오름차순 정렬한다.
2. 정렬된 리스트를 순회하며 각 회의의 종료 시간과 다음 회의의 시작 시간을 비교한다.
3. 현재 회의의 종료 시간이 다음 회의의 시작 시간보다 늦다면 False를 반환한다.
4. 모든 회의를 검사한 후 겹치는 시간이 없다면 True를 반환한다.

# Complexity
- Time complexity: $$O(n \log n)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True
```