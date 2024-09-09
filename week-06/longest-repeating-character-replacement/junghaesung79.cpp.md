# Longest Repeating Character Replacement
---
## 문제 해결 방법
---
* 백터에 각 알파벳의 빈도수를 저장한다.
* 문자열을 순환하며 그때의 문자를 파악하여 동작한다.
* 현재 윈도우 크기에서 maxCount를 뺀 값이 k보다 크면, 윈도우의 시작점을 이동한다.
* 순환이 끝나면 최대 길이를 반환한다.
## 자료구조 알고리즘
---
* 슬라이딩 윈도우 기법
## 성능
---
* O(n) / O(1)
## 알게 된 것
---
* 

## 코드
```cpp
class Solution {
 public:
  int characterReplacement(string s, int k) {
    vector<int> count(26, 0);
    int maxCount = 0;
    int start = 0;
    int maxLength = 0;

    for (int end = 0; end < s.length(); end++) {
      count[s[end] - 'A']++;
      maxCount = max(maxCount, count[s[end] - 'A']);

      if (end - start + 1 - maxCount > k) {
        count[s[start] - 'A']--;
        start++;
      }

      maxLength = max(maxLength, end - start + 1);
    }

    return maxLength;
  }
};
```
