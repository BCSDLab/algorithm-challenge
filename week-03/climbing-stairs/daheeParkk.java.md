[# Intuition
n-1일 경우와 n-2일 경우의 수를 더한 값을 반환한다.

# Approach
```java 
1. n이 1이면 1을 반환한다.
2. 배열의 index 1에는 1을, index 2에는 2를 저장한다. (= 방법의 수 저장)
3. 3부터 n이 될 때까지 for문을 돌린다.
  3-1. i개일 때 배열에 i-1과 i-2의 방법의 수를 더한 값을 저장한다.
4. 배열의 index가 n일 때 값을 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];

        if (n == 1) {
            return 1;
        }
        dp[1] = 1;
        dp[2] = 2;

        for (int i=3; i<=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    } 
}
```
]()
