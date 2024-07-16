# Intuition

구매 최솟값과 최대 이익을 갱신하며 리스트를 순회한다

# Approach

1. 더 낮은 구매 가격을 찾으면 갱신한다.
2. 현재 이익이 최대 이익보다 크면 갱신한다.

# Complexity

- Time complexity: $O(n)$
- Space complexity: $O(1)$

# Code
```python
def maxProfit(prices: List[int]) -> int:
    ans = 0

    buy = prices[0]
    for sell in prices:
        if sell < buy:
            buy = sell
        
        if (x:=sell - buy) > ans:
            ans = x
    
    return ans

with open("user.out", "w") as f:
    for case in map(loads, stdin):
        f.write(f"{maxProfit(case)}\n")
exit()
```