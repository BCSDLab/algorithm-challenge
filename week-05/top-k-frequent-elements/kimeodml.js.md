# Intuition
빈도수를 계산하여 정렬한 후, k까지 추출한다.

# Approach
1. Map을 활용해 각 요소의 빈도수를 계산한다.
2. 빈도수를 내림차순으로 정렬한다.
3. k값까지의 키값을 추출한다.


# Complexity
- Time complexity: $$O(nlogn)$$
 - 정렬로 인한 시간 복잡도 nlogn
- Space complexity: $$O(n)$$
 - 문자열 nums의 길이 n
	
# Code
```js
var topKFrequent = function(nums, k) {
    let map = new Map();
    nums.forEach((num)=> {
        if(!map.has(num)) {
            map.set(num,[]);
        }
        map.get(num).push(num);
    });

    let sorted = Array.from(map.entries()).sort((a,b)=> b[1].length - a[1].length);
    return sorted.map((num) => num[0]).slice(0,k);
};
```

