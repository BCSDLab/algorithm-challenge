# Subtree of Another Tree
---
## 문제 해결 방법
---
1
* 이전 문제의 메서드(isSameTree)를 활용한다.
* subRoot가 nullptr일 경우 true
* 이후 root가 nullptr일 경우 false
* 이후 root와 subRoot를 isSameTree하여 포함을 검사한다.
2
* root와 subRoot에 존재하는 모든 요소를 string으로 변환한다.
* rootString이 subRootString을 포함하는 지 검사한다.
## 자료구조 알고리즘
---
* 트리
## 성능
---
* O(r * s) / O(r + s)
* O(r + s) / O(r + s)
## 알게 된 것
---
* 알고달래 풀이에서 스냅샷으로 만들고 포함을 확인하는 방법이 신기했다.
  * 괄호를 붙여서 
* 파이썬 문법 진짜 너무 간편해보인다..(A in B)
* string::npos = (find 등에서) 찾지 못함
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
  bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    if (subRoot == nullptr) return true;
    if (root == nullptr) return false;

    if (isSameTree(root, subRoot)) return true;

    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
  }

 private:
  bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    if (p->val != q->val) return false;
    return isSameTree(p->right, q->right) && isSameTree(p->left, q->left);
  }
};

///

class Solution {
 public:
  bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    string rootString = pre(root);
    string subRootString = pre(subRoot);

    return rootString.find(subRootString) != string::npos;
  }

 private:
  string pre(TreeNode* node) {
    if (node == nullptr) return "N";
    return "(" + to_string(node->val) + "," + pre(node->left) + "," + pre(node->right) + ")";
  }
};
```