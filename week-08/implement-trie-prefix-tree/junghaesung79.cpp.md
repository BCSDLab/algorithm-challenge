# Implement Trie Prefix Tree
---
## 문제 해결 방법
---
* 알파벳 개수만큼의 nullptr을 가지는 배열을 갖는 노드를 정의한다.
* 생성자: 최초의 TreeNode인 root를 생성한다.
* insert: 주어진 단어를 반복문으로 순회하며 각 char 마다 부모 노드의 알파벳 순서 인덱스에 새로운 노드를 만든다.
* findNode(메서드x): insert 방식처럼 단어를 순회하며 각 노드에 정상적인 값이 들어있는 지 확인한다.
* search, startsWith: findNode를 사용해서 단어가 존재하는 지 확인한다.
## 알게 된 것
---
* 구현 문제 와 진짜 어떻게 풀어야 할 지 모르겠다.
* 난 못 푼다.
* 해설이랑 ai가 푼 거 보고 감탄 밖에 안 나온다.
* 처음 주어진 빈 메서드 코드 보고 진짜 아무 생각이 안 났다.

## 코드
```c++
class TrieNode {
 public:
  TrieNode* children[26];
  bool isEndOfWord;

  TrieNode() {
    for (int i = 0; i < 26; i++) {
      children[i] = nullptr;
    }
    isEndOfWord = false;
  }
};

class Trie {
 private:
  TrieNode* root;

 public:
  Trie() {
    root = new TrieNode();
  }

  void insert(string word) {
    TrieNode* current = root;
    for (char c : word) {
      int index = c - 'a';
      if (current->children[index] == nullptr) {
        current->children[index] = new TrieNode();
      }
      current = current->children[index];
    }
    current->isEndOfWord = true;
  }

  bool search(string word) {
    TrieNode* node = findNode(word);
    return (node != nullptr && node->isEndOfWord);
  }

  bool startsWith(string prefix) {
    return (findNode(prefix) != nullptr);
  }

 private:
  TrieNode* findNode(string& word) {
    TrieNode* current = root;
    for (char c : word) {
      int index = c - 'a';
      if (current->children[index] == nullptr) {
        return nullptr;
      }
      current = current->children[index];
    }
    return current;
  }
};
```
