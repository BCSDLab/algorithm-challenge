# Intuition

 슬라이딩 윈도우를 사용한다. 문자의 마지막 등장 위치를 추적하면서 윈도우의 크기를 조절한다.

# Approach

1. 두 개의 포인터 l(left)과 r(right)를 사용하여 슬라이딩 윈도우를 관리한다.
2. chars 배열을 사용하여 각 문자의 마지막 등장 위치를 추적한다.
3. 오른쪽 포인터 r을 이동시키면서:
	- 현재 문자의 이전 등장 위치를 확인한다.
	- 이전 등장 위치가 현재 윈도우 내에 있다면, 왼쪽 포인터 l을 해당 위치 다음으로 이동시킨다.
	- 현재 윈도우의 크기(r - l + 1)와 지금까지의 최대 길이 ans를 비교하여 갱신한다.
	- 현재 문자의 위치를 chars 배열에 기록한다.
1. 최종적으로 가장 긴 부분 문자열의 길이 ans를 반환한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        chars = [-1] * 128
        
        l = 0
        for r, char in enumerate(s):
            idx = chars[ord(char)]

            if -1 < idx and l <= idx < r:
                l = idx + 1
            
            ans = max(ans, r - l + 1)

            chars[ord(char)] = r
        
        return ans

```

