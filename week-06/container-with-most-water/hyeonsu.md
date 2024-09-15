# Intuition
투포인터로 양쪽 끝에서 부터 범위를 조정하면서 가장 큰 넓이를 구하면 되는 문제이다.

# Approach
1. 두 개의 포인터가 서로 엇갈리기 전까지 while문 반복
2. 왼쪽 포인터의 높이가 오른쪽 포인터의 높이보다 낮다면 왼쪽 포인터를 오른쪾으로 한칸, 아닌 경우는 오른쪽 포인터를 왼쪽으로 한칸 좁힌다.
3. 이 과정에서 가장 큰 넓이를 구한다.

# Complexity
- Time complexity: $O(N)$
    - 두 개의 포인터를 이용해서 조사하기 노드를 한번씩 조사하기 때문에 → $O(N)$

- Space complexity: $O(1)$
    - 별도의 공간을 사용하지 않기 때문에 → $O(1)$

# Code
```java []
class Solution {
    public int maxArea(int[] height) {
        int width = height.length - 1;
        int low = 0, high = height.length - 1;
        int maxArea = Math.min(height[low], height[high]) * width;
        while(low < high) {
            if (height[low] < height[high]) ++low;
            else --high;
            --width;
            maxArea = Math.max(maxArea, Math.min(height[low], height[high]) * width);
        }
        return maxArea;
    }
}
```

# Learned
개념적으로 잘 잡혀있지 않은 투 포인터를 익힐 수 있어서 좋았습니다. 2개의 포인터를 가지고 index를 관리하는 방법에 익숙해질 수 있었습니다.