# 3Sum
---
## 문제 해결 방법
---
* 배열을 정렬한다.
* 큰 쪽, 작은 쪽 끝에 포인터를 두고 그 사이에서 배열을 오가며 값을 찍는다.
* 세 가지 숫자를 더했을 때 0이 되는 수들을 찾아 배열로 만든다.
## 성능
---
* O(n^2) / O()
## 알게 된 것
---
* 어렵다...

# 코드
```cpp
class Solution {
 public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size() - 2; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) continue;
      int low = i + 1, high = nums.size() - 1;
      while (low < high) {
        int sum = nums[i] + nums[low] + nums[high];
        if (sum < 0)
          low++;
        else if (sum > 0)
          high--;
        else {
          result.push_back({nums[i], nums[low], nums[high]});
          while (low < high && nums[low] == nums[low + 1]) low++;
          while (low < high && nums[high] == nums[high - 1]) high--;
          low++;
          high--;
        }
      }
    }

    return result;
  }
};
```