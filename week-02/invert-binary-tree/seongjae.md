# Intuition
현재 노드에서 왼쪽과 오른쪽 자식을 교환 하는 것들을 반복한다.

# Approach
1. 현재 노드가 null인지 확인한다. 만약 null이라면 null을 반환한다.(기저 조건)
2. 현재 노드의 왼쪽 자식과 오른쪽 자식을 교환한다.
3. 교환된 왼쪽 자식에 대해 재귀적으로 invertTree를 호출한다.
4. 교환된 오른쪽 자식에 대해 재귀적으로 invertTree를 호출한다.
5. 현재 노드를 반환

# Complexity
- Time complexity: O(n)
각 노드를 정확히 한 번씩 방문한다.
- Space complexity: O(h)
재귀 호출 스택의 깊이는 트리의 높이에 비례하므로 공간 복잡도는 트리의 높이에 비례한다.

# Code
Runtime: 0ms Memory Usage: 40.89MB
```java
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
public class InvertBinaryTree226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
```

# Learned
