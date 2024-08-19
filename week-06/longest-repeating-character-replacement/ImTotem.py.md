# Intuition

슬라이딩 윈도우를 사용한다. 윈도우 내에서 가장 빈도가 높은 문자를 유지하면서, k개의 문자를 변경하여 만들 수 있는 가장 긴 연속 문자열의 길이를 찾는다.

# Approach

1. 두 개의 포인터 left와 right를 사용하여 슬라이딩 윈도우를 관리한다.
2. right 포인터를 오른쪽으로 이동시키면서 각 문자의 빈도수를 freq 딕셔너리에 기록한다.
3. maxfreq를 통해 윈도우 내에서 가장 높은 빈도수를 추적한다.
4. 현재 윈도우 크기에서 maxfreq를 뺀 값이 k 이하라면, 이 윈도우는 유효하다.
5. 윈도우가 유효하지 않으면 left 포인터를 오른쪽으로 이동시키고, 해당 문자의 빈도수를 감소시킨다.
6. 과정을 반복하며 가장 긴 유효한 윈도우의 길이를 ans에 저장한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$
	- `freq` 딕셔너리는 최대 26개의 알파벳 대문자만을 저장하므로 공간 복잡도는 상수이다.

# Code
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        
        freq = defaultdict(int)
        maxfreq = 0
        
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            maxfreq = max(maxfreq, freq[s[right]])
            
            if (right - left + 1) - maxfreq <= k:
                ans = max(ans, right - left + 1)
            else:
                freq[s[left]] -= 1
                left += 1
        
        return ans

```

