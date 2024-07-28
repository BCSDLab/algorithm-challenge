# Intuition

n의 값은 n-1과 n-2의 합과 같다 -> DP로 접근

# Approach

1. n+1의 길이로 배열 초기화
2. dp[0]과 dp[1]일 때의 경우의 수를 초기값으로 설정
3. 반복문을 통해 dp 배열을 채움

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var climbStairs = function(n) {
    let dp = new Array(n+1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    for(let i = 2; i < dp.length;i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }

    return dp[n];
};
```