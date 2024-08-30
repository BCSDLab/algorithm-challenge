# Kth Smallest Element In a Bst
---
## 문제 해결 방법
---
1
* 우선순위 큐에 트리의 요소들을 넣는데 size를 k 개수만큼 유지한다.
* top을 반한다. (c++에서는 최대힙이므로)
2
* 주어진 트리를 중위 순회하여 벡터에 저장한다.
* k번째 요소를 반한다.(인덱스: k - 1)
## 자료구조 알고리즘
---
* 우선순위 큐
* 힙
## 성능
---
* O(n log k) / O(k + h)
* O(n) / O(h)
## 알게 된 것
---
* 전중후위 dfs 표현
* 알고달래 대박...
  * 난 언제쯤 돼야 혼자서 저런 깔끔한 풀이를 만들 수 있을까...

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
  int kthSmallest(TreeNode* root, int k) {
    priority_queue<int> pq;
    dfs(root, k, pq);

    return pq.top();
  }

 public:
  void dfs(TreeNode* node, int k, priority_queue<int>& pq) {
    if (!node) return;

    pq.push(node->val);
    if (pq.size() > k) {
      pq.pop();
    }

    dfs(node->left, k, pq);
    dfs(node->right, k, pq);
  }
};

///

class Solution {
 public:
  int kthSmallest(TreeNode* root, int k) {
    vector<int> values;
    dfs(root, values);

    return values[k - 1];
  }

 private:
  void dfs(TreeNode* node, vector<int>& values) {
    if (!node) return;
    dfs(node->left, values);
    values.push_back(node->val);
    dfs(node->right, values);
  }
};
```
