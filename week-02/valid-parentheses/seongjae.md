# Intuition
스택으로 괄호의 유효성을 검사한다.

# Approach
1. 여는 괄호일 경우 push
2. 닫는 괄호일 경우 pop 비어있으면 false 반환

# Complexity
- Time complexity: O(n)
각 문자를 한번씩 처리한다.
- Space complexity: 
최악의 경우 스택에 모든 여는 괄호가 쌓일 수 있다.

# Code
Runtime: 1ms Memory Usage: 41.31MB
```java
/**
 public class ListNode {
 int val;
 ListNode next;
 ListNode() {}
 ListNode(int val) { this.val = val; }
 ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 */
public class ValidParentheses20 {
    public boolean isValid(String s) {
        char[] sArr = s.toCharArray();
        Stack<Character> stack = new Stack<>();

        for (char c : sArr) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

# Learned
