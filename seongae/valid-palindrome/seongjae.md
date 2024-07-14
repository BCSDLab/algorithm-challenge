# 첫시도

# Intuition
주어진 문자열이 회문인지 확인하기 위해 문자열의 비알파벳 문자를 제거하고, 남은 문자를 소문자로 변환한 후 비교

# Approach
1. 정규 표현식을 사용하여 문자열에서 모든 비알파벳 문자를 제거
2. 문자열을 소문자로 변환
3. 문자열의 처음과 끝에서부터 중앙으로 이동하면서 문자를 비교
4. 만약 어느 한 쌍이라도 다르다면 false를 반환
5. 끝까지 확인한 후에도 다르지 않다면 true를 반환

# Complexity
- Time complexity: `O(n)`
  - 문자열을 한 번 순회하여 비알파벳 문자를 제거하고 한 번 더 순회하여 회문을 확인하므로 O(n)
- Space complexity: `O(n)`
  - 정규 표현식을 사용하여 새로운 문자열을 생성하므로 O(n)

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 16ms
Memory Usage: 44.75 MB

```java
public class ValidPalindrome125 {
    public boolean isPalindrome(String s) {
        String match = "[^\uAC00-\uD7A30-9a-zA-Z]";
        s = s.replaceAll(match, "").toLowerCase();
        int length = s.length() - 1;
        for(int i = 0; i <= length; i++) {
            if (!(s.charAt(i) == s.charAt(length-i)))
                return false;
        }
        return true;
    }
}
```

# Learned
replace되는 과정에서 시간을 잡아 먹어 비효율 적일 수 있따는 것을 배웠다

# 두번째 시도
# Intuition
문자열의 양 끝에서부터 중앙으로 이동하면서 알파벳 또는 숫자만 비교하여 회문을 확인

# Approach
1. 문자열의 왼쪽 포인터와 오른쪽 포인터를 설정합니다.
2. 양 포인터가 만날 때까지 반복

# Complexity
- Time complexity: `O(n)`
    - 입력 배열을 순회하는 비용 `O(n)`
- Space complexity: `O(1)`
    - 추가 적인 배열을 사용하지 않으므로 `O(1)`

# Code
시간복잡도: `O(n)`
공간복잡도: `O(1)`
Runtime: 2 ms
Memory Usage: 42.52 MB
```java
public class ValidPalindrome125 {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
```

# Learned
문자열을 양 끝에서부터 중앙으로 이동하면서 알파벳 또는 숫자만 비교하여 회문을 확인하는 효율적인 방법을 배웠다.
