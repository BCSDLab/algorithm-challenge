# Intuition

각 단어의 개수를 키로 사용하여 그룹화한다.

# Approach

1. defaultdict를 사용하여 키가 없을 때 자동으로 빈 리스트를 생성한다.
2. 각 단어를 순회하면서:
	- 26개의 알파벳에 대한 빈도수 배열(key)을 생성한다.
	- 단어의 각 문자에 대해 해당 알파벳의 빈도수를 증가시킨다.
	- 빈도수 배열을 튜플로 변환하여 키로 사용한다.
	- 원래 단어를 해당 키의 리스트에 추가한다.
3. defaultdict의 값들(각 그룹)을 반환한다.

# Complexity
- Time complexity: $$O(N\times M)$$
	- N은 단어의 개수, M은 가장 긴 단어의 길이

- Space complexity: $$O(N \times M)$$

# Code
```python
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for i in strs:
        key = [0] * 26
		for c in i:
			key[ord(c) - ord('a')] += 1
		
		ans[tuple(key)].append(i)
    
    return ans.values()

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{list(groupAnagrams(case))}\n".replace("'", '"'))
exit(0)
```

