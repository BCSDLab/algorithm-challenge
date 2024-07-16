# Intuition

알파벳의 개수를 배열에 기록하면서 그 개수의 차이를 기반으로 anagram임을 판별한다.

# Approach

1. 알파벳 개수를 저장할 배열을 만든다.
2. s 문자열에 대해 각 글자를 순회하며 알파벳 개수를 더한다.
3. t 문자열에 대해 각 글자를 순회하며 알파벳 개수를 뺀다.
  3.1 만약 알파벳 개수가 음수가 된다면 이 문자열은 anagram이 아니므로 false를 반환한다. (주어진 개수보다 여러번 사용하는 경우가 존재함)
4. 알파벳 개수를 저장하는 배열에 남아있는 알파벳이 있다면 해당 수는 anagram이 아니므로 false를 반환한다. (모든 글자를 사용하지 않음)

# Complexity
- 시간복잡도
  - 주어진 문자열들의 길이만큼 순회한다. (s의 길이 + t의 길이 + 26) => O(n)
- 공간복잡도
  - 주어진 문자열을 배열로 변환하면서 차지하는 공간과, 알파벳을 저장하는 공간 (s의 길이 + t의 길이 + 26) => O(n)

# Code
```java
class Solution {

    public boolean isAnagram(String s, String t) {
        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();
        int[] arr = new int[26];
        for (char letter : sChar) {
            arr[letter - 'a']++;
        }
        for (char letter : tChar) {
            if (arr[letter - 'a'] == 0) {
                return false;
            }
            arr[letter - 'a']--;
        }
        for (int remain : arr) {
            if (remain != 0) {
                return false;
            }
        }
        return true;
    }
}
```
