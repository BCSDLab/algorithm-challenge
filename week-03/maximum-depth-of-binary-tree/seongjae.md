# Intuition
이 문제는 이진 트리의 최대 깊이를 구하는 문제임. 
재귀적으로 각 노드의 자식 노드들을 탐색하여 최대 깊이를 계산함.

# Approach
1. 기저 사례로, 현재 노드가 null인 경우 0을 반환.
2. 현재 노드가 리프 노드인 경우 1을 반환.
3. 그렇지 않은 경우, 왼쪽 서브트리와 오른쪽 서브트리의 깊이를 재귀적으로 계산한 후, 두 값 중 큰 값에 1을 더하여 반환.

# Complexity
- Time complexity: O(n)
트리의 모든 노드를 한 번씩 방문하기 때문.

- Space complexity: O(h)
재귀 호출의 깊이 때문에, h는 트리의 높이.

# Code
Runtime: 0ms Memory Usage: 42.6MB
```java
// public class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//     TreeNode() {}
//     TreeNode(int val) { this.val = val; }
//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }
public class MaximumDepthOfBinaryTree104 {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

# Learned
재귀를 사용하여 이진 트리의 최대 깊이를 계산하는 방법을 익혔음.
