# Intuition
현재 인덱스의 이득과 지금까지 발견된 가장 작은 이득을 뺀 것이 가장 큰 것을 구한다.

# Approach
1. 가장 작은 값은 입력 배열을 0번째 인덱스로 초기화한다.
2. 가장 큰 값은 0으로 초기화 한다.
3. 입력 배열을 순회하면서 최적을 구한다.
    - 매 반복 마다 가장 작은 이득을 갱신한다.
    - 현재 반복 index의 이득에서 가장 작은 이득을 뺀 값(수익)과 max를 비교하여 max를 갱신한다.

# Complexity
- Time complexity: `O(n)`
    - 입력 배열을 순회하는 비용 `O(n)`
- Space complexity: `O(n)`
    - 추가 공간은 사용하지 않지만 입력 배열 `O(n)`

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 2 ms
Memory Usage: 61.8 MB
```java
class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int max = 0;
        for (int i = 0; i < prices.length; ++i) {
            max = Math.max(max, prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        return max;
    }
}
```

# Learned
