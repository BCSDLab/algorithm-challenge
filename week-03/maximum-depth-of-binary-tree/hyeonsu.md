# Intuition
재귀적으로 왼쪽 노드와 오른쪽 노드의 depth중 큰 것을 반환한다.

# Approach
1. 재귀의 종료조건은 root = null인 경우이다.
2. 왼쪽 트리와 오른쪽 트리중 depth가 큰 것을 반환하면 된다.

# Complexity
- Time complexity: $O(n)$
    - 최악의 경우 모든 노드를 방문해야하기 때문에 입력노드의 개수 $O(n)$

- Space complexity: $O(h)$
    - 재귀호출트리의 깊이만큼 스택이 호출되기 때문에 $O(h)$


# Code
```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public int maxDepth(TreeNode root) {
        int maxDepth = maxDepth(root, 0);
        return maxDepth;
    }

    private int maxDepth(TreeNode root, int depth) {
        if (root == null) return depth;
        int left = maxDepth(root.left, depth + 1);
        int right = maxDepth(root.right, depth + 1);
        return Math.max(left, right);
    }
}
```

# Learned
재귀함수를 구현할 때 root, left, right만 고려하면 조금 더 해결하기 쉽다.