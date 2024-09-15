# Intuition
각 문자를 상하좌우로 이동하면서 찾아야 하므로, DFS를 이용해서 해결한다.

# Approach
1. 2D 배열의 각 위치에서 주어진 단어가 시작할 수 있는지 확인하기 위해, 보드의 각 셀에서 DFS를 시작한다.
2. DFS를 통해 상하좌우로 이동하며, 현재 문자가 단어와 일치하는지 확인한다.
3. 문자가 일치하면 다음 문자로 넘어가고, 모든 문자를 찾으면 true를 반환한다.
4. 탐색 중에 이미 방문한 셀은 임시로 다른 값으로 변경하고, 탐색이 끝난 후 복원한다.
5. 모든 경로를 탐색했음에도 단어를 찾지 못하면 false를 반환한다.

# Complexity
- Time complexity: $O(n⋅m⋅4k)$
    - 각 셀에서 DFS를 호출하고, 최대 4방향으로 탐색한다.

- Space complexity: $O(K)$
    - DFS 호출 스택의 깊이는 단어의 길이인 k에 비례

# Code
```java []
class Solution {
    public boolean exist(char[][] b, String w) {
        int r = b.length;
        int c = b[0].length;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (dfs(b, w, i, j, 0)) return true;
            }
        }

        return false;
    }

    private boolean dfs(
        char[][] b,
        String w,
        int i,
        int j,
        int idx
        ) {
        if (idx == w.length()) return true;

        if (
            i < 0 ||
            i >= b.length ||
            j < 0 ||
            j >= b[0].length ||
            b[i][j] != w.charAt(idx)
        ) return false;

        char temp = b[i][j];
        b[i][j] = '#';

        boolean found = dfs(b, w, i + 1, j, idx + 1) ||
                        dfs(b, w, i - 1, j, idx + 1) ||
                        dfs(b, w, i, j + 1, idx + 1) ||
                        dfs(b, w, i, j - 1, idx + 1);

        b[i][j] = temp;

        return found;
    }
}

```

# Learned
백트래킹 👍