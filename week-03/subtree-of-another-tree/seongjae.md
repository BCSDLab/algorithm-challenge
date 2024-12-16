# Intuition
주어진 트리의 각 노드에서 시작해 두 트리가 동일한지 확인

# Approach
1. 트리의 루트 노드부터 시작해, 각 노드를 순회하면서 부분 트리인지 확인.
2. 현재 노드가 부분 트리의 루트 노드와 동일한지 확인.
3. 동일하면, 두 트리가 동일한지 재귀적으로 확인.
4. 동일하지 않으면, 왼쪽 및 오른쪽 자식 노드에서 다시 부분 트리인지 확인.

# Complexity
- Time complexity: O(n * m)
n은 주어진 트리의 노드 수, m은 부분 트리의 노드 수. 최악의 경우 모든 노드에서 부분 트리 확인.

- Space complexity: O(h)
재귀 호출의 깊이 때문에, h는 주어진 트리의 높이.


# Code
Runtime: 2ms Memory Usage: 44.5MB
```java
// public class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//     TreeNode() {}
//     TreeNode(int val) { this.val = val; }
//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }
public class SubtreeOfAnotherTree572 {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;
        if (root.val == subRoot.val) return isContainTree(root, subRoot);
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isContainTree(TreeNode p, TreeNode q) {
        if(p == null || q == null);
        if (p.val != q.val) return false;
        return isContainTree(p.left, q.left) && isContainTree(p.right, q.right);
    }
}
```

# Learned
두 트리 중 하나가 다른 트리의 부분 트리인지 확인하는 방법을 배웠음.
각 노드를 순회하면서 부분 트리의 루트 노드와 동일한지 확인하고, 동일하면 두 트리가 동일한지 재귀적으로 확인하는 것이 중요함.
