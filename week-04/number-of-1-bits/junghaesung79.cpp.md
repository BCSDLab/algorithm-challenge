# Number of 1 Bits
---
## 문제 해결 방법
---
1
* bitset라이브러리를 사용하여 2진 문장으로 만든다.
* 1의 수를 센다.
2
* 비트연산자로 2진수 끝이 1인지 세며 >>한다.
3
* Brian Kernighan 알고리즘 사용한다.
* 오른 쪽에 있는 1을 없애가며 그것을 센다.
## 자료구조 알고리즘
---
* Brian Kernighan 알고리즘
## 성능
---
* O(1) / O(1)
## 알게 된 것
---
* bitset 라이브러리
* &과 >>의 활용
* Brian Kernighan 알고리즘
---
## 코드
```cpp
class Solution {
 public:
  int hammingWeight(int n) {
    bitset<32> bits(n);
    int count = 0;
    for (char i : bits.to_string()) {
      if (i == '1') count++;
    }

    return count;
  }
};

///

class Solution {
 public:
  int hammingWeight(int n) {
    int count = 0;
    while (n) {
      count += n & 1;
      n >>= 1;
    }

    return count;
  }
};

///

class Solution {
 public:
  int hammingWeight(int n) {
    int count = 0;
    while (n) {
      n &= (n - 1);
      count++;
    }

    return count;
  }
};
```
