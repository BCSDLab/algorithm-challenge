# Intuition
노드를 하나씩 비교하면서 추가한다.

# Approach
1. 더미를 생성한다.
2. list1, list2의 현재 노드를 반복하며 비교한다
3. 남은 노드들 연결한다.

# Complexity
- Time complexity: O(n + m)
list1과 list2의 노드를 한번씩 방문한다.

- Space complexity: O(1)
추가적인 리스트나 데이터 구조를 사용하지 않는다. 

# Code
Runtime: 0ms Memory Usage: 42.48MB
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
public class MergeTwoSortedLists21 {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode buffer = new ListNode();
        ListNode current = buffer;

        while(list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        return buffer.next;
    }
}
```

# Learned
