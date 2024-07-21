# Intuition

두 개의 연결 리스트를 서로 비교하면서 이동

# Approach

1. 하나의 dummy 노드를 생성(리스트의 시작점)
2. list1과 list2가 존재할 때까지 반복하면서 서로의 값을 비교 후 연결
3. 남은 노드가 있을 경우 결과 리스트에 연결
4. 결과 리스트 반환

# Complexity

- 시간복잡도: O(n+m)
- 공간복잡도: O(1)

# Code
```js
var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode();
    let tail = dummy;

    while(list1 && list2) {
      if(list1.val >= list2.val) {
        tail.next = list2;
        list2 = list2.next;
      } else {
        tail.next = list1;
        list1 = list1.next;
      }
      tail = tail.next;
    }

    tail.next = list1 || list2;
    return dummy.next;
};
```