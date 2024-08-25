# Intuition
배열을 오름차순으로 정렬한 후 현재의 값이 이전값의 차가 1이면 연속된 수열을 증가한다.

# Approach

1. 주어진 배열을 오름차순으로 정렬한다.
2. 빈 배열일 경우 0으로 반환한다.
3. 현재의 숫자가 이전 숫자보다 1 크면 연속된 수열의 길이를 증가한다.
4. 현재의 숫자가 이전의 숫자보다 1 크기 않고, 값이 일치하지 않으면(=연속된 수열이 끊긴 경우) 연속된 수열의 길이를 결괏값에 갱신한다.
5. 반복문이 끝난 후에 저장된 값이 연속된 최대 수열의 길이일 수 있으므로 결괏값에 다시 갱신한다.

# Complexity
- Time complexity: $$O(nlogn)$$
  - 정렬로 인한 시간복잡도
- Space complexity: $$O(n)$$

# Code
```js
var longestConsecutive = function(nums) {
    nums.sort((a,b)=>a-b);
    let cnt = 1;
    let res = 1;
    if(nums.length === 0) return 0;
    for(let i = 1; i < nums.length;i++) {
        if(nums[i] - nums[i-1] === 1) {
            cnt++;
        }else if(nums[i] !== nums[i - 1]) {
            res = Math.max(res, cnt);
            cnt = 1;
        }
    }

    res = Math.max(res, cnt);

    return res;
};
```

