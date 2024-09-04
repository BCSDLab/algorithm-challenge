# Intuition

Trie 자료구조가 뭔지 몰라서 찾아봤다. 뭔지 알고나니까 쉬운거 같다.

# Approach

1. 초기화 (`__init__`):
	- 루트 노드를 빈 딕셔너리로 초기화한다.
2. 삽입 (`insert`):
	- 단어의 각 문자를 트리에 순차적으로 추가한다.
	- 각 문자는 딕셔너리의 키로 표현된다.
	- 단어의 끝을 표시하기 위해 특별한 키 ';'를 사용한다.
3. 검색 (`search`):
	- 주어진 단어의 각 문자를 트리에서 순차적으로 찾는다.
	- 모든 문자를 찾고 마지막에 ';' 키가 있으면 단어가 존재하는 것이다.
4. 접두사 검색 (`startsWith`):
	- 주어진 접두사의 각 문자를 트리에서 순차적으로 찾는다.
	- 모든 문자를 찾을 수 있으면 해당 접두사로 시작하는 단어가 존재하는 것이다.

# Complexity
- Time complexity:
	- Insert: $$O(N)$$
	- Search: $$O(N)$$
	- N은 단어의 길이


- Space complexity:
	- Insert: $$O(N)$$
	- Search: $$O(1)$$
	- N은 단어의 길이

# Code
```python
class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        head = self.root

        for c in word:
            if c not in head:
                head[c] = dict()
            
            head = head[c]
        
        head[';'] = None

    def search(self, word: str) -> bool:
        head = self.root

        for c in word:
            if c not in head:
                return False
            head = head[c]
        
        return ';' in head

    def startsWith(self, prefix: str) -> bool:
        head = self.root

        for c in prefix:
            if c not in head:
                return False
            
            head = head[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

