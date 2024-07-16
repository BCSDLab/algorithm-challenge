# Intuition
영문, 숫자를 제외한 모든 문자를 제거하고 반복문을 통해 팰린드롬인지 검사한다.

# Approach
1. 입력 문자열 S에서 영문, 숫자를 새로운 문자 배열에 할당한다.
    - 이때 대문자의 경우 문자코드를 이용해 소문자로 변환한다.
2. 영문, 숫자로만 구성된 문자배열을 반복문을 통해 순회하여 팰린드롬인지 검사한다.
    - left, right인덱스를 통해 양쪽에서 한칸씩 땡기며 검사한다.


# Complexity
- Time complexity: `O(n)`
    - 입력 문자열에서 영문, 숫자만 남기는 비용 `O(n)`
    - 팰린드롬을 검사하는 비용 `O(n/2)`
    - 총 시간복잡도 `O(n)`
- Space complexity: `O(n)`
    - 새로운 문자 배열을 만들어서 알파벳, 숫자를 보관하기 때문에 `O(n)`

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 2 ms
Memory Usage: 43.5 MB
```java
class Solution {
    public boolean isPalindrome(String s) {
        char[] origin = s.toCharArray();
        char[] letters = new char[s.length()];
        int index = 0;
        for (char letter: origin) {
            if (isAlphaNumber(letter)) {
                letters[index++] = (letter >= 'A' && letter <= 'Z')? (char) (letter - ('A' - 'a')): letter;
            }
        }
        int left = 0;
        int right = index - 1;
        while(left < right) {
            if (letters[left] != letters[right]) return false;
            ++left; --right;
        }
        return true;
    }

    private boolean isAlphaNumber(char alphaNumber) {
        return (
            (alphaNumber >= 'a' && alphaNumber <= 'z') || (alphaNumber >= 'A' && alphaNumber <= 'Z') ||
            (alphaNumber >= '0' && alphaNumber <= '9')
        );
    } 
}
```

# Learned
범위 검사, 유효성 검사를 모듈화 하면 조금 더 깔끔하게 알고리즘을 작성할 수 있다는 것을 배웠다.