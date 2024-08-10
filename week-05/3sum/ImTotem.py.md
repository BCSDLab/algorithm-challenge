# Intuition

비슷한 문제에 여러번 당했던 기억이 있다.
배열을 정렬한 후 한 수를 고정하고 나머지 두 수를 투 포인터 방식으로 찾는다.

# Approach

1. 배열을 오름차순으로 정렬한다.
2. 첫 번째 수(i)를 고정하고 순회한다.
3. 두 번째(j)와 세 번째(k) 수를 찾기 위해 i+1부터 배열의 끝까지 투 포인터를 사용한다.
4. 세 수의 합이 0이면 결과에 추가하고, 중복을 피하기 위해 j와 k를 이동시킨다.
5. 합이 0보다 작으면 j를 증가시키고, 크면 k를 감소시킨다.
6. 중복된 결과를 피하기 위해 같은 수는 건너뛴다.

# Complexity
- Time complexity: $$O(N^2)$$

- Space complexity: $$O(N)$$

# Code
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, n - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    
                    while j < k and nums[k] == nums[k + 1]: k -= 1
                elif s < 0: j += 1
                else: k -= 1
                    
        return ans
```

