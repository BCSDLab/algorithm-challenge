# Intuition

0~n 까지 반복문을 돌면서 배열의 index 값과 일치하지 않으면 없는 숫자임을 확인

# Approach
1. 기존 숫자 배열 오름차순으로 정렬
2. 반복문을 통해 숫자가 비어 있으면 값 반환
  2.1. 현재 숫자와 i값이 일치하지 않으면 i 값을 반환
  2.2. 그렇지 않으면 0과 n 사이에 모든 숫자가 존재하다는 의미이기 때문에 n 다음 숫자 반환


# Complexity
- Time complexity: $$O(nlogn)$$
- Space complexity: $$O(n)$$

# Code
```js
var missingNumber = function(nums) {
    nums = nums.sort((a,b) => a - b)

    for(let i = 0; i < nums.length;i++) {
        if(nums[i] !==i) {
            return i;
        }
    }
    return nums.length;
};
```