# Intuition
연결 리스트의 노드를 앞과 뒤에서 번갈아가며 재배치하면 된다.

# Approach
1. 리스트의 값을 순차적으로 배열에 저장한다.
2. 배열의 앞과 뒤에서 값을 번갈아가며 꺼내서 리스트의 노드를 재배치한다.
3. 배열의 중간까지 이를 반복하여 리스트를 재정렬한다.

# Complexity
- Time complexity: $O(N)$
    - 리스트의 노드를 한 번 순회하여 배열에 저장하고, 다시 배열에서 리스트로 값을 넣기 때문에 총 두 번의 순회가 필요하다. 때문에 $O(N)$

- Space complexity: $O(N)$
    - 리스트의 값을 저장하기 위한 배열을 사용하므로 추가 공간이 필요하다 따라서 $O(N)$

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
    public void reorderList(ListNode head) {
        List<Integer> vals = new ArrayList<>();
        ListNode currNode = head;
        while(currNode != null) {
            vals.add(currNode.val);
            currNode = currNode.next;
        }
        int count = 0;
        int l = 0, h = vals.size() - 1;
        while(count < vals.size()) {
            if (count % 2 == 0) head.val = vals.get(l++);
            else head.val = vals.get(h--);
            head = head.next;
            ++count;
        }
    }
}
```

# Learned
index를 조정해가며 프로그래밍 하는것에 익숙해질 수 있었다.