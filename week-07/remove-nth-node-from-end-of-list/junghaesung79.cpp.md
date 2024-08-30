# Remove Nth Node From End of List
---
## 문제 해결 방법
---
* n만큼 위치 차이가 나는 두 포인터를 만든다.
* 꼬리쪽 포인터가 끝에 도달했을 때 중간 포인터는 목표한 위치를 가리킨다.
* 그것을 빼낸 리스트의 head를 반환한다.
## 자료구조 알고리즘
---
* 링크드 리스트
## 성능
---
* O(n) / O(1)
## 알게 된 것
---
* delete로 메모리 해제
  * 알고리즘 문제 풀 때 하지 않아도 무방하나 코딩테스트 또는 면접 상황을 생각하면 포함하는 것 권장한다.
  * 단점은 본 로직에 집중도가 떨어질 수 있다

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
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode* end = head;
    for (int i = 0; i < n; i++) {
      end = end->next;
    }

    ListNode* dummy = new ListNode(-1, head);
    ListNode* mid = dummy;
    while (end) {
      end = end->next;
      mid = mid->next;
    }

    ListNode* temp = mid->next;
    mid->next = mid->next->next;
    delete temp;

    ListNode* result = dummy->next;
    delete dummy;
    return result;
  }
};
```
