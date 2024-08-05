# Intuition

루트 노드에서 가장 먼 리프 노드까지의 거리를 반환한다.

# Approach

1. 루트가 None일 경우 깊이는 0이다.
2. 현재 노드의 깊이는 1(자기 자신) + 왼쪽과 오른쪽 서브트리 중 더 깊은 쪽의 깊이이다.
3. 재귀적으로 왼쪽과 오른쪽 서브트리의 깊이를 계산한다.
4. 두 서브트리의 깊이 중 큰 값에 1을 더해 반환한다.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```