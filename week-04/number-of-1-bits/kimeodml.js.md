# Intuition

이진수로 변환한 후 1의 개수 세기

# Approach
1. 숫자 n을 2진수로 변환 후 배열로 변경
2. 변환된 숫자에 1이 존재하면 개수 세기


# Complexity
- Time complexity: $$O(nlogn)$$
- Space complexity: $$O(n)$$

# Code
```js
var hammingWeight = function(n) {
    let cnt = 0;
    let 이진수 = n.toString(2);
    이진수 = 이진수.split('');
    for(let i = 0; i < 이진수.length;i++) {
        if(이진수[i] === '1') {
            cnt++;
        }
    }
    return cnt;
};
```