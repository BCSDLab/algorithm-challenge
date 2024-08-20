# Intuition
양 끝의 높이를 비교하는 문제여서 투 포인터를 활용하였다.

# Approach
1. 높이의 양 끝을 비교하며 최소 높이를 찾는다.
2. 동시에 너비를 계산한다.
3. 갱신된 최소 높이와 너비를 곱해 최대 면적을 갱신한다.


# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(1)$

# Code
```js
var maxArea = function(height) {
    let start = 0;
    let end = height.length - 1;
    let maxWater = 0;
    while(start < end) {
        let water = (end - start) * Math.min(height[start], height[end]);
        maxWater = Math.max(maxWater, water);
        if(height[start] > height[end]) {
            end--;
        } else {
            start++;
        }
    }
    return maxWater;
};
```