# Intuition
두 개의 입력 `LinkedList`의 `head`중 작은 것을 새로운 `LinkedList`에 붙이는것을 두 입력 `LinkedList`의 `head`를 업데이트하며 반복한다.

# Approach
1. 새로운 노드 하나를 만든다.
2. 새로 만든 노드의 뒤에 입력 노드중 작은 값인 도드를 붙이고 `head`를 `head.next`로 업데이트한다.
3. 위의 과정을 재귀를 통해 반복한다. 이때 재귀의 종료조건은 다음과 같다.
    - 두 노드가 `null`인 경우: 두 입력 `LinkedList`의 노드를 전부 옮겼다는 뜻
    - 둘 중 하나의 노드만 `null`인 경우: 하나의 `LinkedList`는 전부 옮겼기 때문에 다른 하나는 통째로 새로운 `Node`의 뒤에 붙이면 됨.

# Complexity
- Time complexity: $O(N + M)$
    - 입력 `LinkedList`두 개를 전부 순회해야 하기 때문에 $N + M$ → $O(N + M)$

- Space complexity: $O(1)$
    - 새로운 노드를 하나 만들어서 그 뒤에 기존의 노드를 붙인다 → $O(1)$

# Code
``` java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(-1, null);
        merge(head, list1, list2);
        return head.next;
    }

    private void merge(ListNode head, ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) return;
        if (list1 == null) head.next = list2;
        else if (list2 == null) head.next = list1;
        else {
            if (list1.val < list2.val) {
                head.next = list1;
                list1 = list1.next;
            } else {
                head.next = list2;
                list2 = list2.next;
            }
            merge(head.next, list1, list2);
        }
    }
}
```

# Learned
재귀적으로 문제를 해결하는것이 반복문으로 해결하는 것 보다 깔끔하게 짤 수 있는 경우가 있다. 재귀로 짜게 될 경우 종료조건을 잘 설정해주는것이 중요하다.