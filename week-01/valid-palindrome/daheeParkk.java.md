# Intuition
문자에서 알파벳과 숫자를 제외한 나머지는 없애고, 소문자로 바꾼다.
알파벳의 앞에서부터 뒤에와 비교한다.

# Approach
```java
1. 주어진 문자에서 알파벳과 숫자가 아니면 제거하고, 소문자로 바꾼다.
2. 바뀐 문자의 절반만큼 for문을 돌아 앞글자와 뒷글자를 비교한다.
3. 앞글자와 뒷글자가 다르면 false를 반환하고 마지막에 true를 반환한다.
```

# Code
```java
class Solution {
    public boolean isPalindrome(String s) {
        String[] alpha = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase().split("");
        int length = alpha.length;
        int half = length / 2;
        int backIndex = length - 1;

        for (int i=0; i<half; i++) {
            String front = alpha[i];
            String back = alpha[backIndex];
            backIndex--;
            if (!front.equals(back)) {
                return false;
            }
        }
        return true;
    }
}
```
