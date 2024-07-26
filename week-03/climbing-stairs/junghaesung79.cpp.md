# Climbing Stairs
---
## 문제 해결 방법
---
1. 
  * 조합(combination) 함수를 구현한다.
  * 계단 수를 적절히 나누어 조합의 결과를 누적한다.
2. 
  * n번째 방법 수는 n - 1과 n - 2번째 방법 수의 합이다.
  * dp에 N까지의 방법 수를 저장한다.
3. 
  * pre와 cur만을 사용하여 N번째 방법 수를 구한다.
## 자료구조 알고리즘
---
* 조합
* DP
## 성능
---
1. O(n^2) / O(1)
2. O(n) / O(n)
3. O(n) / O(1)
## 알게 된 것
---
* cpp로 구현하는 순열과 조합을 알았다.
* 조합으로 문제를 풀면 시간 복잡도가 크게(O(n^2)) 나온다.
## 코드
```cpp
class Solution {
 public:
  int climbStairs(int N) {
    int ways = 0;

    for (int n = N; n >= (N + 1) / 2; n--) {
      int r = N - n;
      ways += combinationCount(n, r);
    }

    return ways;
  }

 private:
  int combinationCount(int n, int r) {
    r = min(r, n - r);
    long long result = 1;
    for (int i = 1; i <= r; i++) {
      result *= (n - i + 1);
      result /= i;
    }

    return result;
  }
};

///

class Solution {
 public:
  int climbStairs(int N) {
    vector<int> dp(46);
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= N; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[N];
  }
};

///

class Solution {
 public:
  int climbStairs(int N) {
    int pre = 1;
    int cur = 2;

    if (N == 1) return pre;

    for (int i = 3; i <= N; i++) {
      int tmp = cur;
      cur += pre;
      pre = tmp;
    }

    return cur;
  }
};
```