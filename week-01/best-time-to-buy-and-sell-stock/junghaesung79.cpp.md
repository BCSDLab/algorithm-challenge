# Best Time to Buy and Sell Stock
---
## 문제 해결 방법
---
* 최소 가격과 최대 이익을 선언한다.
* prices를 순환하며 그때마다의 최소 가격을 저장하고 최고가 아닐 경우 이익을 계산한다.
* 이익이 저장된 최대 이익보다 클 경우 계산 값을 최대 이익에 저장한다.
## 자료구조 선택
---
## 성능
---
* 한 번 배열 순환
* 단일 변수 저장
* O(n) / O(1)
## 알게 된 것
---
# Code
```cpp
class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    if (prices.empty()) return 0;

    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.size(); i++) {
      if (prices[i] < minPrice) {
        minPrice = prices[i];
      } else {
        maxProfit = max(maxProfit, prices[i] - minPrice);
      }
    }

    return maxProfit;
  }
};
```