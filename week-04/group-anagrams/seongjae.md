# Intuition
단어를 정렬해서 확인한다.

# Approach
1. 입력된 문자열 배열을 순회함.
2. 각 문자열을 문자 배열로 변환한 뒤 정렬함.
3. 정렬된 문자열을 키로 사용하여 해시맵에 추가함.
4. 해시맵의 키에 해당하는 리스트에 원래 문자열을 추가함.
5. 해시맵의 모든 값을 결과 리스트에 추가하여 반환함.

# Complexity
- Time complexity:  O(NKlogK)
N은 문자열의 개수, K는 문자열의 평균 길이
각 문자열을 정렬하는 데 O(K log K) 시간이 걸리므로 전체 시간 복잡도는 O(NKlogK)

- Space complexity: O(N * K)
해시맵에 모든 문자열을 저장하므로 공간 복잡도는 O(N * K)

6ms 47.83MB
# Code
```java
public class GroupAnagrams49 {
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);

            if (!map.containsKey(sortedStr)) {
                map.put(sortedStr, new ArrayList<>());
            }
            map.get(sortedStr).add(str);
        }

        result.addAll(map.values());

        return result;
    }
}

```

# learn
