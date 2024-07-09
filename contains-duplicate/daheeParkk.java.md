# Intuition

중복을 제거한 후 길이가 변했는지 검사한다.

# Approach

```sass
1. 주어진 배열의 길이를 저장한다.
2. stream의 distinct()를 이용해 중복을 제거한다.
3. 중복을 제거한 후의 길이가 처음 길이보다 줄어들었다면 true를 반환한다.
```

# Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        int size = nums.length;
        nums = Arrays.stream(nums).distinct().toArray();
        return size > nums.length;
    }
}
```
