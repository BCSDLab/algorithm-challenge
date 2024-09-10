# Intuition

평범한 dfs 문제다. 였으나 뇌빼고 풀다가 오래걸렸다.

# Approach

1. 보드의 모든 셀을 시작점으로 하여 DFS를 수행한다.
2. DFS 에서 다음을 확인한다:
	- 현재 위치가 보드 범위 내에 있는지
	- 현재 셀의 문자가 찾고 있는 단어의 현재 인덱스의 문자와 일치하는지
	- 단어의 모든 문자를 찾았는지 (종료 조건)
3. 현재 셀을 방문했음을 표시하기 위해 임시로 값을 제거한다.
4. 상하좌우 네 방향으로 DFS를 재귀적으로 수행한다.
5. 백트래킹을 위해 셀의 원래 값을 복구한다.

# Complexity
- Time complexity: $$O(M \times N \times 4^L)$$
	- M, N은 보드의 크기, L은 단어의 길이

- Space complexity: $$O(N)$$
	- N은 단어의 길이

# Code
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        d = [0, 1, 0, -1, 0]

        def dfs(x, y, idx):
            if not (0 <= x < n and 0 <= y < m):
                return False
            
            if board[y][x] != word[idx]:
                return False
            
            if len(word)-1 == idx:
                return True
	        
	        tmp, board[y][x] = board[y][x], ''
            
            for i in range(4):
                if dfs(x+d[i], y+d[i+1], idx+1):
                    return True
            
			board[y][x] = tmp
            
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(j, i, 0):
                    return True

        return False

```

