# 첫시도

# Intuition
주어진 배열에서 중복된 요소가 있는지 확인하기 위해 요소들의 빈도를 기록한다.

# Approach
1. 주어진 배열을 순회하면서 각 요소의 빈도를 해시맵에 기록
2. 해시맵을 다시 순회하면서 빈도가 2 이상인 요소가 있는지 확인

# Complexity
- Time complexity: `O(n)`
  - 배열을 한 번 순회하는 비용 O(n)과 해시맵을 순회하는 비용 O(n)이 합쳐져 O(n)이다.
- Space complexity: `O(n)`
  - 해시맵에 배열의 모든 요소를 저장할 수 있으므로 O(n)이다.

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 29 ms
Memory Usage: 58.80 MB

```java
public class ContainsDuplicate217 {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> m = new HashMap<>();
        for(Integer num : nums) {
            if (!m.containsKey(num)) {
                m.put(num, 1);
            } else {
                m.replace(num, m.get(num)+1);
            }
        }

        boolean bool = false;

        for(Integer key : m.keySet()) {
            if (bool) return true;
            if (!((m.get(key) >= 2))) {
                bool = false;
            } else {
                bool = true;
            }
        }

        return bool;
    }
}
```

# Learned
for문이 각각 돌아서 O(n)이지만 비효율적이라고 생각해 한번만 돌게 개선점을 찾았다.

# 두번째 시도
# Intuition
배열의 각 요소를 순회하면서 집합(Set)을 사용하여 중복 여부를 확인할 수 있다.

# Approach
1. 주어진 배열을 순회하면서 각 요소를 집합(Set)에 추가
2. 집합에 요소를 추가할 때 이미 존재하는 요소가 있으면 중복이므로 true를 반환
3. 배열을 끝까지 순회한 후에도 중복이 없으면 false를 반환

# Complexity
- Time complexity: `O(n)`
    - 입력 배열을 순회하는 비용 `O(n)`
- Space complexity: ` `
    - 집합(Set)에 배열의 모든 요소를 저장할 수 있으므로 O(n)

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 7 ms
Memory Usage: 60.19 MB

```java
public class ContainsDuplicate217 {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for(Integer num : nums) {
            if (!s.add(num)) {
                return true;
            }
        }
        return false;
    }
}
```

# Learned
집합을 사용해 중복 요소를 효율적으로 찾는 법을 배웠다.
