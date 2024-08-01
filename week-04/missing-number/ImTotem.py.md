# Intuition

수열의 전체 합 - 주어진 배열의 모든 숫자의 합

# Approach

1. 수열의 합 $=\sum\limits_{k=0}^{n}{k} = \dfrac{n(n+1)}{2}$
2. 주어진 배열의 모든 숫자의 합을 계산한다.
3. 둘의 차를 구한다.

# Complexity
- Time complexity: $$O(N)$$

- Space complexity: $$O(1)$$

# Code
```python
def missingNumber(nums: List[int]) -> int:
    return (len(nums) * (len(nums)+1) // 2) - sum(nums)

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{missingNumber(case)}\n")
exit(0)
```

