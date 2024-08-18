# Intuition
특정 인덱스에서의 왼쪽, 오른쪽으로 곱을 계산하여 두 배열에 저장한 후 두 요소를 곱한다.

# Approach
1. 왼쪽, 오른쪽으로 구분하여 곱한 것을 저장할 두 배열을 생성한다.
2. 왼쪽에서 오른쪽으로 순회하면서 왼쪽부분의 곱을 기록할 배열에 저장한다.
3. 오른쪽에서 왼쪽으로 순회하면서 오른쪽부분의 곱을 기록할 배열에 저장한다.
4. left, right배열을 순회하며 서로 곱한 값을 저장하여 반환한다.

# Complexity
- Time complexity: $O(N)$
    - 왼쪽에서 오른쪽으로 곱한 값을 저장하는 시간: $O(N)$
    - 오른쪽에서 왼쪽으로 곱한 값을 저장하는 시간: $O(N)$
    - left, right배열을 순회하며 서로 곱한 값을 저장하는 시간: $O(N)$

- Space complexity: $O(N)$
    - 왼쪽, 오른쪽, 반환배열의 공간: $O(3N)$

# Code
```
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        left[0] = right[nums.length - 1] = 1;
        for (int i = 1; i < nums.length; ++i) left[i] = left[i - 1] * nums[i - 1];
        for (int i = nums.length - 2; i >= 0; --i) right[i] = right[i + 1] * nums[i + 1];
        int[] ret = new int[nums.length];
        for (int i = 0; i < ret.length; ++i) ret[i] = left[i] * right[i];
        return ret;
    }
}
```

# Learned
분할정복으로 문제를 해결하면 시간복잡도를 개선할 수 있는 문제인지 파악하는 것을 배웠습니다.