#Search In Rotated Sorted Array
-- -##문제 해결 방법-- -
    *이분 탐색을 하면서 mid가 target의 위치인지 확인하여 반환한다.
         *좌측이 정렬되어 있을 때,
    우측이 정렬되어 있을 때에 따라
            target이 있을 쪽을 골라서 low 또는 high를 바꾼다.
                *만약 while문을 빠져나올 경우 nums에 target이 없는 것이기 때문에 -
        1을 반환한다.##자료구조 알고리즘-- -
        *이분 탐색##성능-- -
        *O(log n) / O(1)##알게 된 것
            -- -
        *##코드
```cpp
        class Solution {
 public:
  int search(vector<int> &nums, int target) {
    int low = 0;
    int high = nums.size() - 1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (nums[mid] == target) return mid;

      if (nums[low] <= nums[mid]) {
        if (nums[low] <= target && target < nums[mid]) {
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      } else {
        if (nums[mid] < target && target <= nums[high]) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
    }

    return -1;
  }
};
```
