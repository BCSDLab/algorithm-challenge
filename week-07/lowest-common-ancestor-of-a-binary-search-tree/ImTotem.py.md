# Intuition

왼쪽 서브트리의 모든 노드 값이 현재 노드보다 작고, 오른쪽 서브트리의 모든 노드 값이 현재 노드보다 크다는 특성을 이용한다.

# Approach

1. 루트 노드에서 시작한다.
2. 현재 노드의 값과 p, q의 값을 비교한다:
	- p와 q의 값이 모두 현재 노드보다 크면, 오른쪽 자식으로 이동한다.
	- p와 q의 값이 모두 현재 노드보다 작으면, 왼쪽 자식으로 이동한다.
	- 그 외의 경우(p와 q가 현재 노드를 기준으로 서로 다른 방향에 있거나, 둘 중 하나가 현재 노드와 같은 경우), 현재 노드가 LCA이다.
1. LCA를 찾을 때까지 2번 과정을 반복한다.

# Complexity
- Time complexity:
	- 평균: $O(\log{(n)})$
	- 최악: $O(N)$

- Space complexity: $$O(1)$$

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:

            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node
```

