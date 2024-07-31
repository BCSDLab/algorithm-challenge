# Intuition
자료구조 시간에 배운 두 개의 포인터를 이용해서 문제를 푼다. 하나의 포인터는 한칸씩 다른 하나의 포인터는 두칸씩 이동하면서 싸이클이 있는지 확인한다.

# Approach
1. 2칸씩 이동하는 노드와 한칸씩 이동하는 노드를 생성한다.
2. 싸이클이 없다면, 2칸씩 이동하는 노드의 `next`는 `null`값이 될 수 있다. 따라서 `next`가 `null`이 아닌 동안 `while`문을 돌고 만약 다 돌 수 있다면 싸이클이 없다는 것.
3. 싸이클이 있다면 `while`문은 무한반복을 할것이다. 그렇다면 `fast`와 `slow`는 무조건 한번 만난다. 만난다면 `return true`

# Complexity
- Time complexity: $O(N)$
    - 입력 노드의 개수만큼 반복 → $O(N)$

- Space complexity: $O(1)$
    - 입력 노드의 수에 따른 추가 공간을 사용하지 않기 때문에 → $O(1)$

# Code
``` java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        if (head.next == null) return false;
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) return true;
        }
        return false;
    }
}
```

# Learned
김상진교수님의 자료구조시간에 배웠던 내용을 활용해 볼 수 있어서 좋았습니다. 두 개의 포인터로 노드를 이동할 때 싸이클이 있다면 무조건 한번은 두 포인터가 만난다는것을 배웠습니다. 만약 싸이클이 없다면 fast는 slow보다 무조건 빨리 `LinkedList`를 순회합니다.