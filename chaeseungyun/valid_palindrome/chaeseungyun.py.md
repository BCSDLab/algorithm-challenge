# Intuition
주어진 문자열 중에 영어와 숫자만 남겼을 때, 앞,뒤 방향에 상관없이 같은 읽히는지 판단

# Approach
1. 주어진 문자열이 공백이거나, 길이가 1이면 palindrome이므로 True
2. 아스키코드를 통해 숫자, 소문자 영어,. 대문자 영어만 alphanumeric 리스트에 추가한다.
3. 이때 만들어진 리스트의 길이가 0이면 영어와 숫자가 없는 문자인데, 이때 문제에 조건에 따라 문자를 다 지우면 빈 문자열이 되므로 True
4. 만들어진 문자열의 첫 번째와 마지막, 두 번째와 마지막 - 1.. 을 문자열 길이의 절반만큼 비교한다.


# Complexity
- Time complexity: $O(n^2)$
이중 반복분

- Space complexity: $O(n)$
리스트의 크기

# Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s.replace(" ",'')) == 0 or len(s) == 1): return True

        alphanumeric = []

        for char in s:
            if ((ord(char) >= 48 and ord(char) <= 57)):
                alphanumeric.append(char)
                continue
            if ((ord(char) >= 65 and ord(char) <= 90)):
                alphanumeric.append(char.lower())
                continue
            if ((ord(char) >= 97 and ord(char) <= 122)):
                alphanumeric.append(char)

        if len(alphanumeric) == 0: return True
        
        length = len(alphanumeric)
        for i in range(length):
            if (i > length // 2): break
            if (alphanumeric[i] != alphanumeric[length - i - 1]): return False
        
        return True
```
# Learned
isalnum() 이라는 메소드가 있었다. 숫자인지 영어인지 판별해준다고 한다..
isalnum()을 사용했다면 조건문의 길이가 훨씬 짧아졌을 것이다.

# 여담
-