# Intuition
이진 탐색 트리의 조건을 생각한다.
 - 부모 노드의 왼쪽 노드는 부모 노드보다 작아야 한다.
 - 부모 노드의 오른쪽 노드는 부모 노드보다 커야 한다.

# Approach
1. 부모 노드가 null이면 참으로 반환한다.
2. 이진 탐색 트리의 조건에 벗어나면 거짓을 반환한다.
 2.1. 부모 노드의 왼쪽 노드들의 값이 부모 노드보다 크다.
 2.2. 부모 노드의 오른쪽 노드들의 값이 보무 노드보다 작다.
3. 위의 과정을 재귀적으로 반복한다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```js
var CheckBST = function(root, left, right) {
    if(root === null) return true;
    if(left !== null && (left >= root.val)) {
        return false;
    }

    if(right !== null && (right <= root.val)) {
        return false;
    }

    return CheckBST(root.left, left, root.val) && CheckBST(root.right, root.val, right);
}
var isValidBST = function(root) {
    return CheckBST(root, null, null);
};
```