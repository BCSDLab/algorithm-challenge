# Intuition

스택을 활용해 괄호들을 비교 후 pop하거나 push함

# Approach

1. 빈 배열 arr 생성
2. 여는 괄호일 경우 arr에 push
3. 닫는 괄호일 경우
  3.1. 이때 arr이 비어 있을 경우 false로 반환
  3.2. 가장 맨 위의 prev와 닫는 괄호를 비교하여 올바르면 괄호 제거 그렇지 않으면  false로 반환
3. arr이 비어있으면 true 그렇지 않을 경우 false로 반환


# Complexity

- 시간복잡도: O(n)
- 공간복잡도: O(n)

# Code
```js
var isValid = function(s) {
    let arr = [];
    for (let char of s) {
        if (char === '(' || char === '[' || char === '{') {
            arr.push(char);
        } else if (char === ')' || char === ']' || char === '}') {
            if (arr.length === 0) {
                return false;
            }
            let prev = arr[arr.length - 1];
            if ((char === ']' && prev === '[') || 
                (char === ')' && prev === '(') || 
                (char === '}' && prev === '{')) {
                arr.pop();
            } else {
                return false;
            }
        }
    }
    return arr.length === 0;
};
```