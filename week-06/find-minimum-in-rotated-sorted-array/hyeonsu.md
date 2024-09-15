# Intuition
이분탐색으로 풀면 되는 문제이다.

# Approach
1. low가 high보다 작을때 동안 while문을 반복한다.
2. 중간값이 오른쪽 끝값보다 작으면 가장 작은값은 왼쪽에 있다. 아닌경우는 반대

# Complexity
- Time complexity: $O(logN)$
    - 이분탐색이기 때문에 $O(logN)$

- Space complexity: $O(1)$
    - 별도의 추가공간을 사용하지 않기 때문에 $O(1)$

# Code
```java []
class Solution {
    public int findMin(int[] nums) {
        int l = 0, h = nums.length - 1;
        while(l < h) {
            int m = (h - l) / 2 + l;
            if (nums[m] < nums[h]) h = m;
            else l = m + 1;
        }
        return nums[l];
    }
}
```

# Learned
이분탐색 문제와 투 포인터 문제의 매커니즘이 비슷한 것 같다. 정렬된 문제를 봤을 때 잘 떠올릴 수 있을 것 같다.