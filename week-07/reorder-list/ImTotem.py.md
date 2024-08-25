# Intuition

리스트를 반으로 나누고, 두 번째 절반을 뒤집은 다음, 두 부분을 교차로 병합한다.

# Approach

1. 리스트의 중간 지점을 찾는다.
2. 리스트의 오른쪽 절반을 뒤집는다.
3. 왼쪽 절반과 뒤집힌 오른쪽 절반을 교차로 병합한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        # Linked List의 가운데 값 찾기
        right = double = head
        while double and double.next:
            right = right.next
            double = double.next.next
        
        # 리스트의 오른쪽 절반을 뒤집는다
        prev, cur = None, right
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        left, right = head, prev
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next
        
```

