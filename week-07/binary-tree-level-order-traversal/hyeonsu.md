# Intuition
각 레벨별로 노드의 값을 수집하여 리스트로 반환한다.

# Approach
재귀적으로 깊이 우선 탐색(DFS)을 하면서, 각 노드의 깊이를 기준으로 리스트를 채운다.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```java []
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

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> orderList = new ArrayList<>();
        levelOrder(root, 0, orderList);
        return orderList;
    }

    public void levelOrder(TreeNode root, int depth, List<List<Integer>> list) {
        if (root == null) return;
        if (list.size() <= depth) list.add(new ArrayList<>());
        list.get(depth).add(root.val);
        levelOrder(root.left, depth + 1, list);
        levelOrder(root.right, depth + 1, list);
    }
}
```

# Learned
재귀적으로 트리를 방문하는 방식에 대해 익숙해질 수 있었습니다.