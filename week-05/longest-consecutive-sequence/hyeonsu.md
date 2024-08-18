# Intuition
Set을 이용해서 중복된 숫자를 제거한 뒤, Set의 요소들을 하나씩 살펴보면서 수열이 있는지 확인한다.

# Approach
1. Set에 입력배열의 요소를 전부 넣는다.
2. Set의 내용으로 순회하면서 수열인지 확인하고, 제일 긴 수열을 기록한다.

# Complexity
- Time complexity: $O(N)$
    - Set에 nums의 요소를 넣는 비용: $O(N)$
    - Set을 순회하는 비용: $O(N)$

- Space complexity: $O(N)$
    - 별도의 Set에 입력배열의 값을 모두 넣기 때문에: $O(N)$

# Code
```
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet(nums.length);
        for (int num: nums) set.add(num);
        int maxCount = 0;
        for (int num: set) {
            if (set.contains(num - 1)) continue;
            int count = 1;
            while(set.contains(num + 1)) {
                ++num;
                ++count;
            }
            maxCount = Math.max(maxCount, count);
        }
        return maxCount;
    }
}
```

# Learned
전수조사 하면 되는 문제였다. Set자료구조를 응용해서 사용하는 것을 배웠다.