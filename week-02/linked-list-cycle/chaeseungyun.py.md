# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
사이클을 찾아야하므로 중복 검사가 생각났다.

# Approach
<!-- Describe your approach to solving the problem. -->
1. 연결 리스트를 차례를 순회한다.
2. 만약 사이클이 있다면 같은 노드를 두 번 지나갈 것이다.
3. 연결 리스트의 끝에 닿았다면 False, 아니면 True

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->


- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
```

# learned
항상 딕셔너리만 쓰다가 set()을 썼는데, key를 정의하지 않아도 돼서 중복 검사할 때 더 편했던 것 같다.