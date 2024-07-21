# Two Sum
---
## 문제 해결 방법
---

* nums의 요소가 키이고 인덱스가 값인 unordered_map(m)을 선언하고 nums의 크기만큼 순환한다.
* target과 인덱스를 빼서 보수를 만든다.
* m에 보수를 키로하는 쌍을 찾고 있다면 그것의 값(nums일 때의 인덱스)과 현재 인덱스의 배열을 반환한다.
* 없을 경우 m에 현재 인덱스의 키값을 넣는다.
## 자료구조 선택
---
* vector 제공
* unordered_map: 삽입에 O(1), 접근에 O(1)
## 성능
---
* nums 순환에 최악 O(n)
* unordered_map 저장에 최악 O(n)
* O(n) / O(n)
## 알게 된 것
---
* unordered_map 사용법
  * it는 pair 객체 가리킴 it -> first나 second로 키값 접근
  * it -> first / (\*it).first / pair.first
  * m.count(key) > 0 / m.find(key) != m.end() 존재 여부 확인
# Code

```cpp
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> m;

    for (int i = 0; i < nums.size(); i++) {
      int complement = target - nums[i];

      if (m.find(complement) != m.end()) {
        return {m[complement], i};
      }

      m[nums[i]] = i;
    }

    return {};
  }
};

```