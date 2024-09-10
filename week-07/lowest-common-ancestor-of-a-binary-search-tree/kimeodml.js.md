# Intuition
재귀적으로 노드를 비교하면서 최저 공통 부모 노드를 찾는다.

# Approach
1. 두 개의 노드 모두 루트 노드 보다 크면 공통 부모 노드가 좌측 서브 트리에 존재
2. 두 개의 노드 모두 루트 노드 보다 ㅈ가으면 공통 부모 노드가 우측 서브 트리에 존재
3. 위의 과정을 재귀적으로 반복한다.

# Complexity
- Time complexity: $O(h)$
  - 트릐 높이(h)
- Space complexity: $O(n)$
  - 노드의 크기(n)

# Code
```js
var lowestCommonAncestor = function(root, p, q) {
    if(root.val < p.val && root.val < q.val) {
        return lowestCommonAncestor(root.right, p, q);
    }
    if(root.val > p.val && root.val > q.val) {
        return lowestCommonAncestor(root.left, p, q);
    } 
    
    return root;
};
```