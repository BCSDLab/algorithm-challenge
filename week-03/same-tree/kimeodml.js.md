# Intuition

각 트리의 오늘쪽 노드와 왼쪽 노드를 재귀를 활용해 비교

# Approach

1. p와 q 모두 root가 null일 경우 동일하므로 true로 반환
2. p가 null이고 q에 노드가 존재하거나 p에 노드가 존재하고 q가 null일 경우 서로 다르므로 false를 반환
3. p와 q의 현재 노드값이 다를 경우 false를 반환
4. p와 q의 노드값이 같으면 각각 트리의 오른쪽 노드와 왼쪽 노드를 재귀적으로 비교

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var isSameTree = function(p, q) {
   if(p === null && q === null) return true;
   if((p === null && q !==null) || (p !== null && q ===null)) return false;
   if(p.val !== q.val) return false;
   else return isSameTree(p.left, q.left) && isSameTree(p.right, q.right); 
};
```