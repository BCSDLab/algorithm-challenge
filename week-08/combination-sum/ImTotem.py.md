# Intuition

평범한 백트래킹 문제다.

# Approach

1. 숫자들을 정렬한다.
2. 백트래킹으로 조합을 찾는다.
3. 각 재귀 호출에서:
	- 목표 값이 0이 되면 현재 조합을 결과에 추가한다.
	- 현재 인덱스부터 시작하여 가능한 모든 후보 숫자를 시도한다.
	- 숫자가 현재 목표보다 크면 반복을 중단한다.

# Complexity
- Time complexity: $$O(2^N)$$

- Space complexity: $$O(T)$$
	- T는 목표 값(target)
	- 재귀 호출의 최대 깊이는 `target/min(candidates)`

# Code
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        n = len(candidates)
        ans = []
        
        stack = []
        def dfs(target, idx):
            if target == 0:
                ans.append(stack[:])
                
            for i in range(idx, n):
                if candidates[i] > target: break
                
                stack.append(candidates[i])
                dfs(target - candidates[i], i)
                stack.pop()

        dfs(target, 0)

        return ans
```

