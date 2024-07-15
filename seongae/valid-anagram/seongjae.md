# 첫시도

# Intuition
두 문자열의 정렬된 결과가 동일하면 아나그램일 수 있다.

# Approach
1. 두 문자열을 각각 문자 배열로 변환
2. 두 배열을 정렬
3. 두 배열의 길이가 다르면 false를 반환
4. 두 배열을 순회하며 각 인덱스의 문자가 동일한지 확인
5. 만약 동일하지 않은 문자가 있다면 false를 반환
모든 문자가 동일하다면 true를 반환

# Complexity
- Time complexity: `O(n log n)`
  - 문자열을 정렬하는 비용이 있기 때문에 log n이 더 걸림
- Space complexity: `O(n)`
  - 정렬된 배열을 저장하기 위한 공간이 필요

# Code
시간복잡도: `O(n log n)`
공간복잡도: `O(n)`
Runtime: 4 ms
Memory Usage: 44.60 MB

```java
public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {
        char[] ch1 = s.toCharArray(); char[] ch2 = t.toCharArray();
        Arrays.sort(ch1); Arrays.sort(ch2);
        if (!(ch1.length ==ch2.length)) return false;
        for (int i = 0; i < ch2.length; i++) {
            if (!(ch1[i] == ch2[i])) {
                return false;
            }
        }
        return true;
    }
}
```

# Learned
문자열을 정렬하여 아나그램을 확인할 수 있지만, 이는 시간복잡도가 높아 대규모 데이터에 비효율적일 수 있다.

# 두번째 시도
# Intuition
각 문자의 빈도를 비교하는 방식으로 문제를 해결

# Approach
1. 두 문자열의 길이가 다르면 false를 반환
2. 알파벳 소문자 26개의 빈도를 저장할 수 있는 배열을 생성
3. 첫 번째 문자열의 각 문자의 빈도를 증가
4. 두 번째 문자열의 각 문자의 빈도를 감소
5. 배열을 순회하며 모든 값이 0인지 확인. 모든 값이 0이면 true를, 그렇지 않으면 false를 반환

# Complexity
- Time complexity: `O(n)`
    - 입력 배열을 순회하는 비용 `O(n)`
- Space complexity: `O(1)`
    - 고정된 크기의 추가 배열(알파벳 26개)을 사용하므로 공간복잡도는 O(1)

# Code
시간복잡도: `O(n)`
공간복잡도: `O(1)`
Runtime: 1 ms
Memory Usage: 42.98 MB

```java
public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] count = new int[26];

        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            count[c - 'a']--;
        }

        for (int i : count) {
            if (i != 0) {
                return false;
            }
        }

        return true;
    }
}
```

# Learned
1. 문자열을 정렬하지 않고 각 문자의 빈도를 비교하여 아나그램을 효율적으로 확인하는 방법을 배웠다.
2. 배열을 사용하여 고정된 크기의 공간을 사용함으로써 공간복잡도를 낮출 수 있음을 알게 되었다.
