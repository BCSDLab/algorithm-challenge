# Intuition
처음엔 sort를 사용해서 접근하려고 했지만 시간복잡도가 정해져 있어서 이분 탐색으로 접근하였다.

# Approach
1. 배열 인덱스의 왼쪽과 오른쪽을 각각 start와 end로 초깃값을 설정한다.
2. 왼쪽 인덱스가 오른쪽 인덱스보다 작은 동안 반복하며 최솟값을 찾는다.
 2.1. 배열의 중간 인덱스를 mid로 설정하여 중간값이 오른쪽 값보다 크다면, 최소값은 오른쪽에 존재한다는 것을 의미
 2.2. 중간값이 오른쪽 값보다 작거나 같으면, 최소값은 왼쪽에 있거나 중간에 존재한다는 것을 의미
3. 결과적으로 오른쪽 인덱스와 왼쪽 인덱스가 같아질 때 최솟값이 결정된다.

# Complexity
- Time complexity: $O(log(n))$
- Space complexity: $O(n)$

# Code
```js
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    while(left < right) {
        let mid = Math.floor((left + right)/2);

        if(nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return nums[left];
};
```

# 여담
nums.sort((a,b)=>a-b); 로 구할 수 있지만 시간 복잡도가 nlogn이 된다.