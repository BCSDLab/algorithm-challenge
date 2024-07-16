# Intuition
중복을 허용하지 않는 Set자료구조에 모든 요소를 넣은 후 Set의 크기와 입력 배열의 크기를 비교한다.

# Approach
1. 입력 배열의 요소들을 넣을 `Set`자료구조를 선언한다.
    - 입력 배열이 주어졌다. → 초기 용량이 주어졌다.
    - 자료구조에 담길 요소의 개수가 정해져 있는 경우 TreeSet[O(logn)]보다 HashSet[O(1)]이 더 효율적이다.
    - 따라서 `Set`의 구현체는 `HashSet`선택
2. 선언한 `Set`에 입력 배열의 요소를 전부 삽입.
3. 입력 배열 요소의 개수와 `Set`에 존재하는 요소의 개수 비교
    - 개수가 다르다면 중복 요소가 있는 것.

# Complexity
- Time complexity: `O(n)`
    - 배열의 길이를 n이라고 했을 때, 모든 원소를 `Set`에 삽입하는 비용 `O(n)`이 소모된다.
- Space complexity: `O(n)`
    - 배열의 길이를 n이라고 했을 때, 원소들을 저장하는 `Set`의 공간 `O(n)`을 소모한다.

# Code
## 1번 방법
HashSet을 이용한 방법.
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 18 ms
Memory Usage: 57.9 MB
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int num: nums) set.add(num);
        return nums.length != set.size();
    }
}
```

## 2번 방법
TreeSet을 이용한 방법.
시간복잡도: `O(nlogn)`
공간복잡도: `O(n)`
Runtime: 61 ms
Memory Usage: 59.3 MB
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new TreeSet<>();
        for (int num: nums) set.add(num);
        return nums.length != set.size();
    }
}
```
## 3번 방법
정렬을 한 후 근접 요소를 비교하는 방법
시간복잡도: `O(nlogn)`
공간복잡도: `O(n)`
Runtime: 19 ms
Memory Usage: 55.1 MB
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
}
```

# Learned
1번 방법과 3번 방법의 시간복잡도가 비슷한 것을 보니 `HashSet`의 삽입 비용이 `O(1)`이지만 해시값을 계산하는 비용도 적지 않다는 것을 배움.