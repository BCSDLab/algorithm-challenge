# Intuition
어디선가 본것같은 계단오르기 dp문제.. 백준에도 있던듯?

# Approach
1. step1, step1의 초깃값을 지정해준다.
2. 예를들어 step4의 경우의수는 step3에서 한칸 오른 경우의수 + step2에서 2칸으로 오른 경우의수 이다.

# Complexity
- Time complexity: $O(n)$
    - 입력 n만큼 순회하기 때문에 $O(n)$

- Space complexity: $O(n)$
    - 입력 n만큼의 dp배열을 만들기 때문에 $O(n)$

# Code
```
class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < dp.length; ++i) dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }
}

```

# Learned
이번에 풀어봤던 문제라서 쉽게 풀린것 같다. 예전에는 조금 고민했던 문제인데 지금은 술술풀린다.