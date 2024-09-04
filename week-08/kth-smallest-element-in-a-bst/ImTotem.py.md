# Intuition

BST의 중위 순회(inorder traversal)는 원소를 오름차순으로 방문하는 특성을 이용한다.

# Approach

1. 스택을 사용하여 반복적 중위 순회를 구현한다.
2. 루트에서 시작하여 왼쪽 자식 노드들을 모두 스택에 넣는다.
3. 스택에서 노드를 꺼내 처리한다 (이는 현재 가장 작은 미방문 노드).
4. k를 1 감소시키고, k가 0이 되면 현재 노드의 값을 반환한다.
5. 오른쪽 자식 노드로 이동하여 과정을 반복한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(H)$$
	- H는 트리의 높이

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

```

