# Intuition
재귀함수로 모든 노드를 가보면서 가장 깊은 depth를 찾는다.

# Approach
```java
1. count를 0부터하고 root node부터 재귀한다.
2. node가 null이면 count를 반환한다.
3. node가 null이 아니면 왼쪽 노드와 count+1을 재귀하고, 오른쪽 노드와 count+1을 재귀한다.
4. 두 개의 결과 중 더 큰 값을 반환한다.
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

    public int maxDepth(TreeNode root) {
        return countDepth(root, 0);
    }

    public int countDepth(TreeNode node, int count) {
        if (node == null) {
            return count;
        }
        return Math.max(countDepth(node.left, count+1), countDepth(node.right, count+1));
    }
}
```
