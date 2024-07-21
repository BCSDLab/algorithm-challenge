# Intuition
`prev`노드를 유지하면서 `LinkedList`를 순회하며 방향만 바꿔준다.

# Approach
1. `currNode`와 `prevNode`를 만든다.
2. `currNode`를 이동시키며 `Link`를 바꿔준다.

# Complexity
- Time complexity: $O(N)$
    - 입력 `LinkedList`를 전부 순회해야 하기 때문에 $O(N)$

- Space complexity: $O(1)$
    - 입력 배열에 따라 사용하는 공간이 바뀌는게 아닌 상수비용이기 때문에 $O(1)$

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
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null;
        while(curr != null) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
}
```

# Learned
`prev`노드를 유지하며 `LinkedList`를 순회하면 `null`예외처리리를 하지 않아도 된다. 해결해야하는 문제에 복잡한 예외처리가 있다면 요소의 앞이나 뒤에 더미데이터를 추가해서 해결할 수 있는지 고민해보면 문제를 깔끔하게 해결할 수 있을 것 같다.