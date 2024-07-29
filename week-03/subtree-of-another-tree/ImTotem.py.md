# Intuition

각 노드에서 서브트리 일치 여부를 검사한다.

# Approach

1. subRoot가 None이면 항상 True를 반환한다.
2. 현재 root가 None이고 subRoot가 None이 아니면 False를 반환한다.
3. 현재 root에서 시작하는 서브트리가 subRoot와 같은지 확인한다.
4. 같지 않다면, root의 왼쪽과 오른쪽 자식에 대해 재귀적으로 검사를 수행한다.
5. same 함수는 [same-tree](week-03/same-tree/ImTotem.py)문제와 동일하다.

# Complexity
- Time complexity: $$O(N\times M)$$
	- $N$은 `root` 트리의 노드 수.
	- $M$은 `subRoot` 트리의 노드 수.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.same(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, p, q):
        if p == q == None: return True
        if not (p and q): return False

        return p.val == q.val and \
            self.same(p.left, q.left) and \
            self.same(p.right, q.right)
```