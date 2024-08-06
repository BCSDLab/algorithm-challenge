# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
트리의 순회하면 재귀가 먼저 떠올랐다.

# Approach
<!-- Describe your approach to solving the problem. -->
1. 재귀 호출 방식을 사용
2. 루트부터 차례대로 왼쪽 자식과 오른쪽 자식을 바꿈
3. 종료조건 - 현재 노드가 None

# Complexity
- Time complexity: $$O(log(n))$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = root
        if root is None:
             return root

        tmp = root.left

        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return result
```

# learn
a ,b = b, a 방식으로 스왑하면 더 간결한 코드가 됐을 것이다.