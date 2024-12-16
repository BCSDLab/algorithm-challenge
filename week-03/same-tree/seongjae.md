# Intuition
이 문제는 두 이진 트리가 같은지 확인하는 문제임. 
이를 위해 각 노드를 재귀적으로 비교하면 됨.

# Approach
1. 두 트리의 루트 노드부터 비교를 시작함.
2. 두 노드가 모두 null이면 true를 반환.
3. 한 노드만 null이면 false를 반환.
4. 두 노드의 값이 다르면 false를 반환.
5. 두 노드의 값이 같으면, 왼쪽 자식 노드와 오른쪽 자식 노드를 각각 재귀적으로 비교.

# Complexity
- Time complexity: O(n)
트리의 모든 노드를 한 번씩 방문하기 때문.

- Space complexity: O(h)
재귀 호출의 깊이 때문에, h는 트리의 높이.


# Code
Runtime: 0ms Memory Usage: 40.7MB
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
public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

# Learned
두 이진 트리가 동일한지 확인하기 위해 재귀적으로 각 노드를 비교하는 방법을 익혔음.
