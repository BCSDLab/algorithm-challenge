# Meeting Rooms
---
## 문제 해결 방법
---
* start가 작은 순서로 정렬한다.
* i번째 요소의 start가 i - 1번째 요소의 end보다 빠르다면 false를 반환한다.
* 문제 없이 순환을 마칠 경우 true를 반환한다.
## 자료구조 알고리즘
---
* 
## 성능
---
* 정렬에 O(n log n)
* O(n log n) / O(1)
## 알게 된 것
---
* c++의 람다 함수를 알게 되었다.
  * js의 콜백 함수와 유사. 익명함수로써의 기능
  * 캡처 절[], 매개변수 목록(), 반환 타입 ->, 함수 본문 {}
  * sort 등의 STL 알고리즘 함수에 활용
## 코드
```cpp/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
 public:
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  bool canAttendMeetings(vector<Interval>& intervals) {
    sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
      return a.start < b.start;
    })

        for (int i = 1; i < intervals.size(); i++) {
      if (intervals[i].start < intervals[i - 1].end) {
        return false;
      }
    }

    return true;
  };
  ```