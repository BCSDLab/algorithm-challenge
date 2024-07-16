# Intuition
해시맵을 사용하여 각 숫자와 그 숫자의 인덱스를 저장하면서 목표 값에 도달할 수 있는지 확인하는 방식으로 접근할 수 있다.

# Approach
1. 해시맵(HashMap)을 생성하여 각 숫자와 그 숫자의 인덱스를 저장
2. 배열을 순회하면서 현재 숫자를 확인
3. 목표 값에서 현재 숫자를 뺀 값을 해시맵에서 찾음
4. 만약 찾으면, 그 값의 인덱스와 현재 숫자의 인덱스를 반환
찾지 못하면, 현재 숫자와 그 인덱스를 해시맵에 저장
5. 배열을 끝까지 순회하여도 목표 값을 만드는 두 숫자가 없으면 예외를 반환

# Complexity
- Time complexity: `O(n)`
  - 배열을 한 번 순회하는 비용 O(n)
- Space complexity: `O(n)`
  - 해시맵에 배열의 모든 요소를 저장할 수 있으므로 O(n)

# Code
시간복잡도: `O(n)`
공간복잡도: `O(n)`
Runtime: 2ms
Memory Usage: 44.82 MB

```java
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();
        int count = 0;
        int a;
        for (int num : nums) {
            a = target - num;
            if (m.containsKey(a)) {
                return new int[]{m.get(a), count};
            } else {
                m.put(num, count);
            }
            count++;
        }
        return new int[]{0};
    }
}

```

# Learned
해시맵을 사용하여 배열을 한 번 순회하면서 두 수의 합이 목표 값이 되는 두 수를 효율적으로 찾는 방법을 배웠다.
