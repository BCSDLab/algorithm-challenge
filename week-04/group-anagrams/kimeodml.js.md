# Intuition

동일한 문자를 그룹화하기 -> Map 활용

# Approach
1. 각각의 문제를 알파벳 순으로 정렬
2. 정렬된 문자열을 키로 사용하여 그룹화 진행
  2.1. 키가 존재하지 않으면 새로운 키로 등록하고
  2.2. 키가 존재하면 map에서 등록된 키의 배열에 값을 추가
3. map의 value 값만 출력

# Complexity
- Time complexity: $$O(n*klogk)$$
  - n은 문자열의 개수, k는 문자열의 최대 길이
- Space complexity: $$O(n*k)$$
  - n은 문자열의 개수, k는 문자열의 최대 길이

# Code
```js
var groupAnagrams = function(strs) {
    const map = new Map();
    strs.forEach((str)=> {
        const 정렬 = str.split('').sort().join('');
        if(!map.has(정렬)) {
            map.set(정렬,[]);
        }
        map.get(정렬).push(str);
    })
    return Array.from(map.values());
};
```