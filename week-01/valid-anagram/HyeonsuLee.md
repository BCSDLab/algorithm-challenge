# Intuition
빈도수배열을 이용해서 두 문자의 빈도수를 비교한다.

# Approach
1. 두 문자열에 대한 빈도수 배열을 생성한다.
2. 각각의 문자열에 대한 빈도수를 반복문을 이용하여 계산한다.
3. 두 문자열의 빈도수 배열을 순회하여 같은지 확인한다.
    - 빈도수가 다른 요소가 있다면 `false`

# Complexity
- Time complexity: `O(n)`
    - 문자열의 길이 n
    - 문자열이 2개이기 때문에 2n 따라서 `O(n)`
- Space complexity: `O(1)`
    - 영문 소문자의 빈도수 배열 2개의 공간은 52개이다.
    - 따라서 공간복잡도는 `O(1)`

# Code
시간복잡도: `O(n)`
공간복잡도: `O(1)`
Runtime: 1 ms
Memory Usage: 42.9 MB
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char[] freqS = new char[26];
        char[] freqT = new char[26];
        for (char c: s.toCharArray()) ++freqS[c - 'a'];
        for (char c: t.toCharArray()) ++freqT[c - 'a'];
        for (int i = 0; i < 26; ++i) {
            if (freqS[i] != freqT[i]) return false;
        }
        return true;
    }
}
```

# Learned
처음 제출했을 때에는 조기 종료 조건을 넣지 않아서 2ms가 걸렸지만, 조기 종료 조건을 넣고 난 뒤 1ms로 줄었다.
따라서 조기 종료 조건의 중요성을 배웠다.