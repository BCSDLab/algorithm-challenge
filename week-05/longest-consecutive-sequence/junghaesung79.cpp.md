# Longest Consecutive Sequence
---
## 문제 해결 방법
---
* nums를 unordered_set으로 바꾼다.
* unordered_set을 순회하며 각 값의 이전 값, 이후 값을 찾아 그 수를 카운트한다.
* 가장 큰 카운트를 구하여 반환한다.
## 성능
---
* O(n) / O(n)
## 알게 된 것
---
* 

# 코드
```cpp
class Solution {
 public:
  int longestConsecutive(vector<int>& nums) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int longest = 0;

    int current;
    int count;
    for (int num : numSet) {
      if (numSet.find(num - 1) == numSet.end()) {
        current = num;
        count = 1;

        while (numSet.find(current + 1) != numSet.end()) {
          current++;
          count++;
        }

        longest = max(longest, count);
      }
    }

    return longest;
  }
};
```