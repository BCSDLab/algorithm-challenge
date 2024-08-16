# Find Minimum In Rotated Sorted Array
---
## 문제 해결 방법
---
1
* 배열을 한 번 순환하며 그때의 커지는 수를 저장한다.
* 만약 작아지는 경우(한 바퀴를 rotate한 경우) 그때 작아지는 값을 반환한다.
* 반복문을 빠져나온 경우(처음부터 오름차순인 경우) 첫 번째 요소를 반환한다.
2
* 이분 탐색을 진행하며 갑자기 숫자가 작아질 때를 찾아 반환한다.
## 자료구조 알고리즘
---
* 이분 탐색
## 성능
---
* O(n) / O(1)
* O(log n) / O(1)
## 알게 된 것
---
* 문제가 너무 단순하다고 생각했었는데 역시 더 효율적인 방법이 있었다.
  * 지금까지는 O(n)이 제일 빨랐던 문제들이었지만 이제는 O(log n)이 나왔다.
* 정렬된 배열 => 이분 탐색
* low + (high - low) / 2: 오버플로우 방지 관행

## 코드
```cpp
class Solution {
 public:
  int findMin(vector<int>& nums) {
    int compare = nums[0];
    for (int& i : nums) {
      if (i < compare) {
        return i;
      }

      compare = i;
    }

    return nums[0];
  }
};

///

class Solution {
 public:
  int findMin(vector<int>& nums) {
    int low = 1;
    int high = nums.size() - 1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (nums[mid - 1] > nums[mid]) {
        return nums[mid];
      }

      if (nums[0] < nums[mid]) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return nums[0];
  }
};
```
