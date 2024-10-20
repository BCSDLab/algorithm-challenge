# Intuition
start부터 end까지 체크해 놓고, 체크한 곳을 또 오면 false를 반환한다.

# Approach
```java 
1. 시간에 따른 방문 여부를 기록할 배열을 만든다.
2. 시작과 끝을 모두 방문한적 있다면 false를 반환한다.
3. 시작시간부터 끝시간까지 for문을 돌린다.
  3-1. 방문한적이 있고, i가 시작시간이나 끝시간이 아니면 false를 반환한다.
  3-2. 방문한적이 없으면 true를 기록한다.  
4. true를 반환한다.
```

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(n)

# Code
```java
class Solution {
    public int climbStairs(int n) {
        boolean[] check = new boolean[1000001];
        for (Interval interval : intervals) {
            int start = interval.start;
            int end = interval.end;
            if (check[start] && check[end]) {
                return false;
            }
            for (int i=start; i<=end; i++) {
                if (check[i] && (i != start && i != end)) {
                    return false;
                }
                check[i] = true;
            }
        }
        return true;
    } 
}
```
