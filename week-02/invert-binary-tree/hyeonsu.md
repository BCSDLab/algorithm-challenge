# Intuition
재귀적으로 트리를 순회하면서 트리의 `left`와 `right`를 교체한다.

# Approach
1. 트리를 재귀로 순회해야 하기 때문에 재귀로 사용할 함수를 하나 만든다.
2. 재귀의 종료조건은 입력 노드가 `null`일 경우
3. 입력 노드의 `left`와 `right`를 교체한 후 각각에 대해 재귀호출을 한다.

# Complexity
- Time complexity: $O(N)$
    - 모든 노드를 한번씩 방문해서 좌우를 반전시킴 → $O(N)$

- Space complexity: $O(logN)$
    - 재귀호출트리의 공간 $O(logN)$

# Code
``` java
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
    
    public TreeNode invertTree(TreeNode root) {
        invertSubTree(root);
        return root;
    }

    private void invertSubTree(TreeNode root) {
        if (root == null) return;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
    }
}
```

# Learned
재귀적으로 해결하면 쉽게 해결할 수 있는 문제였다.