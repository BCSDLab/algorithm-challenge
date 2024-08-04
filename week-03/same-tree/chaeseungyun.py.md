# Intuition
각 노드를 비교하면서 값이 다르면 false, 모두 통과 시 true

# Approach
1. 노드의 순회는 재귀를 활용
2. 각 노드가 모두 None이면 말단 노드까지 비교 성공
3. 둘 중 하나만 None이면 서로 같지 않음
4. 노드값이 다르면 서로 같지 않음

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
           # 두 노드가 모두 None이면 True
        if not p and not q:
            return True
        # 두 노드 중 하나만 None이면 False
        if not p or not q:
            return False
        # 현재 노드의 값이 다르면 False
        if p.val != q.val:
            return False
        # 좌측 및 우측 자식 노드를 재귀적으로 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

# learn
다른 재귀식을 보니 그냥 한 줄 뚝딱이었다. depth를 어떻게 하위 인자로 주지? 라는 생각만 했는데, return 문에서 애초에 1을 더해주면 쉽게 끝날 일이었다.