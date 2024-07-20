# Intuition

노드를 방문할 때마다 값을 변경하여 사이클을 감지한다.

# Approach

1. 빈 리스트 확인: 헤드가 `None`이면 사이클이 없다.
2. 현재 노드의 값의 타입이 `bool`인지 확인: 사이클 존재 여부 판단.
3. 현재 노드의 값을 `False`로 변경: 방문 표시.
4. 다음 노드로 재귀 호출.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if isinstance(head.val, bool):
            return True
            
        head.val = False
        return self.hasCycle(head.next)
```