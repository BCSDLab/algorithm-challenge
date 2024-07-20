# Intuition

재귀로 각 노드의 왼쪽과 오른쪽 자식을 교환한다.

# Approach

1. 루트가 None이면 즉시 반환한다 (기저 조건).
2. 현재 노드의 왼쪽과 오른쪽 자식을 교환한다.
3. 왼쪽 서브트리에 대해 invertTree를 호출한다.
4. 오른쪽 서브트리에 대해 invertTree를 호출한다.
5. 뒤집힌 트리의 루트를 반환한다.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```