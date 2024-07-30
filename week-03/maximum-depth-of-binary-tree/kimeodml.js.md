# Intuition

재귀를 활용해 트리의 최대 깊이 계산

# Approach

1. root가 null일 경우 높이는 0
2. 왼쪽 노드와 오른쪽 노드를 각각 재귀적으로 계산
  2.1. Math.max 함수를 이용해 더 깊은 값을 파악하고, 1을 더함

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var maxDepth = function(root) {
    if(root === null) return 0;
    else return Math.max(maxDepth(root.right), maxDepth(root.left))+1;
};
```