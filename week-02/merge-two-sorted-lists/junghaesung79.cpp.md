# Merge Two Sorted Lists
---
## 문제 해결 방법
---
1
* list1과 list2에 요소가 있을 경우, 이 둘을 비교하여 더 작은 값을 current에 넣는다.
* 만약 둘 중 하나라도 요소가 없을 경우, current에 나머지 리스트를 붙인다.
* dummy가 가리키는 리스트 헤드를 반한다.
## 자료구조 선택
---
* linked_list
## 성능
---
* 입력 노드를 그대로 사용하기에 공간 복잡도 O(1)
* O(n + m) / O(1)
## 알게 된 것
---
* dummy 노드
  * 링크드 리스트 반환 문제에서 시작 전에 위치하는 가상 노드(객체임!!)
  * 코드를 단순화한다.
    * 로직에서 사용되는 변수가 줄어들어서 가독성이 좋아진다.
  * return dummy.next;
  * 링크드 리스트에 익숙해지려면 더 풀어봐야겠다.
## 코드
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode dummy(0);
    ListNode* current = &dummy;

    while (list1 && list2) {
      if (list1->val <= list2->val) {
        current->next = list1;
        list1 = list1->next;
      } else {
        current->next = list2;
        list2 = list2->next;
      }
      current = current->next;
    }

    if (list1) current->next = list1;
    if (list2) current->next = list2;

    return dummy.next;
  }
};
```