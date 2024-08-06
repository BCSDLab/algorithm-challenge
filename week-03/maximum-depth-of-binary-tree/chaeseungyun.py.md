# Intuition
트리의 순회는 주로 재귀 호출을 사용했던 것 같다. 라는 생각으로 일단 재귀적으로 접근

# Approach
1. 하위 노드로 갈 수록 depth를 1씩 증가
2. 각 노드에 대해서 왼쪽, 오른쪽 노드를 재귀 호출하고 둘 중 더 큰 값이 트리의 깊이다.

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(N)$$ (worst case for  skewed tree)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(N: size of node.)

# Code
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if root is None: return 0
        return max(self.getDepth(root.left, depth), self.getDepth(root.right, depth))
    
    def getDepth(self, node, depth):
        if node is None: return depth
        return max(self.getDepth(node.left, depth + 1), self.getDepth(node.right, depth + 1))
```

# learn
다른 재귀식을 보니 그냥 한 줄 뚝딱이었다. depth를 어떻게 하위 인자로 주지? 라는 생각만 했는데, return 문에서 애초에 1을 더해주면 쉽게 끝날 일이었다.