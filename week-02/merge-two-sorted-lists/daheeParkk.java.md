# Intuition
작은 값의 노드를 찾아 next에 넣는다.

# Approach
```java
1. list가 null이면 다른 list를 반환한다.
2. 더 작은 값인 노드의 next와 다른 노드를 인자로 넣고 재귀한다.
3. 더 작은 값인 노드를 찾아 next에 저장 후 해당 list를 반환한다.
```
# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}
```
