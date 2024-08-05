# Intuition
모든 노드를 root노드로 하여 subtree와 같은지 확인한다.

# Approach
1. 모든 노드를 순회하며 그 노드가 subtree인지 확인한다.
2. 각각의 노드를 순회할 때 마다 isSametree를 호출해서 같은 트리인지 확인한다.

# Complexity
- Time complexity: $O(nm)$
    - 모든 노드를 방문하고, 각각의 노드에서 subtree와 같은지 확인한다.
    - root트리의 노드의 개수 n, subRoot의 노드의 수 m → $O(nm)$

- Space complexity: $O(h1 + h2)$
    - 공간복잡도는 스택의 깊이만큼이다.
    - 스택의 최대 깊이는 root노드의 깊이인 h1 + subRoot의 깊이인 h2 → $O(h1 + h2)$

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
    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;
        if (isSametree(root, subRoot)) return true;
        return (
            isSubtree(root.left, subRoot) ||
            isSubtree(root.right, subRoot)
        );
    }

    private boolean isSametree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null && root == null) return true;
        if (subRoot == null || root == null) return false;
        if (root.val != subRoot.val) return false;
        return (
            isSametree(root.left, subRoot.left) &&
            isSametree(root.right, subRoot.right)
        );
    }
    
}
```

## Learned
트리를 재귀함수로 순회하는 훈련이 됐다.