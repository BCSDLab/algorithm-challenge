# Intuition

노드 swap

# Approach

1. 두 개의 포인터를 사용한다: prev (이전 노드)와 curr (현재 노드).
2. prev를 None으로, curr를 head로 초기화한다.
3. 리스트를 순회하면서 `curr.next`, `prev`, `curr` 3개의 노드를 Swap한다.
4. 순회가 끝나면 `prev`가 새로운 헤드가 되므로 이를 반환한다.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
			curr.next, prev, curr = prev, curr, curr.next
        
        return prev
```