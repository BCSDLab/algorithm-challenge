# Encode and Decode Strings
---
## 문제 해결 방법
---
* 단어마다 단어의 길이와 특수문자, 단어를 조합하여 인코딩한다.
* 단어 길이 숫자와 특수문자를 만나서 그것을 제외한 후 백터로 만든다.
## 성능
---
* O(n) / O(n)
## 알게 된 것
---
* 알고달래 풀이에서 문제의 조건을 이해하고 이모지를 이용해서 푸는 것이 인상깊었다.

# 코드
```cpp
class Solution {
 public:
  /*
   * @param strs: a list of strings
   * @return: encodes a list of strings to a single string.
   */
  string encode(vector<string> &strs) {
    string result;
    for (string &s : strs) {
      result += to_string(s.size()) + "^" + s;
    }

    return result;
  }

  /*
   * @param str: A string
   * @return: decodes a single string to a list of strings
   */
  vector<string> decode(string &str) {
    vector<string> result;
    int i = 0;
    while (i < str.length()) {
      int j = i;
      while (str[j] != '#') j++;
      int len = stoi(str.substr(i, j - i));
      string s = str.substr(j + 1, len);
      result.push_back(s);
      i = j + 1 + len;
    }

    return result;
  }
};
```