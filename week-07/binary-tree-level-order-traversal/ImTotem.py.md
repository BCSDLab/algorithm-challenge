# Intuition

각 레벨의 노드들을 순서대로 방문하면서 그 값들을 리스트로 모은다. BFS를 이용한다.

# Approach

1. 결과를 저장할 리스트 ans를 초기화한다.
2. 루트가 없으면 빈 리스트를 반환한다.
3. 큐(deque)를 사용하여 BFS를 구현한다.
4. 각 레벨마다:
	- 현재 레벨의 노드 값들을 저장할 새 리스트를 ans에 추가한다.
	- 큐의 현재 크기만큼 반복하여 현재 레벨의 모든 노드를 처리한다.
	- 각 노드에 대해:
		- 노드 값을 현재 레벨의 리스트에 추가한다.
		- 왼쪽 자식이 있으면 큐에 추가한다.
		- 오른쪽 자식이 있으면 큐에 추가한다.
5. 모든 레벨을 처리한 후 ans를 반환한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(N)$$

# Code
```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        q = deque([root])

        while q:
            ans.append([])
            for _ in range(len(q)):
                node = q.popleft()

                ans[-1].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans

```

