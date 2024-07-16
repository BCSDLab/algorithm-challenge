# Intuition

BF 알고리즘(무식하게 검사하기)

# Approach

1. 이중 반복문을 통해 일일이 비교
2. 두 값을 더한 값이 target과 같으면 반환

# Complexity

- 시간복잡도: O(n^2)
- 공간복잡도: O(1)

# Code
```js
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length;i++) {
        for(let j = i+1;j < nums.length;j++) {
            if(nums[i] + nums[j] === target) {
                return [i, j]
            }
        } 
    }
};
```