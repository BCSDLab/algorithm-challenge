# Intuition
리스트의 길이를 먼저 계산하지 않고, 재귀적으로 노드를 탐색하며 뒤에서 n번째 노드를 찾는다.

# Approach
1. 재귀적으로 연결 리스트의 끝까지 탐색한 후, 다시 돌아오면서 인덱스를 증가시킨다.
2. 인덱스가 n과 같아지면 해당 노드를 건너뛰어 제거한다.
3. 나머지 노드는 그대로 연결하여 반환한다.

# Complexity
- Time complexity: $O(N)$
    - 리스트를 한 번 순회하기 때문에 $O(N)$

- Space complexity: $O(N)$
    - 재귀 호출 스택의 깊이가 리스트의 길이만큼 필요하기 때문에 $O(N)$

# Code
```java []
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
    int index = 0;
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        head.next = removeNthFromEnd(head.next, n);
        ++index;
        if (n == index) return head.next;
        return head;
    }
}
```