# Intuition
`Stack`에 입력 괄호들중 여는 괄호는 `push`하고, 닫는 괄호일 경우`Stack`의 `Top`은 해당 닫는 괄호의 쌍인 여는 괄호여야 한다.

# Approach
1. 입력 문자열을 순회하면서 여는 괄호일 경우 `Stack`에 넣는다.
2. 닫는 괄호일 경우 `Stack`에서 `pop`한 것이 쌍인지 확인한다.
3. 쌍이 아니라면 `return false`

# Complexity
- Time complexity: $O(N)$
    - 입력 문자열의 길이 N을 순회하는 for문의 비용 → $O(N)$

- Space complexity: $O(N)$
    - `Stack`의 공간 → 입력 문자열의 크기 → $O(N)$

# Code
``` Java
class Solution {
    public boolean isValid(String s) {
        Map<Character, Integer> map = new HashMap<>(10);
        map.put('(', 0); map.put(')', 3);
        map.put('{', 1); map.put('}', 4);
        map.put('[', 2); map.put(']', 5);
        Stack<Character> stack = new Stack<>();
        for (char bracket: s.toCharArray()) {
            if (map.get(bracket) < 3) {
                stack.push(bracket);
            } else {
                if (stack.size() < 1) return false;
                int topBracketIndex = map.get(stack.pop());
                if (map.get(bracket) - 3 != topBracketIndex) return false;
            }
        }
        return stack.size() == 0;
    }
}
```

# Learned
조건을 map으로 인덱싱해서 접근하기 편하게 하는 방법을 배웠다.