# Intuition
이분 탐색으로 접근

# Approach
1. 왼쪽 부분이 정렬된 경우와 오른쪽 부분이 정렬된 경우를 나눠서 계산
2. target이 중간값에 속하면 중간 인덱스를 반환
3. target이 정렬된 왼쪽 부분에 속하는지 확인하고,
 3.1. 범위에 있다면 탐색 범위를 왼쪽 부분으로 좁히고,
 3.2. 범위에 없다면 오른쪽 부분으로 이동
4. 오른쪽 부분에 정렬된 경우도 3번 과정을 반복
5. 없다면 -1 반환

# Complexity
- Time complexity: $O(log(n))$
- Space complexity: $O(n)$

# Code
```js
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
};
```

# 여담
nums.indexOf(target);으로 구현 가능하다.