# Intuition

숫자를 이진수로 변환한 후에 reverse() 메소드를 이용해 역순으로 변경

# Approach
1. 숫자를 2진수로 변환
2. 변환된 2진수를 역순으로 정렬
3. 역순으로 정렬된 2진수를 다시 정수로 변환


# Complexity
- Time complexity: $$O(1)$$
- Space complexity: $$O(1)$$

# Code
```js
var reverseBits = function(n) {
    let 이진수 = n.toString(2).padStart(32, '0');
    let 역순 = 이진수.split('').reverse().join('');
    let res = parseInt(역순, 2);

  return res;
};
```