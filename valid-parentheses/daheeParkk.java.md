# Intuition
열린 괄호를 stack에 넣고 닫힌 괄호가 오면 stack에서 꺼낸 후 비교한다.

# Approach
```java
1. 문자 s 한글자씩 for문을 돌리며 확인한다.
2. 열린 괄호일 경우 stack에 넣는다.
3. 닫힌 괄호일 경우 stack이 비어있거나 stack에서 꺼낸 괄호가 짝이 맞는 괄호가 아니라면 false를 반환한다.
4. for문을 다 돌았을 때 stack에 괄호가 남아있으면 false, 비어있으면 true를 반환한다.
```

# Complexity
- Time complexity:
  O(n)

- Space complexity:
  O(n)

# Code
```java
class Solution {
    public boolean isValid(String s) {
       String[] brackets = s.split("");
       Stack<String> stack = new Stack<>();

       for (String bracket: brackets) {
            if (isOpenBracket(bracket)) {
                stack.push(bracket);
            } else {
                if (stack.isEmpty() || !isSameBracket(stack.pop(), bracket)) {
                    return false;
                }
            }
       }

       if (!stack.isEmpty()) {
            return false;
       }
       return true;
    }

    public boolean isOpenBracket(String bracket) {
        return bracket.equals("(") || bracket.equals("{") || bracket.equals("[");
    }

    public boolean isSameBracket(String openBracket, String closeBracket) {
        return (openBracket.equals("(")&&closeBracket.equals(")")) || (openBracket.equals("{")&&closeBracket.equals("}")) || (openBracket.equals("[")&&closeBracket.equals("]"));
    }
}
```
