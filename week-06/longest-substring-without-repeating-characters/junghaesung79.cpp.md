# Longest Substring Without Repeating Characters
---
## 문제 해결 방법
---
* s를 순환하며 반복되지 않는 문자들을 unordered_map에 넣는다.
* 순환 중 같은 문자가 나올 경우 전에 나온 그 문자의 위치와 현재 start 변수를 비교해서 더 큰 값을 찾는다.
* 각각의 순환마다 문자열의 길이를 파악하여 가장 길 때를 반환한다.
## 자료구조 알고리즘
---
* 슬라이딩 윈도우 기법
## 성능
---
* O(n) / O(min(m, n))
## 알게 된 것
---
* 슬라이딩 윈도우 기법
  * 고정 크기 윈도우, 가변 크기 윈도우, 특정 조건을 만족하는 최소 윈도우 찾기 문제에서 사용

** 코드
```cpp
class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int result = 0;
    unordered_map<char, int> charMap;
    int start = 0;

    for (int end = 0; end < s.size(); end++) {
      char& c = s[end];
      if (charMap.find(c) != charMap.end()) {
        start = max(start, charMap[c] + 1);
      }
      charMap[c] = end;
      result = max(result, end - start + 1);
    }

    return result;
  }
};
```
