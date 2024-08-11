# Intuition
주어진 10진수를 2진수 문자열로 변환한 다음 1의 개수를 샌다.

# Approach
1. 입력 n을 2진수 문자열로 변환한다.
2. for-each문을 이용해서 1의 개수를 샌다.

# Complexity
- Time complexity: $O(1)$
    - 정수 n을 2진수 문자열로 변환하는 비용: $O(1)$
    - 2진수 문자열에서 1의 개수를 새는 비용: $O(1)$

- Space complexity: $O(1)$

# Code
```
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        for (char binary: Integer.toBinaryString(n).toCharArray()) {
            if (binary == '1') ++count;
        }
        return count;
    }
}
```

# Learned
쉽게 풀 수 있는 문제였던 것 같다.