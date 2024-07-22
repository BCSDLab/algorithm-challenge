# Linked List Cycle
---
## 문제 해결 방법
---
* head와 head->next를 검사해서 빈 리스트가 아닌지 확인한다.
* 토끼 포인터와 거북기 포인터를 만든다.
* 토끼 포인터는 두 노드씩, 거북이 포인터는 한 노드씩 이동한다.
* 두 노드가 같은 노드인지 검사하고 같으면 true를 반환한다.
* 만약 순환 리스트가 아닐 경우 토끼 노드가 null을 가리키면서 false를 반환한다.
## 자료구조 선택
---
* linked_list
## 성능
---
* O(n) / O(1)
## 알게 된 것
---
* 플로이드의 토끼와 거북이 알고리즘
  * 두 단계 가는 포인터와 한 단계 가는 포인터가 만나면 순환
## 코드
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
 public:
  bool hasCycle(ListNode *head) {
    if (!head || !head->next) return false;

    ListNode *fast = head->next;
    ListNode *slow = head;

    while (fast && fast->next) {
      if (fast == slow) return true;

      fast = fast->next->next;
      slow = slow->next;
    }

    return false;
  }
};
```