# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
두 연결 리스트는 정렬되어 있으므로 반복문을 통해 비교가 쉬워보였다.

# Approach
<!-- Describe your approach to solving the problem. -->
1. 각 노드의 val를 비교하며 작은 값을 더미 노드에 추가한다.
2. 반복문이 끝나도 남아 있는 연결 리스트가 있다면 끝에 이어 붙인다. (무조건 더 크다.)

# Complexity
- Time complexity: $$O(N+M)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(N+M)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

N과 M은 각각 연결 리스트의 길이
# Code
```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode() # 더미 노드
        cur = merge # 현재 노드 포인터

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
            
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return merge.next # 시작 노드 반환
```

# learn
더미 노드를 만들고 노드 포인터를 왜 만드는지에 궁금증이 있었는데, 시작 노드 위치를 잃어버리기 때문이란 것을 알았다.
