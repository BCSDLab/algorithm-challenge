# Intuition
tmp를 활용해서 두 연결된 리스트간의 연결을 끊고 이전 노드와 연결하자

# Approach
<!-- Describe your approach to solving the problem. -->
1. 리스트에 연결된 리스트를 저장한 후 거꾸로 순회하는 방식은 간단하지만 반복문을 2회 진행해야했다. 따라서 tmp를 만들어 바로 연결을 바꿔주는 방식으로 반복문 1회로 마무리했다.
2. 이전 노드, 현재 노드, 다음 노드를 저장할 변수를 선언한다.
3. 연결을 끊으면 다음 노드로 이동할 방법이 없으므로 다음 노드를 우선 저장한다.
4. 현재 노드의 next를 이전 노드로 지정한다.
5. 이전 노드를 현재 노드로 지정한다.
# Complexity
- Time complexity: $$O(n)$$
반복문 1회
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
linked list의 크기
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        return prev
```

