# Intuition
연결 리스트의 길이를 구해 (길이 - n)만큼 연결한 후에 뒤에서 n 번째 숫자는 제외해 연결한다.

# Approach
1. 연결 리스트의 길이를 구한다.
2. 구한 길이의 길이 - n 만큼 연결한다.
3. 연결할 때 뒤에서 n 번째 숫자는 제외한다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(1)$

# Code
```js
var removeNthFromEnd = function(head, n) {
    let length = 0;
    let cur = head;
    while(cur) {
        length += 1;
        cur = cur.next
    }

    let dummy = new ListNode(0, head);
    cur = dummy;
    
    for(let i = 0; i < length - n;i++) {
        cur = cur.next;
    }
    cur.next = cur.next.next;

    return dummy.next;
};
```