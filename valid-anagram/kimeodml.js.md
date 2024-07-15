# Intuition

정렬을 통해 값이 일치하는지 비교

# Approach

1. 길이가 다르면 false
2. 문자열 정렬을 통해 일치하면 true, 다르면 false를 반환

# Complexity

- 시간복잡도: O(nlogn)
- 공간복잡도: O(n)

# 알게 된 것

- 항상 써 오던 자바스크립트의 sort()가 insertion sort와 merge sort를 결합하여 만든 time sort라는 것을 알게 됨 -> O(nlogn)

# Code
```js
var isAnagram = function(s, t) {
    if(s.length != t.length) return false;

    let newS = s.split('').sort().join('');
    let newT = t.split('').sort().join('');
    if(newS === newT) return true;
    else return false;
};
```