# Intuition
이분탐색을 이용해서 풀 수 있다.

# Approach
1. l <= h일 동안 while문 반복
2. nums[m] == target이면 m 반환
3. 분할의 한쪽이 정렬되어있는지 확인하는 방법은 해당 분할의 가장 왼쪽, 가장 오른쪽 값을 비교해보는 것.
4. 정렬되어 있는 분할이라면 그 분할에 target이 들어가는지 확인하고 들어간다면 h를 m - 1로 업데이트, 아니라면 l을 m + 1로 업데이트
5. while문에서 같은 값을 찾지 못했다면 -1반환

# Complexity
- Time complexity: $O(logN)$
    - 이분탐색이기 때문에 → $O(logN)$

- Space complexity: $O(1)$
    - 입력에 따른 별도의 추가공간을 사용하지 않기 때문에 → $O(1)$

# Code
```java []
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1 && nums[0] == target) return 0;
        int l = 0, h = nums.length - 1;
        while(l <= h) {
            int m = (h - l) / 2 + l;
            if (nums[m] == target) return m;
            if (nums[l] <= nums[m]) {
                if (nums[l] <= target && nums[m] > target) h = m - 1;  
                else l = m + 1;
            } else {
                if (nums[m] < target && nums[h] >= target) l = m + 1;  
                else h = m - 1;
            }
        }
        return -1;
    }
}
```

# Learned
이번 문제는 지금까지 이분탐색을 트레이닝 한 덕분인지 뭔가 잘 풀렸던 것 같다.(연습의 성과!?)