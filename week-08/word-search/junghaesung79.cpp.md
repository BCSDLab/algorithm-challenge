# Word Search
---
## 문제 해결 방법
---
2(개선)
* 보드 포인터 사용
* string_view
* 문자 빈도수 확인
*  visited 대신 보드의 문자 변경
* static const로 dirs 선언
## 알게 된 것
---
* string_view
  * 포인터와 길이만을 저장하기 때문에 가볍다.
* 그래프는 너무 어려워~ 생각해야 할 게 많네요
* 빈도수 확인은 진짜 전혀 생각 못 했는데
*  ai 대박... 나는 멍청이...

## 코드
```cpp
class Solution {
 private:
  vector<vector<char>> board;
  string word;
  int m, n;
  vector<vector<bool>> visited;

  bool dfs(int index, int y, int x) {
    if (index == word.length()) {
      return true;
    }

    if (y < 0 || y >= m || x < 0 || x >= n || visited[y][x] || board[y][x] != word[index]) {
      return false;
    }

    visited[y][x] = true;

    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (auto [dy, dx] : directions) {
      if (dfs(index + 1, y + dy, x + dx)) {
        return true;
      }
    }

    visited[y][x] = false;
    return false;
  }

 public:
  bool exist(vector<vector<char>>& board, string word) {
    this->board = board;
    this->word = word;
    m = board.size();
    n = board[0].size();
    visited = vector<vector<bool>>(m, vector<bool>(n, false));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (dfs(0, i, j)) {
          return true;
        }
      }
    }
    return false;
  }
};

///

class Solution {
 private:
  int m, n;
  int wordLength;
  vector<vector<char>>* boardPtr;
  string_view wordView;

  bool dfs(int index, int y, int x) {
    if (index == wordLength) return true;

    if (y < 0 || y >= m || x < 0 || x >= n || (*boardPtr)[y][x] != wordView[index]) return false;

    char temp = (*boardPtr)[y][x];
    (*boardPtr)[y][x] = '#';

    static const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (const auto& [dy, dx] : dirs) {
      if (dfs(index + 1, y + dy, x + dx)) return true;
    }

    (*boardPtr)[y][x] = temp;
    return false;
  }

 public:
  bool exist(vector<vector<char>>& board, string word) {
    m = board.size();
    n = board[0].size();
    wordLength = word.length();
    boardPtr = &board;
    wordView = word;

    vector<int> charCount(128, 0);
    for (char c : word) charCount[c]++;

    for (const auto& row : board) {
      for (char c : row) {
        if (--charCount[c] <= 0) charCount[c] = 0;
      }
    }

    for (char c : word) {
      if (charCount[c] > 0) return false;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (dfs(0, i, j)) return true;
      }
    }
    return false;
  }
};

```
