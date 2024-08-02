# Same Tree
---
## 문제 해결 방법
---
* 두 노드가 nullptr인지 확인 후 둘 다 nullptr일 경우 true를 반환한다.
* 두 노드의 값을 비교 후 다르면 false를 반환한다.
* 두 노드의 left와 right에도 재귀적으로 함수를 적용한다.
## 자료구조 알고리즘
---
* 트리
## 성능
---
* O(n) /  O(n)
## 알게 된 것
---
* 
## 코드
```cpp/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
 public:
  bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    if (p->val != q->val) return false;
    return isSameTree(p->right, q->right) && isSameTree(p->left, q->left);
  }
};
```