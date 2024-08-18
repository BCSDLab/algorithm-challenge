# Intuition
n의 오른쪽 끝 비트부터 result에 넣는다.

# Approach
```java
1. 32번 for문을 돈다.
1-1. result에 2를 곱한다.
1-2. result에 n과 1을 and 연산한 값을 더한다.
1-3. n의 비트열을 오른쪽으로 한칸 이동한다.
2. result를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;

        for (int i=0; i<32; i++) {
            result *= 2;
            result += n & 1;
            n = n >> 1;
        }
        return result;
    }
}
```
