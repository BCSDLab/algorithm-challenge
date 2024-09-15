# Intuition
투 포인터로 해결할 수 있는 문제이다.

# Approach
1. set을 이용해서 중복된 문자를 체크한다.
2. 만약 이미 존재하는 문자인 경우 low에 있는 문자를 지운 뒤 포인터를 옮겨준다.
3. 존재하지 않는다면 set에 넣고 오른쪽 포인터를 하나 옮기고 max를 업데이트한다.

# Complexity
- Time complexity: $O(N)$
    - 한번만 순회하기 때문에 $O(N)$

- Space complexity: $O(1)$
    - 별도의 추가공간을 사용하지 않기 때문에 $O(1)$

# Code
```java []
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>(s.length());
        int l = 0, h = 0, ret = 0;
        while(h < s.length()) {
            if (set.contains(s.charAt(h))) set.remove(s.charAt(l++));
            else {
                set.add(s.charAt(h++));
                ret = Math.max(ret, h - l);
            }
        }
        return ret;
    }
}
```

# Learned
투포인터 트레이닝 하는중.. 해도해도 아이디어는 생각나는데 구현능력이 부족한듯. 투포인터 문제를 많이 풀어보면 해결될 문제라고 생각