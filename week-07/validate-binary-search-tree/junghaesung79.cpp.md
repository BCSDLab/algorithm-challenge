# Validate Binary Search Tree
---
## 문제 해결 방법
---
* DFS, 루트 노드에서 시작해서 먼저 자기자신이 양쪽 값 사이에 있는 지 확인한다.
* 양쪽 요소에 대하여 재귀 호출하여 검사를 반복한다.
## 자료구조 알고리즘
---
* 트리, DFS
## 성능
---
* O(n) / O(h)
## 알게 된 것
---
* LONG_MIN과 LONG_MAX

## 코드
```cpp
/**
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
  bool isValidBST(TreeNode* root) {
    return dfs(root, LONG_MIN, LONG_MAX);
  }

 private:
  bool dfs(TreeNode* node, long long low, long long high) {
    if (!node) {
      return true;
    }
    if (!(low < node->val && node->val < high)) {
      return false;
    }
    return dfs(node->left, low, node->val) && dfs(node->right, node->val, high);
  }
};
```
