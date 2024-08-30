# Lowest Common Ancestor of a Binary Search Tree
---
## 문제 해결 방법
---
* 부모 노드가 중간 값인 특성을 이용해서 p와 q의 사이에 들어올 때까지 root를 이동한다.
## 자료구조 알고리즘
---
* 이진 트리
## 성능
---
* O(h) / O(1)

## 코드
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;ㅈ
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
 public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (root == nullptr) return nullptr;

    if ((p->val <= root->val && root->val <= q->val) ||
        (q->val <= root->val && root->val <= p->val)) {
      return root;
    }

    if (root->val > p->val && root->val > q->val) {
      return lowestCommonAncestor(root->left, p, q);
    }

    return lowestCommonAncestor(root->right, p, q);
  }
};
```
