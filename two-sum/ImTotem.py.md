# Intuition
 
 정렬 후 투 포인터 기법을 사용하여 두 수의 합이 target이 되는 인덱스 쌍을 찾는다.
# Approach

1. (value, index) 쌍으로 정렬한다.
2. 양 끝에 포인터 설정를 설정한다. (l, r)
3. 포인터가 가리키는 값들의 합이 target과 일치할 때까지 포인터 이동한다.
4. 일치하는 쌍을 찾으면 원래 인덱스 반환한다.

# Complexity
- Time complexity: $O(n\ log(n))$

- Space complexity: $O(n\ log(n))$

# Code
```python
def twoSum(nums: List[int], target: int) -> List[int]:
    nums = sorted((v, i) for i, v in enumerate(nums))
    
    l, r = 0, len(nums)-1
    while (s:=nums[l][0] + nums[r][0]) != target:
        if s < target:
            l += 1
        else:
            r -= 1

    return [nums[l][1], nums[r][1]]

with open("user.out", "w") as f:
    cases = list(map(loads, stdin))
    for i in range(0, len(cases), 2):
        f.write(f"{str(twoSum(cases[i], cases[i+1])).lower()}\n")
exit()
```