# Intuition
전수조사를 해서 Two Sum을 찾는다.

# Approach
1. 2중 반복으로 Two Sum을 찾는다.
    - 외부 반복은 nums.length - 1만큼 반복한다.
    - 내부 반복은 외부 반복의 index + 1만큼 반복 한다.
2. 내부 반복 중 Two Sum이 있으면 반환한다.

# Complexity
- Time complexity: `O((n * n) / 2)`
    - 외부 반복 n, 내부 반복 n / 2
- Space complexity: `O(n)`
    - 입력 배열 `O(n)`

# Code
Runtime: 45 ms
Memory Usage: 44.4 MB
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}
```

# Learned
테스트 케이스에 따라서 실행 속도가 차이 날 수 있다는 것을 알았다.