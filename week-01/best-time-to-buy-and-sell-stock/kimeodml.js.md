# Intuition

초기값을 최소가격으로 설정한 후 최대 이익과 최소 가격을 업데이트

# Approach

1. 초기값을 최소 가격으로 설정
2. 반복문을 통해 buy을 업데이트
3. 현재의 가격과 buy의 차를 비교하여 profit을 업데이트

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(1)

# Code
```js
var maxProfit = function(prices) {
    let buy = prices[0];
    let profit = 0;
    for(let i = 1;i < prices.length;i++) {
        if(prices[i] < buy) {
            buy = prices[i];
        }else if(prices[i] - buy > profit) {
            profit = prices[i] - buy;
        }
    }
    return profit;
};
```