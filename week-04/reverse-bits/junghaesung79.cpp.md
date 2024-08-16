# Reverse Bits
---
## 문제 해결 방법
---
* n의 끝 비트를 result의 끝에 넣어가며 비트를 이동시킨다.
## 자료구조 알고리즘
---
* 
## 성능
---
* O(1): 32번 반복 / O(1)
## 알게 된 것
---
* 파이썬은 사기다(format 내장 함수로 한 줄 가능)
---
## 코드
```cpp
class Solution {
 public:
  uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (int i = 0; i < 32; i++) {
      result = (result << 1) | (n & 1);
      n >>= 1;
    }
    return result;
  }
};
```
