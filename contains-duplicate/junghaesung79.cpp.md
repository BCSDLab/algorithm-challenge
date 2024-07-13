# Contains Duplicate
---
## 문제 해결 방법
---
* 1
  * input으로 제공된 vector(nums)의 size를 구한다.(vl)
  * nums를 set으로 변환하며 다음 그것의 size를 구한다.(sl)
  * 두 값을 비교하여 동일 여부에 따라 부울값을 반환한다.
* 2
  * 방법 1에서 set을 사용하던 것을 unordered_set으로 바꾼다.
* 3
  * vector를 순환하며 요소를 unordered_set에 추가한다.
  * 순환하며 이미 있는 요소일 경우 true를 반환한다.
  * 순환을 마칠 경우 false를 반환한다.
## 자료구조 선택
---
* vector 제공
* set
* unordered_set
## 성능
---
* 1
    * 시간 복잡도
      * vector의 요소들을 set에 삽입하는데 O(n log n)
      * vector와 set의 크기를 가져오는데 O(1)
    * 공간 복잡도
      * set을 생성할 때 vector의 모든 요소를 저장 O(n)
    * 평가
      * 삽입 시 성능 개선 가능성
* 2
    * 시간 복잡도
      * vector의 요소들을 set에 삽입하는데 O(n)
    * 공간 복잡도
      * set을 생성할 때 vector의 모든 요소를 저장 O(n)
* 3
    * 시간 복잡도
      * unordered_set 삽입 O(1)을 최대 n번 반복문 최악의 경우 O(n)
    * 공간 복잡도
      * vector의 모든 요소가 unordered_set에 추가되는 최악의 경우 O(n)
    * 평가
      * 중복된 요소를 빨리 발견할 수 있다면 더 빠르게 종료
      * 실제로 결과에서 가장 성능이 좋았다.
## 알게 된 것
---
* 리트코드를 처음 사용했다.
  * 입력이 매개변수로 주어진다.
  * 불리언을 직접 출력한다.
  * include 와 namespace 지정이 필요 없다.
  * 입력과 출력 모두 문자열로 처리하는 백준과 차이가 있다.
* 문제를 풀며 시간/공간 복잡도를 고려했다.
  * vector-set 변환에 시간 복잡도 O(n log n), unordered_set은 O(n)
  * 크기를 가져오는 데 시간 복잡도 O(1)
* (정렬) set과 unordered_set에 대해 더 알게 됐다.
  * set: 균형 이진 트리 기반 / unordered_set: 해시 테이블 기반
# Code
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set;

        for (int i : nums) {
            if (nums_set.find(i) != nums_set.end()) return true;
            nums_set.insert(i);
        }

        return false;
    }
};
```