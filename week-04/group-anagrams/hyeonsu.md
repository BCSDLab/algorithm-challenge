# Intuition
입력 배열의 스펠링을 기준으로 정렬한 후 같은 문자를 찾는다.

# Approach
1. 입력 배열 크기의 문자열 배열을 만든다.
2. 입력 배열 요소의 문자열을 정렬하여 새 배열에 옮긴다.
3. 새 배열을 순회하며 Map을 통해 같은 문자일 경우 List에 담는다.
4. Map을 List<List<String>>형식으로 변환하여 반환한다.

# Complexity
- Time complexity: $O(N)$
    - 입력 배열의 크기를 N이라고 했을 때 3개의 반복문 → 3N → $O(N)$

- Space complexity: $O(2N)$
    - 입력 배열의 크기를 N이라고 했을 때 1개의 문자열 배열, 1개의 Map, 1개의 반환 리스트 → 3N → $O(2N)$

# Code
```
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        String[] cloned = new String[strs.length];
        for (int i = 0; i < cloned.length; ++i) {
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            cloned[i] = new String(charArray);
        }
        Map<String, List<String>> map = new HashMap(strs.length);
        for (int i = 0; i < cloned.length; ++i) {
            List<String> anagrams = map.getOrDefault(cloned[i], new ArrayList<>());
            anagrams.add(strs[i]);
            if (!map.containsKey(cloned[i])) map.put(cloned[i], anagrams);
        }
        List<List<String>> ret = new ArrayList<>(strs.length);
        for (Map.Entry<String, List<String>> entry: map.entrySet()) {
            ret.add(entry.getValue());
        }
        return ret;
    }
}
```

# Learned
문자열을 스펠링으로 정렬하면 애너그램을 확인할 수 있다는 것을 배웠습니다.