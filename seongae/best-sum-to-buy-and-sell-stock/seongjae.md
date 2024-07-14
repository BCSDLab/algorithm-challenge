# 첫시도

# Intuition
주어진 배열에서 매일의 주식 가격을 비교하여 최대 이익을 찾기 위해 가능한 모든 경우를 확인한다.

# Approach
1. 이중 for문을 사용하여 모든 가능한 매수와 매도 조합을 확인한다.
2. 각각의 조합에 대해 이익을 계산하고 최대 이익을 업데이트한다.

# Complexity
- Time complexity: `O(n^2)`
    - 이중 반복문
- Space complexity: `O(1)`
    - 추가적인 메모리를 사용하지 않음

# Code
시간복잡도: `O(n^2)`
공간복잡도: `O(1)`
Runtime: Time Limit Exceeded
Memory Usage: Time Limit Exceeded로 확인 불가

```java
public class BestSumToBuyAndSellStock121 {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                int profit = prices[j] - prices[i];
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }

        return maxProfit;
    }
}
```

# Learned
이중 for 문으로 모든 것을 개산하는 것은 역시 매우 비효율적이라는 것을 알았다.

# 두번째 시도
# Intuition
한 번의 순회로 최소 가격을 갱신하면서 최대 이익을 계산할 수 있다.

# Approach
1. 배열을 순회하면서 최소 가격을 기록하며, 
2. 현재 가격에서 최소 가격을 뺀 값을 이익으로 계산하고, 최대 이익을 갱신한다.

# Complexity
- Time complexity: `O(n)`
    - 한번 돌면서 다 끝나기 때문
- Space complexity: `O(1)`
    - 입력 배열 제외 O(1)

# Code
시간복잡도: `O(n)`
공간복잡도: `O(1)`
Runtime: 2 ms
Memory Usage: 61.9 MB
```java
public class BestSumToBuyAndSellStock121 {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }

        return maxProfit;
    }
}
```

# Learned
