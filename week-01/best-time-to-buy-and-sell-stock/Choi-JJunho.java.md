# Intuition

최솟값과 최대 이익률을 비교하며 값을 조회한다.

# Approach

주어진 배열을 전체 순회하면서 값을 다음 조건을 통해 비교한다.

1. 현재 가격이 최소 가격이면 갱신한다.
2. 현재 가격이 최소가격이 아니라면 차익을 비교하고, 기존 차익보다 크면 갱신한다.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```java
class Solution {
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
