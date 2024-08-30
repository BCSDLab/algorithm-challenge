# Combination Sum
---
## 문제 해결 방법
---
* 인자로 받은 수를 total에 더해서 target과 비교하는 dfs를 만든다.
* 만약 같다면 지금까지의 조합을 result에 넣는다.
* 넘칠 경우 무시하고 모자랄 경우 자신 또는 다른 숫자를 total에 더하는 것을 반복한다.
## 자료구조 알고리즘
---
* 백트래킹
## 성능
---
* O(n ^ target) / O(target)
## 알게 된 것
---
* 백트래킹 어려워..
* 상상이 되더라도 구현하는 것도 힘들다...

## 코드
```cpp
class Solution {
 private:
  vector<vector<int>> result;
  vector<int> current;

  void dfs(const vector<int>& candidates, int target, int start, int total) {
    if (total > target) {
      return;
    }

    if (total == target) {
      result.push_back(current);
      return;
    }

    for (int i = start; i < candidates.size(); i++) {
      int num = candidates[i];
      current.push_back(num);
      dfs(candidates, target, i, total + num);
      current.pop_back();
    }
  }

 public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    dfs(candidates, target, 0, 0);
    return result;
  }
};
```
