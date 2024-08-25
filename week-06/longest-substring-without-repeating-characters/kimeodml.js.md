# Intuition
연속된 부분 문자열 + 중복 X -> 슬라이딩 윈도우 + Set

# Approach
1. 슬라이딩 윈도우의 왼쪽 경계를 0으로 초기화한다.
2. 반복문을 통해 슬라이딩 윈도우의 오른쪽 경계를 증가한다.
3. 이때 해당 set에 존재하면(중복 O) 기존 슬라이드에서 제거하고, 왼쪽 경계를 오른쪽으로 이동한다.
4. 존재하지 않는다면(중복 X) set에 추가한다.
5. 최대 길이를 갱신한다.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```js
var lengthOfLongestSubstring = function(s) {
    let left = 0;
    let maxLength = 0;
    let set = new Set();
    for(let right = 0;right < s.length;right++) {
        while(set.has(s[right])) {
            set.delete(s[left]);
            left++;
        }
        set.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
};
```