# Intuition
빈 문자열일 때 결괏값이 다른 것을 확인하여 '문자열 길이'+'특수문자'의 형태로 변환한다는 풀이를 참고하였다.

# Approach
1. '#'을 구분자로 활용함과 동시에 문자열 길이를 인코딩 결과에 기록해 놓는다.
2. '#'과 문자열 길이를 제외한 문자열을 디코딩한다.

# Code
```js
class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = '';
        for(let s of strs) {
            encoded += s.length + '#' + s;
        }

        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let decoded = [];
        let i = 0;
        while(i < str.length) {
            let j = i;
            while(str[j] !== '#') {
                j++;
            }
            let length = parseInt(str.slice(i,j), 10);
            i = j + 1;
            decoded.push(str.slice(i,i+length));

            i+=length;
        }
        return decoded;
    }
}

```