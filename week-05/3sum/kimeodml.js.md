# Intuition
특정 조건을 만족하는 수 찾기 -> 투 포인터로 접근

# Approach
1. 주어진 배열을 오름차순으로 정렬한다.
2. 반복문을 통해 세 수의 합이 0이 되는 값을 res에 저장한다.
 2.1. 이때, 중복되는 숫자는 생략한다.
 2.2. 세 수의 합이 0보다 크면 끝값을 줄인다.
 2.3. 세 수의 합이 0보다 작으면 시작값을 증가시킨다.
 2.4. 세 수의 합이 0이면 결괏값에 저장하고 시작값을 증가시켜 추가로 가능한 조합을 찾는다.
3. 시작값이 끝값보다 작을 경우헤만 반복한다.

# Complexity
- Time complexity: $$O(n^2)$$
  - 중첩 반복문
- Space complexity: $$O(n)$$

# Code
```js
var threeSum = function(nums) {
    let res = [];
    nums.sort((a,b) => a - b);
    for(let i = 0; i < nums.length;i++) {
        if(i > 0 && nums[i] === nums[i-1]) continue;
        let start = i + 1;
        let end = nums.length - 1;

        while(start < end) {
            let sum = nums[i] + nums[start] + nums[end];

            if(sum > 0) {
                end--;
            } else if(sum < 0) {
                start++;
            } else {
                res.push([nums[i], nums[start], nums[end]]);
                start++;

                while(start < end && nums[start] === nums[start -1]) start++;
            }
        }
    }

    return res;
};
```

