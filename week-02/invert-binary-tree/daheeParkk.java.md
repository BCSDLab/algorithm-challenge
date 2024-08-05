# Intuition
root 노드부터 왼쪽과 아래쪽을 바꾸면서 내려간다.

# Approach
```java
1. root를 재귀함수에 전달한다.
2. curr 노드가 null이면 return한다.
3. curr 노드의 왼쪽, 오른쪽 노드를 바꾼다.
4. curr 노드의 왼쪽, 오른쪽 노드를 각각 재귀함수에 넣는다.
5. 재귀함수가 끝나고 root를 반환한다.
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
    public TreeNode invertTree(TreeNode root) {
        invert(root);
        return root;
    }

    public void invert(TreeNode curr) {
        if (curr == null) {
            return;
        }
        
        TreeNode prevLeft = curr.left;
        TreeNode prevRight = curr.right;

        curr.left = prevRight;
        curr.right = prevLeft;
        invert(curr.left);
        invert(curr.right);
    }
}
```
