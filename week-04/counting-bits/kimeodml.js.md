# Intuition

10진수를 2진수로 변환한 후 1의 개수를 세기

# Approach
1. toString() 메소드를 활용해 2진수로 변환
2. 변환된 2진수에 1이 존재하면 cnt 값을 증가하고 배열에 push

# Complexity
- Time complexity: $$O(n)$$
- Space complexity: $$O(n)$$

# Code
```js
var countBits = function(n) {
    let list = [];
    let res = [];
    for(let i = 0; i <=n;i++) {
        list.push(i.toString(2));
    }
    list.forEach((li)=> {
        let cnt = 0;
        for(let i = 0; i < li.length;i++) {
            if(li[i] === '1') {
                cnt++;    
            }
        }
        res.push(cnt)
    })

    return res;
};
```