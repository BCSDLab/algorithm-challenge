# Intuition
price가 작으면 저장하고, 크면 작은 price와 차이를 계산해 가장 큰 profit을 찾는다.

# Approach
```java
1. minPrice에 Integer의 가장 큰 값을 넣고, maxProfit에 0을 넣는다.
2. for문으로 prices 배열을 처음부터 돈다.
2-1. price가 minPrice보다 작으면 저장한다.
2-2. price가 minPrice보다 크고 minPrice와 차이가 maxProfit보다 크면 maxProfit에 저장한다.
3. maxProfit을 반환한다.
```

# Code
```java
class Solution {
    public int maxProfit(int[] prices) {
        int dayCount = prices.length;
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int day=0; day<prices.length; day++) {
            int price = prices[day];
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
