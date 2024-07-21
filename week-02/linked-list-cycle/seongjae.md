# Intuition
빠른 포인터와 느린 포인터 두 가지 포인터를 이용해 두 포인터가 만나면 사이클이다.

# Approach
1. 입력이 null인 경우, 리스트에 사이클이 없다고 간주하고 false를 반환한다.
2. fast 포인터와 그 다음 노드(fast.next)가 null이 아닌 동안 반복한다.
3. slow 포인터는 한 번에 한 노드씩, fast 포인터는 한 번에 두 노드씩 이동한다.
4. slow 포인터와 fast 포인터가 만나는 경우, 리스트에 사이클이 존재함을 의미하므로 true를 반환한다.
4. fast 포인터가 null에 도달하면 리스트에 사이클이 없음을 의미하므로 false를 반환한다.

# Complexity
- Time complexity: O(n)
리스트의 노드를 한 번씩 방문하며, 각 방문에서 상수시간 작업을 수행한다.
- Space complexity: O(1)
추가적인 데이터 구조를 사용하지 않는다.

# Code 
Runtime: 0ms Memory Usage: 44.44MB
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
public class LinkedListCycle141 {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}
```

# Learned
잘 모르겠는 스타일의 문제여서 못 풀었던 문제여서 공부하고 풀었다.
이 문제를 통해 토끼와 거북이 알고리즘을 통해 사이클이 있는지 확인 하는 방법을 배웠다.
