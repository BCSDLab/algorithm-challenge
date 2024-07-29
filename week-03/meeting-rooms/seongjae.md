# Intuition
회의가 서로 겹치는지 확인하기 위해 회의를 시작 시간 기준으로 정렬한 후, 이전 회의의 끝나는 시간과 다음 회의의 시작 시간을 비교하

# Approach
1. 회의를 시작 시간 기준으로 정렬.
2. 각 회의를 순서대로 확인하면서, 이전 회의의 끝나는 시간과 현재 회의의 시작 시간을 비교.
3. 만약 현재 회의의 시작 시간이 이전 회의의 끝나는 시간보다 빠르면, 겹친다고 판단하고 false를 반환.
4. 모든 회의를 확인했을 때 겹치는 회의가 없으면 true를 반환.

# Complexity
- Time complexity: O(n log n)
회의 시간을 정렬하는 데 걸리는 시간.

- Space complexity: O(1) 
추가적인 메모리 사용이 거의 없음.


# Code
Runtime: ms Memory Usage: MB
```java
//  public class Interval {
//     int start, end;
//     Interval(int start, int end) {
//         this.start = start;
//         this.end = end;
//     }
// }
public class MeetingRooms920lintcode {
    public boolean canAttendMeetings(List<Interval> intervals) {
        int end = 0;
        for(Interval interval : intervals) {
            if (interval.start >= end) return false;
            else {
                end = interval.end;
            }
        }
        return true;
    }
}
```

# Learned
중국 사이트는 가입이 안되고 릿은 유료라 돌려보지 못했다.. 맞는지 모르겠다.
