# Intuition
q와 p의 모든 노드를 동시에 보면서 값을 비교한다.

# Approach
```java
1. p와 q 둘 중에 한 개만 null일 경우 false를 반환한다.
2. p와 q 모두 null일 경우 true를 반환한다.
3. p와 q의 val이 다를 경우 false를 반환한다.
4. p와 q의 left node, right node 각각을 재귀하여 둘 다 반환값이 true이면 true를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)


# Code
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
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ((p == null && q != null) || (p != null && q == null)) {
            return false;
        }
        if (p == null && q == null) {
            return true;
        }

        if (p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```
