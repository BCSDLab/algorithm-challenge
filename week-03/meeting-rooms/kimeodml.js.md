# Intuition

현재 회의의 끝시간과 다음 회의의 시작 시간이 겹치면 모든 회의에 참가하지 못하게 된다.

# Approach

1. 시작 시간을 기준으로 오름차순으로 정렬
2. 반복문을 활용해 회의 시간이 겹치는지 확인
	2.1. 현재 회의의 끝 시간이 다음 회의의 시작 시간보다 크면 회의 시간이 겹치는 것이므로 false를 반환
	2.2. 그렇지 않으면 true를 반환

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var canAttendMeetings= function(intervals) {
  intervals = intervals.sort((a, b) => a[0] - b[0]);
  for(let i = 0; i < intervals.length - 1;i++) {
    if(intervals[i][1] > intervals[i + 1][0]) {
      return false;
    }
  }
  return true;
}
```