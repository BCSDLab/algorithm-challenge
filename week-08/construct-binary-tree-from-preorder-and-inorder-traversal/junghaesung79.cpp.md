# Construct Binary Tree From Preorder And Inorder Traversal
---
## 문제 해결 방법
---
1
* preorder의 순서대로 노드를 만든다
* inorder를 힌트로 노드들을 재귀적으로 연결한다.
2
* inorder를 unordered_map에 넣는다.
* preorder의 순서대로 노드를 만든다.
* 각 반복에서 preorder의 값을 inorderMap에서 찾고 그 값의 앞 뒤 인덱스를 이요해 재귀적으로 연결한다.
## 성능
---
* O(n ^ 2) / O(n ^ 2)
* O(n) / O(n)
## 알게 된 것
---
* 인덱스를 알아야 한다 -> unordered_map에 넣는다
* 재귀에서 배열을 인자로 전달한다 -> 인덱스만을 넘긴다

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
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.empty() || inorder.empty()) return nullptr;

    TreeNode* root = new TreeNode(preorder[0]);
    preorder.erase(preorder.begin());

    auto it = find(inorder.begin(), inorder.end(), root->val);
    int position = distance(inorder.begin(), it);

    vector<int> left(inorder.begin(), it);
    vector<int> right(it + 1, inorder.end());

    root->left = buildTree(preorder, left);
    root->right = buildTree(preorder, right);

    return root;
  }
};

///

class Solution {
 private:
  unordered_map<int, int> inorderMap;
  int pre = 0;

  TreeNode* dfs(vector<int>& preorder, int start, int end) {
    if (pre >= preorder.size() || start > end) return nullptr;

    int val = preorder[pre++];
    int mid = inorderMap[val];

    TreeNode* root = new TreeNode(val);
    root->left = dfs(preorder, start, mid - 1);
    root->right = dfs(preorder, mid + 1, end);

    return root;
  }

 public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    for (int i = 0; i < inorder.size(); i++) {
      inorderMap[inorder[i]] = i;
    }

    return dfs(preorder, 0, inorder.size() - 1);
  }
};
```
