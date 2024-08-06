# Intuition

set을 이용해 중복 감지

# Approach

1. 빈 해시셋을 생성
2. 노드를 순회하면서 해시셋에 존재하면 true 아니면 false를 반환

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var hasCycle = function(head) {
    let cur = head;
    let node = new Set();
    while(cur) {
      if(node.has(cur)) {
        return true;
      }
      node.add(cur);
      cur = cur.next;
    }
    return false;
};
```