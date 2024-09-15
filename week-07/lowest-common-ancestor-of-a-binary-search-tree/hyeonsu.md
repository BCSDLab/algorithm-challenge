# Intuition
이진 탐색 트리의 특성을 활용하여, 각 노드의 값을 비교하면서 조상 노드를 찾는다.

# Approach
1. 루트 노드부터 시작해, p와 q의 값과 루트의 값을 비교한다.
2. p와 q가 각각 루트의 양쪽에 있으면, 그 루트가 공통 조상이다.
3. 둘 다 루트보다 작으면 왼쪽 서브트리로, 둘 다 루트보다 크면 오른쪽 서브트리로 이동한다.
4. 재귀적으로 서브트리를 탐색하면서 가장 가까운 공통 조상을 찾는다.

# Complexity
- Time complexity: $O(h)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(h)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if ((p.val <= root.val && q.val >= root.val) ||
            (p.val >= root.val && q.val <= root.val)) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null) return left;
        else return right;
    }
}
```
