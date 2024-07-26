# Maximum Depth of Binary Tree
---
## 문제 해결 방법
---
1
* 재귀적으로 동작시키기 위해 maxDepth의 매개변수에 size를 추가한다.
* root가 nullptr인 경우는 초기 트리가 비어 있을 경우이므로 0을 반환한다.
* left, right의 노드가 존재하는 지에 따라
  * 인자 size를 그대로 반환한다.
  * 1을 증가하여 반환한다.
  * 1을 증가한 후 재귀 호출한다.
2
* 1번의 코드를 최적화한다.
## 자료구조 알고리즘
---
* 트리
## 성능
---
* O(n) / O(h: 높이)
## 알게 된 것
---
* 매개변수를 임의로 추가할 수 있다.
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
  int maxDepth(TreeNode* root, int size = 1) {
    if (root == nullptr) return 0;
    if (root->left == nullptr && root->right == nullptr) return size;
    if (root->left != nullptr && root->right != nullptr) {
      size++;
      size = max(maxDepth(root->left, size), maxDepth(root->right, size));
      return size;
    };
    if (root->left != nullptr) {
      size++;
      return maxDepth(root->left, size);
    }
    if (root->right != nullptr) {
      size++;
      return maxDepth(root->right, size);
    }

    return size;
  }
};

///

class Solution {
 public:
  int maxDepth(TreeNode* root) {
    if (root == nullptr) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
  }
};
```