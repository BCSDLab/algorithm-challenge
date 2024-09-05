# Intuition
맵을 활용해 레벨별 노드를 저장한다.

# Approach
1. 각 레벨별 노드를 저장할 map을 선언한다.
2. level이 없으면 map에 level을 추가한다.
3. level이 존재하면 현재의 노드를 level에 추가한다.
5. 위의 방법을 노드가 끝날 때까지 반복한다.
6. 저장된 결괏값 중 value값만 출력한다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```js
var dfs = function(root, level, map) {
    if(root === null) return [];
    if(!map.has(level)) {
        map.set(level,[]);
    }
    map.get(level).push(root.val);

    dfs(root.left, level+1, map);
    dfs(root.right, level+1, map);
};

var levelOrder = function(root) {
    let map = new Map();
    dfs(root, 0, map);
    
    return Array.from(map).map(([key, value]) => value);
};
```