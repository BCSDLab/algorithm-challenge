# Intuition
a부터 정렬한 단어를 map의 key로 사용하여 저장한다.

# Approach
```java
1. 주어진 배열을 한 개씩 가져온다.
2. 가져온 문자를 정렬하여 map의 key로 사용한다.
3. map에 이미 있는 key이면 해당 정렬 전의 문자를 add한다.
4. map에 없는 key이면 ArrayList를 생성하고, 정렬 전의 문자를 add한다.
5. map의 values로 만든 list를 반환한다.
```

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)

# Code
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for(int i = 0; i < strs.length; i++){
            String str = strs[i];
            char[] characters = str.toCharArray();
            Arrays.sort(characters);
            String sortedStr = new String(characters);

            if(map.containsKey(sortedStr)){
                map.get(sortedStr).add(str);
            } else {
                map.put(sortedStr, new ArrayList<>());
                map.get(sortedStr).add(str);
            }
        }

        return new ArrayList<>(map.values());
    }
}

```
