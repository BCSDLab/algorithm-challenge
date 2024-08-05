# Intuition

각 노드의 값을 재귀적으로 비교한다.

# Approach

1. 두 노드가 모두 None이면 True를 반환한다.
2. 두 노드 중 하나만 None이면 False를 반환한다.
3. 현재 노드의 값을 비교한다.
4. 왼쪽 서브트리를 재귀적으로 비교한다.
5. 오른쪽 서브트리를 재귀적으로 비교한다.
6. 모든 비교 결과를 and연산하여 반환한다.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None: return True
        if not (p and q): return False

        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
```