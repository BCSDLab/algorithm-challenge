# Intuition
각 노드가 특정 범위 내에 있는지 확인하면서 재귀적으로 트리를 탐색하는 방식으로 해결할 수 있다.

# Approach
1. 각 노드에 대해 해당 값이 특정 범위 안에 있는지 확인한다.
2. 루트 노드부터 시작하여 왼쪽 서브트리는 상한값이 현재 노드 값보다 작아야 하고, 오른쪽 서브트리는 하한값이 현재 노드 값보다 커야 한다.
3. 재귀적으로 왼쪽과 오른쪽 서브트리를 탐색하면서 이 규칙을 적용하여 모든 노드가 조건을 만족하는지 확인한다.

# Complexity
- Time complexity: $O(N)$
    - 트리의 모든 노드를 한 번씩 방문하므로 n은 노드의 수이다.

- Space complexity: $O(N)$
    - 재귀 호출로 인해 호출 스택의 깊이가 트리의 높이만큼 필요하다.

# Code
```java []
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean isValidBST(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return (
            isValidBST(node.left, min, node.val) &&
            isValidBST(node.right, node.val, max)
        );
    }
}

```

# Learned
BST와 재귀함수에 대해서 익숙해질 수 있었다.