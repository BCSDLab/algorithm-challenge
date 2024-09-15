# Intuition
슬라이딩 윈도우 기법을 이용해서 해결할 수 있는 문제이다.

# Approach
1. 윈도으의 끝값이 s보다 작을때 동안 while문을 반복한다.
2. 빈도수를 계산하고, 슬라이딩 윈도우기 때문에 가장 긴 문자가 몇개인지 업데이트한다.

# Complexity
- Time complexity: $O(N)$
    - 슬라이딩 윈도우로 전수조사 하기 때문에 $O(N)$

- Space complexity: $O(1)$
    - 빈도수배열의 크기 26이기 때문에 → $O(1)$

# Code
```java []
class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, h = 0, ret = 0, maxFreq = 0;
        int[] freq = new int[26];
        while(h < s.length()) {
            ++freq[s.charAt(h) - 'A'];
            maxFreq = Math.max(maxFreq, freq[s.charAt(h) - 'A']);
            if (h - l + 1 - maxFreq > k) --freq[s.charAt(l++) - 'A'];
            ret = Math.max(ret, h++ - l + 1);
        }
        return ret;
    }
}
```

# Learned
슬라이딩 윈도우의 기본적인 문제만 풀어봤었는데 이렇게도 응용할 수 있다는걸 새롭게 배웠습니다.