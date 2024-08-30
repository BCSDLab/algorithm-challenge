# Binary Tree Level Order Traversal
---
## 문제 해결 방법
---
  * BFS. 큐를 만들어서 루트부터 각 레벨, 좌우 짝 요소를 배열에 저장한다.
  * 그 배열들을 결과 배열에 저장하여 반환한다.
## 자료구조 알고리즘
---
* 트리, BFS
## 성능
---
* O(n) / O(n)

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
  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
      int levelSize = q.size();
      vector<int> currentLevel;

      for (int i = 0; i < levelSize; i++) {
        TreeNode* node = q.front();
        q.pop();
        currentLevel.push_back(node->val);

        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
      }

      result.push_back(currentLevel);
    }

    return result;
  }
};
```
