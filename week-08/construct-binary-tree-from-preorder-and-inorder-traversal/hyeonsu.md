# Intuition
전위 순회와 중위 순회 결과를 이용해 이진 트리를 재구성하면 된다.

# Approach
1. 전위 순회의 첫 번째 요소는 항상 현재 서브트리의 루트가 된다.
2. 중위 순회 배열에서 루트 노드의 인덱스를 찾아 왼쪽 서브트리와 오른쪽 서브트리를 구분한다.
3. 재귀적으로 왼쪽과 오른쪽 서브트리를 구성하여 전체 트리를 완성한다.
4. 중위 순회의 각 값을 빠르게 찾기 위해 해시맵을 사용하여 값을 인덱스와 매핑한다.

# Complexity
- Time complexity: $O(N)$
전위 순회와 중위 순회 배열을 한 번씩 순회하며 각 값을 처리하므로 $O(N)$

- Space complexity: $O(N)$
해시맵을 사용하여 중위 순회의 인덱스를 저장하고, 재귀 호출 스택이 트리의 깊이만큼 필요하므로 $O(N)$

# Code
```java []
import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Integer, Integer> map;
    private int preIdx;

    public TreeNode buildTree(int[] pre, int[] in) {
        map = new HashMap<>();
        for (int i = 0; i < in.length; i++) {
            map.put(in[i], i);
        }
        preIdx = 0;
        return helper(pre, 0, in.length - 1);
    }

    private TreeNode helper(int[] pre, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return null;
        }

        int rootVal = pre[preIdx++];
        TreeNode root = new TreeNode(rootVal);
        int inIdx = map.get(rootVal);

        root.left = helper(pre, inStart, inIdx - 1);
        root.right = helper(pre, inIdx + 1, inEnd);

        return root;
    }
}

```

# Learned
전위 순회와 중위 순회를 이용해 이진 트리를 재구성하는 방법을 배웠다.