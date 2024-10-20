# Intuition
0부터 n까지 1과 and 연산을 하여 개수를 저장한다.

# Approach
```java
1. 0부터 1까지 for문을 돈다.
2. 1과 and 연산하여 1이면 count를 증가시킨다.
3. n의 비트열을 오른쪽으로 이동시키고 왼쪽의 빈공간은 0으로 채운다.
4. n이 0되었을 때 count를 저장한다.
5. count들이 저장된 arr를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n+1];

        for (int i=0; i<=n; i++) {
            arr[i] = countOneBit(i);
        }
        return arr;
    }

    public int countOneBit(int n) {
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
