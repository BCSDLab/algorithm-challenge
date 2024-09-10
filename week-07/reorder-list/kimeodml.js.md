# Intuition
투포인터로 접근하여 사용해 절반을 역순 연결 리스트로 만든 후에 합친다.

# Approach
1. 러너 기법을 활용해 slow와 fast 연결 리스트 두 종류를 만든다.
2. fast의 연결 리스트를 역순으로 연결한다.
3. 각각의 연결 리스트를 다시 합친다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(1)$

# Code
```js
var reorderList = function(head) {
    let slow = head, fast = head;
    let prev = null;

    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let cur = slow.next;
    slow.next = null;

    while(cur) {
        let temp = cur.next;
        cur.next = prev;
        prev = cur;
        cur = temp;
    }

    let first = head, second = prev;
    while(second) {
        let temp1 = first.next;
        let temp2 = second.next;

        first.next = second;
        second.next = temp1;

        first = temp1;
        second = temp2;
    }
    
    return prev;
};
```

## 알게된 점
두 개의 포인터가 서로 다른 속도로 이동하는 러너 기법에 대해 알게 되었다.