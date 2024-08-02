# Counting Bits
---
## 문제 해결 방법
---
1
* 이전 문제의 Brian Kernighan 알고리즘을 n만큼 반복하여 v를 구한다.
2
* 2의 배수마다 특정 수열이 반복되는 규칙을 찾아 동적 계획법을 사용한다.
## 자료구조 알고리즘
---
* Brian Kernighan 알고리즘
## 성능
---
* O(n) / O(n)
## 알게 된 것
---
* CPU 파이프라인 최적화를 위해 같은 복잡도라면 분기문(if 등)을 피하는 게 좋다.
---
## 코드
```cpp
class Solution {
 public:
  vector<int> countBits(int n) {
    vector<int> v(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      int t = i;
      int count = 0;
      while (t) {
        t &= (t - 1);
        count++;
      }

      v[i] = count;
    }

    return v;
  }
};

///

class Solution {
 public:
  vector<int> countBits(int n) {
    vector<int> v(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      int t = i;
      t |= t >> 1;
      t |= t >> 2;
      t |= t >> 4;
      t |= t >> 8;
      t |= t >> 16;
      int floorPow2 = (t + 1) >> 1;
      v[i] = v[i - floorPow2] + 1;
    }

    return v;
  }
};
```
