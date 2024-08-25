# Intuition
DP로 접근해서 문제를 해결할 수 있을 것 같다.
    - 현재 숫자가 홀수라면: 바로 이전 숫자에 1을 추가한 수 이다.
    - 현재 숫자가 짝수라면: 이전 숫자 중 가장 큰 1이 1개인 수를 뺀 나머지 수의 1의 개수 + 1이다.

# Approach
1. DP의 초기 배열을 설정해준다.
2. 이전 숫자중 1이 1개인 가장 큰 숫자를 저장할 변수 pow를 선언한다.
3. count개수만큼 for문을 순회한다.
    - 이때 짝수면 counts[i] = counts[i - 1] + 1;
    - 홀수면 counts[i] = counts[prevPow] + counts[i - prevPow];

# Complexity
- Time complexity: $O(N)$
    - 입력 정수 n의 범위를 N이라고 할 때 N만큼 순회 → $O(N)$


- Space complexity: $O(N)$
    - 입력 정수 n의 범위를 N이라고 할 때 N만큼 DP배열 생성 → $O(N)$

# Code
```
class Solution {
    
    public int[] countBits(int n) {
        if (n == 0) return new int[] {0};
        int[] counts = new int[n + 1];
        counts[0] = 0;
        counts[1] = 1;
        int pow = 2;
        int prevPow = pow;
        for (int i = 2; i < counts.length; ++i) {
            if (i == pow) {
                counts[i] = 1;
                prevPow = pow;
                pow *= 2;
            } else if (i % 2 == 1) counts[i] = counts[i - 1] + 1;
            else counts[i] = counts[prevPow] + counts[i - prevPow];
        }
        return counts;
    }
}
```

# Learned
DP로 접근하는 방식에 대해 익숙해질 수 있었다.