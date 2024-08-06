# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
이진수로 변환 후 1의 개수를 센다
# Approach
<!-- Describe your approach to solving the problem. -->
1. 파이썬의 bin 함수를 통해 이진수 문자열로 변환
2. 반복문을 통해 각 리스트의 1의 개수를 센다

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(n + 1):
            result.append(bin(i).count('1'))
        
        return result
```

# learn
bin()이라는 사기적인 메소드를 배웠다.

bin은 십진수를 이진수의 문자열로 변환해준다.
count(x)는 x가 해당 문자열에서 몇 번 나타났는데 세어준다.

편안하다~