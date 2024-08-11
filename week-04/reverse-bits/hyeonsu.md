# Intuition
입력 정수 n의 비트를 쉬프트 하면서 새로운 정수를 만든다.

# Approach
1. 정수 32개의 비트를 순회한다.
2. 입력 정수 n의 비트를 쉬프트하면서 reverseBit를 만든다.

# Complexity
- Time complexity: $O(1)$
    - 32비트이기 때문에 $O(1)$

- Space complexity: $O(1)$
    - 추가공간을 사용하지 않기 때문에 $O(1)$

# Code
```
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ret = 0;
        for(int i = 0; i < 32; ++i) {
            ret <<= 1;
            ret += n & 1;
            n >>= 1;
        }
        return ret;
    }
}
```

# Learned
비트연산에 대한 이해를 높일 수 있었습니다.