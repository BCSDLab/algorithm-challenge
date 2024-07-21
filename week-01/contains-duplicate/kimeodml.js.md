# Intuition

Set을 활용해 중복의 유무를 확인

# Approach

1. 배열을 Set으로 변환하여 중복을 제거
2. 원래 배열의 길이와 Set의 크기를 비교
3. 길이가 같으면 중복이 없다는 의미이고(false), 다르면 중복이 있다는 의미(true)

# Complexity

- 시간복잡도: O(n)
  - 배열의 크기(n)만큼 순회하여 Set을 생성
- 공간복잡도: O(n)
  - 중복 요소가 없을 경우 Set의 크기는 n

# Code
```js
var containsDuplicate = function(nums) {
    let newNum = new Set(nums);

    if(nums.length === newNum.size) return false;
    else return true;
};
```