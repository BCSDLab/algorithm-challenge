# Intuition

현재의 노드가 이전 노드를 가리키도록 변경

# Approach

1. cur 노드에 head를 prev 노드를 null로 초기화
2. cur 노드가 mull이 아닐 때까지 반복
  2.1. 다음 노드를 cur에 저장
  2.2. 다음 노드를 prev 노드로 변경(노드 연결 반전)
  3.4. prev 노드를 현재 노드로 업데이트
  2.3. 현재 노드를 다음 노드로 업데이트
3. 반전된 노드 반환


# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(1)

# Code
```js
var reverseList = function(head) {
    let cur = head;
    let prev = null;
    while(cur) {
        cur = head.next;
        head.next = prev;
        prev = head;
        head = cur;
    }
    return prev;
};
```