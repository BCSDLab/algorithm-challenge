# Intuition
연결 리스트의 노드 개수를 세면서 set에도 저장하여 개수가 달라지는지 확인한다.

# Approach
```java
1. head를 curr 변수에 저장하고 curr에 null이 들어올 동안 while문을 반복한다.
2. count를 증가해서 node의 개수를 세는 역할을 한다.
3. set에 curr를 저장해서 중복된 노드는 저장하지 않는다.
4. set의 개수와 count의 개수가 다르면 true를 반환한다.
5. curr의 next를 curr에 저장한다.
6. while문이 끝나고 count와 set의 개수가 다르면 true를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
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
        ListNode curr = head;
        int count = 0;
        Set<ListNode> set = new HashSet<>();
        while (curr != null) {
            count++;
            set.add(curr);
            if (count != set.size()) {
                System.out.println("count는: "+count + "// set size는: " +set.size());
                return true;
            }
            curr = curr.next;
        }

        return count != set.size();
    }
}
```
