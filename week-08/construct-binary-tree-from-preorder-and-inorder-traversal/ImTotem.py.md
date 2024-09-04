# Intuition

모르곘어서 풀이를 봤다. 트리 탐색 어렵다...

# Approach

1. 중위 순회 배열의 값과 인덱스를 매핑하는 딕셔너리를 생성한다. 이를 통해 루트 노드의 위치를 빠르게 찾을 수 있다.
2. 전위 순회 배열을 deque로 변환하여 효율적으로 왼쪽 pop 연산을 수행할 수 있도록 한다.
3. 재귀 함수 build를 정의하여 트리를 구성한다:
	- 현재 범위의 시작과 끝 인덱스를 매개변수로 받는다.
	- 전위 순회 배열에서 첫 번째 요소를 pop하여 현재 노드로 사용한다.
	- 중위 순회에서 현재 노드의 위치를 찾아 왼쪽과 오른쪽 서브트리의 범위를 결정한다.
	- 재귀적으로 왼쪽과 오른쪽 서브트리를 구성한다.
4. 구성된 루트 노드를 반환한다.

# Complexity
- Time complexity: $$O(N)$$
	- n은 노드의 수. 각 노드를 한 번씩 방문하므로 $O(N)$.

- Space complexity: $$O(N)$$
	- 중위 순회 배열의 값과 인덱스를 매핑하는 딕셔너리에 $O(N)$ 공간이 필요.
	- 재귀 호출 스택의 최대 깊이는 트리의 높이와 같으며, 최악의 경우 $O(N)$이 될 수 있음.

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {inorder[i]:i for i in range(len(inorder))}
        
        preorder = collections.deque(preorder)

        def build(start, end):
            if start > end: return None

            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root
        
        return build(0, len(preorder) - 1)
```

