# Intuition
n의 첫번째 비트부터 1과 and 연산하여 1이면 count한다.

# Approach
```java
1. n이 0이 아닐동안 반복한다.
1-1. n과 1을 and 연산하여 1이면 count를 증가시킨다.
1-2. n의 비트열을 오른쪽으로 이동시키고 왼쪽의 빈공간은 0으로 채운다. 
2. count를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                count++;
            }
            n >>>= 1;
        }
        return count;
    }
}
```
