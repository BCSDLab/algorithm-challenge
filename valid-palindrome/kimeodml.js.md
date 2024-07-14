# Intuition

알파벳을 소문자로 변환 후, 숫자와 알파벳만 남김
뒤집어서 동일한지 비교

# Approach

1. 문자를 소문자로 변환
2. 알파벳, 숫자만 포함한 새로운 문자열로 변환
3. 뒤집어서 기존 문자열과 비교
4. 동일하면 true, 다르면 false 반환

# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var isPalindrome = function(s) {
    let letter = s.toLowerCase();
    let newLetter = '';
    for(let i = 0; i < letter.length;i++) {
        if((letter[i] >= 'a' && letter[i] <='z') || letter[i] >= '0' && letter[i] <='9') {
            newLetter += letter[i];
        }
    }
    if(newLetter === newLetter.split('').reverse().join('')) {
        return true;
    }else {
        return false;
    }
};
```