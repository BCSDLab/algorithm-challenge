# Intuition
첫 번째 시도에서는 가능한 모든 조합의 수를 계산하려고 했음. 
n개의 계단을 오를 때 1칸씩 오르는 방법과 2칸씩 오르는 방법을 섞어서 몇 가지 경우가 나오는지 세는 방식.

# Approach
1. 계단을 2칸씩 오를 수 있는 최대 횟수를 구함.
2. 2칸씩 오르는 횟수를 0부터 최대 횟수까지 증가시키면서, 남은 계단을 1칸씩 오르는 경우를 계산.
3. 각 경우의 수를 조합 계산(combination)을 통해 구함.

# Complexity
- Time complexity: O(n^2) 
조합 계산을 위해 팩토리얼 계산이 포함됨

- Space complexity: O(1) 
추가 메모리 사용 없음

# Code
스택 오버플로우
```java
public class ClimbingStairs70 {
    public int climbStairs(int n) {
        int cases = 0;
        int maxTwos = n / 2;
        for (int i = 0; i <= maxTwos; i++) {
            int countOnes = n - 2 * i;
            cases += combination(countOnes + i, i);
        }
        return cases;
    }

    private int combination(int n, int k) {
        return factorial(n) / (factorial(k) * factorial(n - k));
    }

    private int factorial(int n) {
        if (n == 0 || n == 1)
            return 1;
        else
            return factorial(n-1) * n;
    }
}
```

# Learned
팩토리얼 계산을 재귀로 하면 큰 숫자에서 스택 오버플로우 발생 가능해서
비효율적일 수 있다는 것을 배웠음


# Intuition
두 번째 시도에서는 반복문을 사용하여 가능한 모든 조합을 계산함. 
더 효율적이고 안정적인 방법을 사용함.

# Approach
1. 2칸씩 오를 수 있는 최대 횟수를 구함.
2. 각 경우에 대해 조합(combination)을 반복문으로 계산.
3. 조합 계산 시 k와 n-k 중 작은 값을 선택하여 계산을 최적화함.

# Complexity
- Time complexity: O(n) 
조합 계산이 더 효율적임

- Space complexity: O(1) 
추가 메모리 사용 없음


# Code
Runtime: 0ms Memory Usage: 40.1MB
```java
public class ClimbingStairs70 {
    public int climbStairs(int n) {
        int maxTwos = n / 2;
        long cases = 0;
        for (int i = 0; i <= maxTwos; i++) {
            int countOnes = n - 2 * i;
            cases += combination(countOnes + i, i);
        }
        return (int)cases;
    }

    private long combination(int n, int k) {
        if (k == 0 || k == n) {
            return 1;
        }
        if (k > n - k) {
            k = n - k; // nCk = nC(n-k)
        }
        long result = 1;
        for (int i = 0; i < k; i++) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }
}
```

# Learned
반복문을 사용하여 조합을 계산하면 재귀보다 효율적이고 안정적일 수 있음.
