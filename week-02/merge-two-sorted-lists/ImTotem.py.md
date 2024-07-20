# Intuition

재귀를 사용해 두 정렬된 리스트를 병합한다. 각 단계에서 더 작은 값을 선택하고 진행한다.

# Approach

1. 기저 조건 처리: 빈 리스트 확인
2. 두 리스트의 현재 노드 값 비교
3. 작은 값을 가진 노드 선택 및 다음 노드로 재귀 호출
4. 선택된 노드 반환

# Complexity
- Time complexity: $$O(N + M)$$

- Space complexity: $$O(N + M)$$
$N$, $M$은 각각 두 리스트 길이
# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next,list2)
                return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
```