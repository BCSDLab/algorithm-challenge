# Intuition
현재 노드의 다음 포인터를 이전 노드를 가리키도록 한다.

# Approach
1. nextTemp를 curr.next로 설정하여 다음 노드를 임시로 저장
2. curr.next를 prev로 설정하여 현재 노드의 포인터를 뒤집는다.
3. prev를 curr로 업데이트하여 이전 노드를 현재 노드로 이동한다.
4. curr를 nextTemp로 업데이트하여 현재 노드를 다음 노드로 이동한다.

# Complexity
- Time complexity: O(n)
각 리스트를 한 번씩 방문하므로 O(n)
- Space complexity: O(1) 
추가적인 리스트나 데이터 구조를 사용하지 않으며, 상수 공간을 사용

# Code 
Runtime: 0ms Memory Usage: 42.09MB
```java
/**
 public class ListNode {
 int val;
 ListNode next;
 ListNode() {}
 ListNode(int val) { this.val = val; }
 ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 */
public class ReverseLinkedList206 {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while(curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        return prev;
    }
}
```

# Learned
각 노드의 포인터를 어떻게 뒤집어야 효율적일지 배웠다.
