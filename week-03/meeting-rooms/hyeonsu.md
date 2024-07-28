# Intuition
어디선가 많이본 그리디문제이다.
# Approach 
1. 입력요소를 정렬한다.
2. 현재 미팅의 시작시간이 이전 미팅의 종료시간보다 이전이면 미팅시간이 겹치는것이다.

# Complexity
- Time complexity: $O(nlog(n))$
	- 정렬비용: $O(nlog(n))$
	- 입력리스트 순회비용: $O(n)$
	→ $O(nlog(n))$
- Space complexity: $O(n)$

(n is length of `intervals`)
# Code
```java
public class Solution {

public boolean canAttendMeetings(List<Interval> intervals) {
	Collections.sort(intervals, (e1, e1) -> {
		return Integer.compare(a.start, b.start));
	});
	for (int i = 1; i < intervals.size(); i++) {
		if (intervals.get(i).start < intervals.get(i - 1).end) {
			return false;
		}
	}
	return true;
}
```

# learned
