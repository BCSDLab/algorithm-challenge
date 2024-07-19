# Reverse Linked List
---
## 문제 해결 방법
---
1
* 링크드 리스트를 스택에 넣고 다시 새로운 링크드 리스트를 만들어서 스택의 요소를 넣는다.
2
* 링크드 리스트의 링크 방향을 바꿔가며 순회한다.
3
* 어떤 노드와 다음 노드의 리스트의 연결을 반대쪽으로 바꾸는 재귀 함수를 만들어 실행한다.
## 자료구조 선택
---
* linked_list
* stack
## 성능
---
* O(n) / O(1)
## 알게 된 것
---
* 다양한 문제 풀이 방법
  * 입출력의 자료형이 같다면?
  * 재귀적으로 문제에 접근
  * 작은 문제로 쪼갠다.
* 화살표 연산자(->) 앞뒤에는 공백을 두지 않는다.
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
  ListNode* reverseList(ListNode* head) {
    stack<int> valueStack;
    ListNode* current = head;
    while (current != nullptr) {
      valueStack.push(current->val);
      current = current->next;
    }

    ListNode* reversedHead = nullptr;
    ListNode* reversedCurrent = nullptr;

    while (!valueStack.empty()) {
      ListNode* newNode = new ListNode(valueStack.top());
      valueStack.pop();

      if (reversedHead == nullptr) {
        reversedHead = newNode;
        reversedCurrent = newNode;
      } else {
        reversedCurrent->next = newNode;
        reversedCurrent = newNode;
      }
    }

    return reversedHead;
  }
};

///

class Solution {
 public:
  ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* current = head;
    ListNode* next = nullptr;

    while (current != nullptr) {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

    return prev;
  }
};

///

class Solution {
 public:
  ListNode* reverseList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }

    ListNode* reversedRest = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return reversedRest;
  }
};
```