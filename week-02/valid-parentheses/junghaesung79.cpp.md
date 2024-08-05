# Valid Parentheses
---
## 문제 해결 방법
---
* check 함수를 선언한다.
  * 여는 괄호이면 스택에 push한다.
  * 닫는 괄호이면 스택의 top을 검사하고 서로 짝이 맞는 여부에 따라 불리언 값을 반환한다.
* s를 순환하며 check함수를 호출한다.
* 루프를 빠져나왔을 때 empty 인지 확인하고 그 결과를 반환한다.
## 자료구조 선택
---
* stack
## 성능
---
* O(n) / O(n)
## 알게 된 것
---
* 
## 코드
```cpp
class Solution {
 private:
  bool check(char c, stack<char>& s) {
    if (c == '(' || c == '{' || c == '[') {
      s.push(c);
      return true;
    } else if (!s.empty()) {
      if ((s.top() == '(' && c == ')') ||
          (s.top() == '{' && c == '}') ||
          (s.top() == '[' && c == ']')) {
        s.pop();
        return true;
      }
    }

    return false;
  }

 public:
  bool isValid(string s) {
    unordered_set<char> brackets = {'(', '{', '[', ')', '}', ']'};
    stack<char> bracket_stack;
    for (char c : s) {
      if (brackets.find(c) != brackets.end()) {
        if (!check(c, bracket_stack)) {
          return false;
        }
      }
    }

    return bracket_stack.empty();
  }
};
```