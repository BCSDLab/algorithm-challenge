# Intuition

정렬된 배열의 양 끝점에서 좁혀오면서 값을 찾는다.

# Approach

1. 배열을 정렬한다.
2. 정렬된 배열에서 left, right 두가지 방향을 설정하고 좁혀온다.
  2.1. 더한 값이 목표한 값보다 크면 right를 감소한다.
  2.2. 더한 값이 목표한 값보다 작으면 left를 증가시킨다.
3. left, right 값을 찾는다.
4. 3번의 값을 이용해 원래 배열의 인덱스 값을 찾아서 반환한다.

브루트포스로 전체탐색 안하고 어떤 방법이 있을까 하다가 고안해본 방식인데 배열을 할당하는 시간에 대한 착각이 있었다.

java의 Arrays.sort는 JCF의 Collections.sort 보다 시간복잡도가 좋지 않다는 사실을 알았다.

Arrays.sort는 DualPivotQuicksort를 사용하고 이의 시간복잡도는 O(N^2)이다.
Collections.sort는 Timsort를 사용하고 이의 시간 복잡도는 O(log n)이다.

이 둘을 헷갈려서 O(log n)인데 왜 느리지? 하고 생각하게 되어 찾아본 결과 이런 내용도 찾아볼 수 있었다.

> [Timsort에 대한 내용](https://d2.naver.com/helloworld/0315536) <- 어렵다..ㅎㅎ;;

# Complexity
- Time complexity: 정렬에 O(N^2), 정렬된 값에서 수를 찾는데 O(n/2), 찾은 수의 index를 찾는데 O(n) => O(N^2)
  - 맞나..? ㅎㅎ

- Space complexity: 정렬된 배열 O(n), 방문한거 찾는 배열 O(2) => O(n)
  - 흠 이것도 맞나..?

# Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        System.out.println(Arrays.toString(sorted));
        int left = 0;
        int right = nums.length - 1;
        while(left != right) {
            int sum = sorted[left] + sorted[right];
            if (sum == target) {
                break;
            } else if (sum > target) {
                right--;
            } else if (sum < target) {
                left++;
            }
        }
        int leftNumber = sorted[left];
        int rightNumber = sorted[right];
        boolean[] visit = new boolean[2];
        for (int i = 0; i < nums.length; i++) {
            if (!visit[0] && leftNumber == nums[i]) {
                left = i;
                visit[0] = true;
            } else if (!visit[1] && rightNumber == nums[i]) {
                right = i;
                visit[1] = true;
            }
        }
        return new int[]{left, right};
    }
}
```

---

# Intuition

배열을 전체 순회하면서 찾는다.

# Approach

1. 배열의 모든 값들에 대해 서로 더해보면서 정답을 찾는다.

궁금해서 해봤는데 역시나 최악의 경우인것 같다.

# Complexity
- Time complexity: O(N^2)

- Space complexity: O(1)

# Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
```

---

# Intuition

브루트포스 (but 중복 검사를 하지 않는)

100%의 soltion을 참고하여 작성해봤다.

# Approach

1. 전체를 탐색한다.
  1.1. i 를 기준으로 간격을 벌려가면서 비교한다.

이 경우 다음과 같은 비교가 일어난다.
{0, 1}, {1, 2}, {2, 3} ...
{0, 2}, {1, 3}, {2, 4} ...
{0, 3}, {1, 4}, {2, 5} ...

이렇게 하면 중복된 검사없이 모든 수를 검증할 수 있는 방법이 된다.

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 1; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                if (nums[j] + nums[j - i] == target) {
                    return new int[]{j, j-i};
                }
            }
        }
        return new int[]{};
    }
}
```

---

# Intuition

HashMap을 이용하여 값의 차이를 이용한 해결방법

> [참고 솔루션](https://leetcode.com/problems/two-sum/solutions/3619262/3-method-s-c-java-python-beginner-friendly/)

# Approach

a + b == target 이라면 target - a == b 라는 점을 이용하여 배열을 한번만 순회한다.

1. 배열을 순회하면서 Map에 값과 해당 값의 index를 저장한다.
2. 만약 `target - nums[i]` 의 값이 있다면 두 수의 합이 target이 되므로 두 값을 반환한다.

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
class Solution {
    // a + b = target
    // a - target = b
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int minus = target - nums[i];
            if (map.containsKey(minus)) {
                return new int[]{map.get(minus), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
```
