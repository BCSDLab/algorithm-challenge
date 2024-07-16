# Intuition
주식을 사고 판매할 때 가장 큰 수익을 계산한다.

# Approach
1. 내가 구매한 주식의 가격과 현재 주식의 가격을 비교해서 주식을 살지 혹은 팔지 판단한다.
2. 주식을 파는 경우는 maxProfit이 더 큰 경우이므로 maxProfit을 다시 계산한다.
3. 더 저렴한 주식을 샀다고 해도 maxProfit이 더 크다는 보장이 없으므로 계산하지 않는다.
4. maxProfit이 0이면 주식으로 이윤을 낼 수 없는 경우(가격이 계속 내려간 경우)


# Complexity
- Time complexity: $O(n)$
이중 반복분

- Space complexity: $O(n)$
리스트의 크기

# Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, maxProfit = 0, 0, 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if (buy < prices[i]):
                sell = prices[i]
                if (sell - buy > maxProfit): maxProfit = sell - buy
            if (buy > prices[i]): buy = prices[i]
        
        if (maxProfit > 0): return maxProfit
        else: return 0
```
# Learned
-

# 여담
인덱스 조정을 더 잘하고 싶다는 생각을 했다.