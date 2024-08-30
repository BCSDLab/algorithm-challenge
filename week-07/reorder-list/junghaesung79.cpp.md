# Reorder List
---
## 문제 해결 방법
---
1
* 리스트를 거꾸로 갖는 배열을 만든다.
* head와 배열에서 하나씩 끼워넣는다.
2
* 리스트를 절반 나눈다.
* 나눈 리스트를 뒤집는다.
* 두 리스트를 합하낟.
## 자료구조 알고리즘
---
* 링크드 리스트
## 성능
---
* O(n) / O(n)
* O(n) / O(1)
## 알게 된 것
---
* 더미 노드를 생성할 때 유효하지 않은 값임을 명시하는 목적으로 -1 사용
* 링크드 리스트 오랜만에 써봐서 어려웠다.
  * head를 반환하지 않고 그저 head가 가리켰던 위치의 정보들을 변경하는 것으로 채점하는 시스템이 조금 헷갈렸다.
  * 어떻게 풀어야 할 지 상상은 되는데 그것을 코드로 바꾸는 것이 어려웠다.

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
  void reorderList(ListNode* head) {
    if (!head || !head->next) return;

    vector<ListNode*> stack;
    ListNode* node = head;
    while (node) {
      stack.push_back(node);
      node = node->next;
    }

    ListNode dummy(-1);
    node = &dummy;
    int n = stack.size();
    for (int i = 0; i < n; i++) {
      if (i % 2) {
        node->next = stack.back();
        stack.pop_back();
      } else {
        node->next = head;
        head = head->next;
      }
      node = node->next;
    }
    node->next = nullptr;
  }
};
```
