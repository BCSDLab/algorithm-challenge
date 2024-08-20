# Intuition
슬라이딩 윈도우로 접근하는 것은 이해했지만, 조건을 어떻게 잡아할지 몰라 알고달래를 참고하였다.

# Approach
1. 문자열의 개수를 저장할 count를 선언한다.
2. 가장 빈도수가 높은 문자를 maxCount에 갱신한다.
3. 현재 윈도우 길이에서 빈도수가 높은 문제를 제외한 나머지 문자의 수가 k보다 크면,
   윈도우 길이를 오른쪽으로 이동시키고, 오른쪽 문자의 빈도도 줄인다.
4. 반복문을 통해 최대 길이를 갱신한다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(1)$ (상수 공간)

# Code
```js
var characterReplacement = function(s, k) {
    const count = {};
    let maxLen = 0, maxCount = 0, start = 0;

    for(let end = 0; end < s.length; end++) {
        let char = s[end];
        count[char] = (count[char] || 0) + 1;
        maxCount = Math.max(maxCount, count[char]);
        
        if ((end - start + 1) - maxCount > k) {
            count[s[start]]--;
            start++;
        }
        
        maxLen = Math.max(maxLen, end - start + 1);
    }

    return maxLen;
};
```