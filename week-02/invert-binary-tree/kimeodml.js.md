# Intuition

재귀를 활용해 오른쪽 노드와 왼쪽 노드를 교환

# Approach

1. 현재 node가 null일 경우 null을 반환
2. 현재 노드의 오른쪽/왼쪽을 서로 교환
3. inverTree를 재귀적으로 호출하여 하위 노드도 동일하게 교환
4. 루트 노드 반환

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var invertTree = function(root) {
    if(!root) return null;

    [root.right, root.left] = [root.left, root.right];
    invertTree(root.right);
    invertTree(root.left);
    return root;
};
```