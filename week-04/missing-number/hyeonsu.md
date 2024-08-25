# Intuition
0~N까지 숫자의 합에서 nums배열의 숫자를 모두 빼면 나머지 하나의 숫자가 나온다.

# Approach
1. `(N * (N + 1)) / 2)`로 전체 숫자를 구한다.
2. `nums`배열을 순회하면서 배열의 요소들을 빼준다.
3. 남은 숫자가 나머지 하나의 숫자이다.

# Complexity
- Time complexity: $O(N)$
    - 입력배열 nums의 크기 N이라고 가정 → $O(N)$

- Space complexity: $O(1)$
    - 추가 공간을 사용하지 않기 때문에 $O(1)$

# Code
```
class Solution {
    public int missingNumber(int[] nums) {
        int N = nums.length;
        int sum = (N * (N + 1)) / 2;
        for (int num: nums) sum -= num;
        return sum;
    }
}
```