# Intuition
배열을 정렬한 후, 각 인덱스와 배열 값을 비교하여 빠진 숫자를 찾아낸다.

# Approach
1. 주어진 배열을 정렬함.
2. 배열의 길이와 배열의 마지막 요소를 비교하여 빠진 숫자가 n인지 확인함.
3. 배열을 순회하며 인덱스와 배열 값을 비교하여 불일치하는 값을 찾음.
4. 불일치하는 값을 반환하고, 모든 값이 일치하면 0을 반환함.

# Complexity
- Time complexity: O(n log n)
배열을 정렬하는 데 O(n log n) 시간
배열을 순회하는 데 O(n)이 걸린다.

- Space complexity: O(1)
추가적인 공간을 거의 사용하지 않으므로 O(1)

5ms 45.24MB
# Code
```java
public class MissingNumber268 {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        Arrays.sort(nums);
        if(len != nums[len-1]) return len;
        for(int i = 0; i < len; i++) {
            if(nums[i] != i) return i;
        }
        return 0;
    }
}
```

# learn
