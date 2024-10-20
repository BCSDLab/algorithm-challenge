# Intuition
주어진 배열을 정렬 후 n - (n-1)이 1이 아닌 값을 찾아 없는 수를 반환한다.

# Approach
```java
1. 주어진 배열을 정렬한다.
2. prev에 -1을 저장한다.
3. 작은 수부터 for문을 반복한다.
3-1. num - prev가 1이 아니면 num - 1을 반환한다.
3-2. prev에 num을 저장한다. 
4. prev + 1을 반환한다.
```

# Complexity
- Time complexity: O(nlogn)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int prev = -1;
        for (int num : nums) {
            if ((num - prev) != 1) {
                return num - 1;
            }
            prev = num;
        }
        return prev + 1;
    }
}
```
