# Intuition

set을 이용해 중복을 제거한 후의 길이와, 리스트의 길이를 비교하여 중복을 검사한다.

# Approach

1. 입력값으로 집합을 생성한다.
2. 집합의 길이와 입력값의 길이를 비교한다.
3. 둘의 길이가 다르다면, 중복이 있다는 것이므로 true를 반환한다.
4. 둘의 길이가 같다면, 중복이 없다는 것이므로 false를 반환한다.

# Complexity

- Time complexity: $O(n)$  
- Space complexity: $O(n)$

# Code

```python
def containsDuplicate(nums: List[int]) -> bool:
	return len(nums) != len(set(nums))

with open("user.out", "w") as f:
	for case in map(loads, stdin):
	f.write(f"{str(containsDuplicate(case)).lower()}\n")

exit()
```