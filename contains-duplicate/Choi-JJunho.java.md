# Intuition

해시테이블인 Set을 이용해 배열의 값을 저장해두고, 이를 비교하며 중복을 검사한다.

# Approach

1. 빈 집합(Set)을 생성합니다.
2. 배열을 순회하면서 각 요소를 집합에 추가합니다.
3. 요소를 집합에 추가하기 전에, 해당 요소가 이미 집합에 존재하는지를 확인합니다.
4. 만약 현재 요소가 집합에 이미 존재한다면, 중복이 있다는 의미이므로 true를 반환합니다.
5. 순회를 완료할 때까지 중복된 요소가 발견되지 않으면 false를 반환합니다.

# Complexity

- 시간복잡도: 배열의 크기가 n일때 시간복잡도는 O(n)
  - 코드레벨에서 반복문 루프가 배열의 크기만큼 돈다. 이 이상의 반복은 없기에 O(n)
- 공간복잡도: 배열의 크기가 n일때 공간복잡도는 O(n)
  - 최악의 경우 배열의 크기만큼 값을 Set에 저장해야하므로 공간복잡도는 O(n)

# Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            }
            set.add(nums[i]);
        }
        return false;
    }
}
```
