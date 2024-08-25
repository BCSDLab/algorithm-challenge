# Intuition

reorder-list 문제의 Linked List의 가운데 값 찾는 부분과 동일하다.

# Approach

1. 더미 노드(ans)를 생성하여 리스트의 시작점으로 사용한다.
2. 두 개의 포인터(gap과 prev)를 사용한다:
	- gap: 리스트의 끝을 향해 n+1만큼 먼저 이동한다.
	- prev: 제거할 노드의 이전 노드를 가리키게 될 포인터
1. gap이 리스트의 끝에 도달할 때까지 gap과 prev를 동시에 이동시킨다.
2. prev의 다음 노드(제거할 노드)를 건너뛰어 연결한다.
3. 더미 노드의 다음 노드(실제 헤드)를 반환한다.

# Complexity
- Time complexity: $$O(L)$$
	- $L$은 연결 리스트의 길이

- Space complexity: $$O(1)$$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(next=head)

        gap = prev = ans
        for _ in range(n+1):
            gap = gap.next
        
        while gap:
            gap = gap.next
            prev = prev.next

        prev.next = prev.next.next

        return ans.next

```

