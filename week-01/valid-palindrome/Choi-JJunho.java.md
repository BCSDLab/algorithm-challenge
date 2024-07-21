# Intuition

좌측, 우측을 가리키는 포인터를 두고 하나씩 비교해온다.

# Approach

1. 왼쪽 인덱스부터 시작하는 left와 오른쪽 인덱스부터 시작하는 right를 선언한다.
2. left, right 두 값이 일치하거나 left < right 가 되는 시점까지 반복한다.
  2.1. 알파벳 혹은 숫자가 아니면 left, right는 계속해서 넘어간다.
  2.2. 만약 알파벳 혹은 숫자를 만난다면 두 값을 비교하여 같은 알파벳/숫자가 아니라면 false를 반환한다.
3. 위 상황에서 반환되지 않는 경우 true를 반환한다.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```java
class Solution {
    public boolean isPalindrome(String s) {
        char[] letters = s.toCharArray();
        int left = 0;
        int right = letters.length - 1;
        while(left != right && left < right) {
            while (!isAlphabetOrNumber(letters[left]) && left < right) {
                left++;
            }
            while (!isAlphabetOrNumber(letters[right]) && left < right) {
                right--;
            }
            
            if (toLowerCase(letters[left]) != toLowerCase(letters[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private boolean isAlphabetOrNumber(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
    }


    private int toLowerCase(char c) {
        if (c >= 'a' && c <= 'z') {
            return c - 'a' + 'A';
        }

        return c;
    }
}
```
