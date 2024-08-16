# Container With Most Water
---
## 문제 해결 방법
---
1
* 컨테이너의 높이를 1씩 늘여가며 넓이 검사
2
* 좌우 포인터를 두고 컨테이너의 너비를 좁혀가며 넓이 검사
## 성능
---
* O(최대 높이) / O(1)
* O(n) / O(1)
## 알게 된 것
---
* 가상의 포인터를 두고 좁혀가며 푸는 문제에 익숙해진 것 같다.

## 코드
```cpp
class Solution {
 public:
  int maxArea(vector<int>& height) {
    int high = height.size() - 1;
    int low = 0;
    int area = 0;
    int currentHeight = 0;

    while (true) {
      int newArea = (high - low) * currentHeight;
      area = max(area, newArea);

      currentHeight++;

      while (height[low] < currentHeight) {
        if (high == low) return area;
        low++;
      }
      while (height[high] < currentHeight) {
        if (high == low) return area;
        high--;
      }
    }
  }
};

///

class Solution {
 public:
  int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int maxArea = 0;

    while (left < right) {
      int currentArea = min(height[left], height[right]) * (right - left);
      maxArea = max(maxArea, currentArea);

      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }

    return maxArea;
  }
};
````
