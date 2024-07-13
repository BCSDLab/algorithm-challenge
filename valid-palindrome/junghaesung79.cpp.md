## Valid Palindrome
---
## 문제 해결 방법
---
* 1
  * 문자열의 양쪽 끝에서 시작해서 한 문자씩 확인한다.
  * 문자가 아닐 경우 그 문자를 건너 뛴다.
## 자료구조 선택
---
## 성능
---
* 문자열 탐색 O(n)
* 저장x O(1)
* O(n) / O(1)
## 알게 된 것
---
# Code

```cpp class Solution {
 private:
  char normalize(char c) {
    if (std::isalpha(c)) {
      return std::tolower(c);
    } else if (std::isdigit(c)) {
      return c;
    } else {
      return 0;
    }
  }

 public:
  bool isPalindrome(string s) {
    int left = 0;
    int right = s.size() - 1;

    while (left < right) {
      char leftChar = normalize(s[left]);
      char rightChar = normalize(s[right]);

      if (leftChar == 0) {
        left++;
        continue;
      }
      if (rightChar == 0) {
        right--;
        continue;
      }

      if (leftChar != rightChar) {
        s return false;
      }

      left++;
      right--;
    }

    return true;
  }
};

```