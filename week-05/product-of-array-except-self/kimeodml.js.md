# Intuition
현재 위치의 왼쪽값과 오른쪽값의 곲들을 결괏값에 저장한다.

# Approach
1. 결과값의 초기 배열을 1로 설정한다.
2. 반복문을 순회하면서 현재 위치의 왼쪽에 있는 모든 값을 결과값에 저장하면서 왼쪽 곲 계산을 진행한다.
3. 오른쪽 곱 계산도 2번과 같이 동일하게 진행한다.


# Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(1)$$
 - 오른쪽, 왼쪽 값을 저장하는 공간
	
# Code
```js
var productExceptSelf = function(nums) {
    let res = Array.from(nums).fill(1);
    let left = 1;
    let right = 1;
    
    // 왼쪽 곱
    for(let i = 0; i < nums.length;i++) {
        res[i] *= left;
        left *=nums[i];
    }

    // 오른쪽 곱
    for(let i = nums.length - 1; i >= 0; i--) {
        res[i] *= right;
        right *= nums[i];
    }
    return res;

};
```

