# Intuition
root node를 재귀하면서 subRoot node의 val과 값이 같으면 동일한 tree인지 확인한다.

# Approach
```java
1. root나 subRoot가 null이면 false를 반환한다.
2. root와 subRoot가 null이면 true를 반환한다.
3. root의 val과 subRoot의 val이 같으면 해당 노드부터 같은 트리인지 확인한다.
4. val이 다르면 왼쪽 노드와 subRoot 또는 오른쪽 노드와 subRoot를 비교해 true가 있으면 true를 반환한다.
```

# Complexity
- Time complexity: O(n^2)

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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if ((root != null && subRoot == null) || (root == null && subRoot != null)) {
            return false;
        }
        if (root == null && subRoot == null) {
            return true;
        }

        if (root.val == subRoot.val) {
            if(checkSame(root, subRoot)) {
                return true;
            }
        }
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean checkSame(TreeNode root, TreeNode subRoot) {
        if ((root != null && subRoot == null) || (root == null && subRoot != null)) {
            return false;
        }
        if (root == null && subRoot == null) {
            return true;
        }

        if (root.val != subRoot.val) {
            return false;
        }

        return checkSame(root.left, subRoot.left) && checkSame(root.right, subRoot.right);
    }
}
```
