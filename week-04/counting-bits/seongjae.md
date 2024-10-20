# Intuition
이를 0부터 n까지 모든 숫자를 이진수로 변환 후 1의 개수를 센다.

# Approach
1. 0부터 n까지의 모든 숫자를 순회함.
2. 각 숫자에 대해 이진수로 변환한 후 1의 개수를 셈.
3. 1의 개수를 결과 배열에 저장함.
4. ㅍ최종적으로 결과 배열을 반환함.

# Complexity
- Time complexity: O(n log n)
각 숫자에 대해 이진수 변환 및 1의 개수를 세는 데 O(log n) 시간이 걸리므로, 
총 n개의 숫자에 대해 수행하면 O(n log n) 시간이 걸림.

- Space complexity: O(n)
결과 배열의 크기가 n + 1이므로 O(n)의 공간이 필요함.

2ms 46.43MB
# Code
```java
public class CountingBits338 {
    public int[] countBits(int n) {
        int[] array = new int[n + 1];
        for(int i = 0; i <= n; i++) {
            int count = 0;
            int num = i;

            while (num != 0) {
                count += num & 1;
                num >>>= 1;
            }

            array[i] = count;
        }
        return array;
    }
}
```

# learn
잊고 있던 비트 연산자를 다시 써볼 수 있었다.
