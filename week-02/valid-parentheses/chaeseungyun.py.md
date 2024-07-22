# Intuition
스택을 이용하여 이전에 등장한 여는 괄호를 판단한다.

# Approach
<!-- Describe your approach to solving the problem. -->
1. 자료구조 시간에 배운 내용을 떠올리며 스택을 사용했다.
2. 파이썬 리스트를 스택처럼 사용했다.
3. 여는 괄호는 스택에 넣고, 닫는 괄호가 나오면 스택에서 꺼내서 괄호 검사를 한다.
4. 괄호가 맞지 않거나 남는다면 False, 그 외에 True
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
(n은 문자열의 길이)
# Code
```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        capacity = -1

        for item in s:
            if (item == '(' or item == '{' or item == '['):
                stack.append(item)
                capacity += 1
            if (item == ')' or item == '}' or item == ']'):
                if (capacity == -1):
                    return False
            if (item == ')'):
                capacity -= 1
                if (stack.pop() != '('):
                    return False
            if (item == '}'):
                capacity -= 1
                if (stack.pop() != '{'):
                    return False
            if (item == ']'):
                capacity -= 1
                if (stack.pop() != '['):
                    return False

        if (capacity != -1): return False
        return True
```

# Learned
역시 stack 유용하다.