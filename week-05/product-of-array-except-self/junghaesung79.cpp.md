# Product of Array Except Self
---
## 문제 해결 방법
---
* 결과 배열의 각각 요소에 대하여 자신을 기준으로 왼쪽과 오른쪽의 수들을 곱함
## 성능
---
* O(n) / O(n)

# 코드
```cpp
class Solution {
 public:
  vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, 1);

    int left = 1;
    for (int i = 0; i < n; i++) {
      result[i] *= left;
      left *= nums[i];
    }

    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
      result[i] *= right;
      right *= nums[i];
    }

    return result;
  }
};
```