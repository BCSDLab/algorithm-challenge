# Intuition
비트의 순서를 거꾸로 만든다.
# Approach
1. 결과를 저장할 변수를 0으로 초기화함.
2. ㅊ주어진 정수의 모든 32비트에 대해 반복함.
3. 매 반복마다 결과 변수를 왼쪽으로 1비트 이동시키고, 주어진 정수의 마지막 비트를 결과 변수에 추가함.
4. 주어진 정수를 오른쪽으로 1비트 이동시켜 다음 비트를 처리함.
5. 최종적으로 반전된 결과를 반환함.

# Complexity
- Time complexity: O(1)
32비트 정수를 처리하므로 항상 32번의 반복만 수행

- Space complexity: O(1)
추가적인 공간을 거의 사용하지 않으므로 O(1)

1ms 40.45MB
# Code
```java
public class ReverseBits190 {
    public int reverseBits(int n) {
        int res = 0;

        for (int i = 0; i < 32; i++) {
            res <<= 1;
            res += n & 1;
            n >>= 1;
        }

        return res;
    }
}
```

# learn
