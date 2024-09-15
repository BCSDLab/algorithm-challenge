# Intuition
트라이(Trie) 자료구조를 구현하는 문제이다.

# Approach
1. 트라이(Trie)는 각 노드가 26개의 자식을 가지며, 알파벳 소문자에 해당하는 배열로 자식 노드를 관리한다.
2. insert 메서드는 문자열을 순차적으로 노드를 따라가면서 새로운 문자가 나오면 해당 위치에 새 노드를 생성하여 단어를 저장한다.
3. search 메서드는 주어진 단어가 트라이에 존재하는지 확인하며, 끝까지 도달하고 isEndOfWord가 true인 경우 단어가 존재한다고 판단한다.
4. startsWith 메서드는 주어진 접두사가 트라이에 존재하는지 확인하며, 접두사까지만 일치하면 true를 반환한다.

# Complexity
- Time complexity: $O(M)$
    - m은 입력 문자열의 길이로, 문자열을 삽입하거나 검색하는 데 문자열 길이에 비례하는 시간이 소요된다.

- Space complexity: $O(NM)$
    - n은 삽입된 문자열의 개수, m은 문자열의 평균 길이로, 각 문자마다 새로운 노드를 생성할 수 있다.

# Code
```java []
class Trie {

    class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;

        public TrieNode() {
            children = new TrieNode[26];
            isEndOfWord = false;
        }
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private TrieNode searchPrefix(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return null;
            }
            node = node.children[index];
        }
        return node;
    }
}

```

# Learned
Trie자료구조에 대해 공부할 수 있었다.