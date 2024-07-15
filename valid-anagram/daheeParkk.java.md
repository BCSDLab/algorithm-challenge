# Intuition
문자 s의 알파벳들을 개수와 함께 저장하여 문자 t의 알파벳들과 같으면 개수를 줄인다.

# Approach
```java
1. 문자 s의 알파벳들을 Map에 개수와 함께 저장한다.
2. 문자 t의 알파벳들이 Map에 있는지 찾아본 후 있다면 개수를 줄이고, 없다면 false를 반환한다. 
3. Map에 저장된 알파벳들의 개수가 모두 0이면 true, 아니면 false를 반환한다.
```

# Code
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        Map<String, Integer> storedLetter = save(s);
        return validInclude(storedLetter, t) && validRemain(storedLetter);
    }

    public boolean validRemain(Map<String, Integer> storedLetter) {
        for (String letter: storedLetter.keySet()) {
            if (storedLetter.get(letter) != 0) {
                return false;
            }
        }
        return true;
    }

    public boolean validInclude(Map<String, Integer> storedLetter, String t) {
        String[] letters;
        if (t.length() == 1) {
            letters = new String[]{t};
        } else {
            letters = t.split("");
        }

        for (String letter : letters) {
            if (storedLetter.containsKey(letter)) {
                int count = storedLetter.get(letter);
                if (count > 0) {
                    storedLetter.put(letter, count-1);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }

    public Map<String, Integer> save(String s) {
        Map<String, Integer> store = new HashMap<>();
        String[] letters = s.split("");

        for (String letter : letters) {
            if (store.containsKey(letter)) {
                store.put(letter, store.get(letter)+1);
            } else {
                store.put(letter, 1);
            }
        }

        return store;
    }
}
```
