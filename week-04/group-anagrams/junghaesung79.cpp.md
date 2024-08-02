# Group Anagrams
---
## 문제 해결 방법
---
* sort 함수를 사용한 후 unordered_map에 배열로 추가한다.
* unordered_map에서 배열 값들을 묶어서 반한다.
## 자료구조 알고리즘
---
* unordered_map
## 성능
---
* O(n * w log w) / O(n * w)
## 알게 된 것
---
* 알고리즘 스터디 초반에 했던 내용과 같은데 풀이를 잊었었다..
  * sort(s.begin(), s.end())
* 파이썬 내장 함수는 사기다.
  * for (const auto& [key, value]) vector.push_back(value); => map.values()
---
## 코드
```cpp
class Solution {
 public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagrams;
    for (string s : strs) {
      string sorted = s;
      sort(sorted.begin(), sorted.end());
      anagrams[sorted].push_back(s);
    }

    vector<vector<string>> result;
    for (const auto& [key, value] : anagrams) {
      result.push_back(value);
    }

    return result;
  }
};
```
