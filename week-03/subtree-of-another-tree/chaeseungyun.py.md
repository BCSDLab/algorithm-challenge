# Intuition
same tree와 마찬가지로 재귀로 접근한다.

# Approach
1. 모든 노드를 순회하면서 각 노드가 같은지 판단한다.
2. 각 노드에 대해 재귀적으로 접근해서 모든 노드가 같은 지 판단한다.

# Complexity
- Time complexity: $$O(n * m)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity
    - $$O(N + M)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(p, q):
            if not p or not q:
                return not p and not q
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

# learn
재귀적으로 접근해야한다는 것은 알았는데 각 노드를 비교하면서 어떻게 재귀적으로 접근할 수 있을까? 라는 생각이 들어 막연해졌다.
결국 풀이를 보고 문제를 풀었다. 종료 조건을 확실히 잡으면 재귀가 더 쉬워지는 것 같다.