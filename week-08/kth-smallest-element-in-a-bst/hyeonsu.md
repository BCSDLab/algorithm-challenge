# Intuition
이진 탐색 트리의 성질을 이용하면 중위 순회(inorder traversal)를 통해 노드를 오름차순으로 방문하여 해결할 수 있다.

# Approach
1. 중위 순회 방식을 사용하여 트리를 순회하면서 노드의 값을 리스트에 저장한다.
2. 중위 순회는 왼쪽 서브트리, 루트, 오른쪽 서브트리 순으로 노드를 방문하므로, 리스트에 저장된 값은 오름차순으로 정렬된다.
3. 리스트의 k번째 원소를 반환한다. (리스트는 0부터 시작하므로 k-1 번째 값을 반환)

# Complexity
- Time complexity: $O(N)$
    - 트리의 모든 노드를 한 번씩 방문해야 한다.

- Space complexity: $O(N)$
    - 리스트에 트리의 모든 노드를 저장한다.

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
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> list = new ArrayList();
        preOrder(root, list);
        System.out.println(list);
        return list.get(k - 1);
    }
    
    public void preOrder(TreeNode root, List<Integer> list) {
        if (root == null) return;
        preOrder(root.left, list);
        list.add(root.val);
        preOrder(root.right, list);
        
    }
}
```

# Learned
이진 탐색 트리에서 중위 순회를 사용하여 노드 값을 오름차순으로 정렬하는 것을 배웠다.