# Missing Number
---
## 문제 해결 방법
---
* 1부터 n까지의 합(n * (n + 1) / 2)에 nums 숫자들을 뺀 후 반환한다.
## 자료구조 알고리즘
---
* 
## 성능
---
* O(n) / O(1)
## 알게 된 것
---
* 풀이에서 xor로 간단하게 풀어내는 것이 신기하다.
---
## 코드
```cpp
class Solution {
 public:
  int missingNumber(vector<int>& nums) {
    int result = nums.size() * (nums.size() + 1) / 2;
    for (int i : nums) {
      result -= i;
    }

    return result;
  }
};
```
