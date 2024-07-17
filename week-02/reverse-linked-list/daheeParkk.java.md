# Intuition
이전 노드와 다음 노드를 저장해서 현재 노드가 이전 노드를 가리키고, 다음 노드가 현재 노드가 되도록 한다.

# Approach
```java
1. curr에 head를 넣고 curr가 null이 아닐 동안 다음 작업을 반복한다.
2. curr의 다음 노드를 변수에 저장한다.
3. curr의 다음 노드를 이전 노드로 바꾼다.
3-1. curr의 prev가 없으면 curr의 next에 null을 넣는다. 
3-2. curr의 prev가 있으면 next에 prev를 넣는다.
4. curr를 prev에 넣는다.
4. curr의 원래 다음 노드를 curr에 넣는다.
5. curr가 null이 되면 prev를 반환한다.
```

# Complexity
- Time complexity:
  O(n)

- Space complexity:
  O(n)

# Code
```java
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
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            if (prev == null) {
                curr.next = null;
            } else {
                curr.next = prev;
            }
            
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
```
