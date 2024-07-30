# Intuition

same-tree 문제에 사용되었던 함수를 활용해 부분 트리인지 확인

# Approach

1. root가 null이면 subRoot는 부분 트리가 될 수 없으므로 false를 반환
2. isSameTree 함수를 생성해 root와 subRoot가 동일하면 true로 반환
  2.1. root와 subRoot 모두 null일 경우 동일하므로 true로 반환
  2.2. 둘 중 하나만 null인 경우 false로 반환
  2.3. root과 subRoot의 현재 노드값이 다를 경우 false를 반환
  2.4. root과 subRoot의 노드값이 같으면 각각 트리의 오른쪽 노드와 왼쪽 노드를 재귀적으로 비교
3. 현재 노드의 자식 노드에 subRoot를 부분 트리로 가지고 있는지 비교

# Complexity

- 시간복잡도: O(r*s)
- 공간복잡도: O(r+s)

# Code
```js
var isSameTree = function(r, s) {
    if(r === null && s === null) return true;
    if((r === null && s !==null) || (r !== null && s ===null)) return false;
    if(r.val !== s.val) return false;
    else return isSameTree(r.left, s.left) && isSameTree(r.right, s.right);
}
var isSubtree = function(root, subRoot) {
    if(root === null) return false;
    if(isSameTree(root, subRoot)) return true;
    else return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
```