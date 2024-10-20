# Intuition
비트를 하나씩 확인한다.

# Approach
1. 주어진 정수가 0인 경우 0을 반환함.
2. 반복문을 사용하여 정수가 0이 될 때까지 각 비트를 확인함.
3. 각 반복에서 가장 높은 2의 거듭제곱 값을 찾아서 해당 값을 정수에서 빼고 1의 개수를 증가시킴.
4. 반복문이 종료되면 1의 개수를 반환함.

# Complexity
- Time complexity: O(log n)
각 반복에서 n을 반으로 줄이는 연산을 수행하므로 O(log n)

- Space complexity: O(1)
추가적인 공간을 거의 사용하지 않으므로 O(1)

1ms 40.45MB
# Code
```java
public class NumberOf1Bits191 {
    public int hammingWeight(int n) {
        if (n == 0) return 0;

        int count = 0;
        while (n > 0) {
            int highestPowerOfTwo = 1;
            while (highestPowerOfTwo <= n / 2) {
                highestPowerOfTwo *= 2;
            }
            n -= highestPowerOfTwo;
            count++;
        }

        return count;
    }
}
```

# learn
