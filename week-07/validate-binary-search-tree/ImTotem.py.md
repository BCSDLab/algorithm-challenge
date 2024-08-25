# Intuition

중위 순회(inorder traversal)를 했을 때 노드의 값들이 오름차순으로 정렬되어야 한다.

# Approach

1. 반복적 중위 순회(iterative inorder traversal)를 사용하여 트리를 순회한다.
2. 순회하면서 각 노드의 값을 이전에 방문한 노드의 값과 비교한다.
3. 현재 노드의 값이 이전 노드의 값보다 작거나 같으면 유효하지 않은 BST이다.
4. 스택을 사용하여 노드들을 저장하고 처리한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(N)$$

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= prev:
                return False
            
            prev = root.val
            root = root.right

        return True

```

