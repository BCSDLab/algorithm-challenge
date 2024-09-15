# Intuition
중복 선택이 가능하므로 재귀적으로 각 후보를 추가하고, 목표 값에 도달하면 그 조합을 결과에 추가하는 방식을 떠올린다.

# Approach
1. 각 숫자를 중복 선택할 수 있으므로, 현재 숫자를 여러 번 선택하는 경우도 고려하여 재귀적으로 탐색한다.
2. 남은 목표 값이 0이 되면 그 조합을 결과 리스트에 추가한다.
3. 남은 목표 값이 음수가 되면 더 이상 탐색하지 않고 돌아간다.
4. 탐색 중간에 숫자를 리스트에서 추가하고, 재귀 호출 후 다시 제거하는 방식으로 조합을 생성한다.

# Complexity
- Time complexity: $O(2^n)$
가능한 모든 조합을 탐색하므로, 최악의 경우 후보 수에 비례

- Space complexity: $O(N)$
재귀 호출 스택의 깊이와 조합 리스트를 저장하는 데 사용되는 공간 $O(N)$

# Code
```java []
class Solution {
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        combinationSum(result, new ArrayList<>(), candidates, target, target, 0);
        return result;
    }

    public void combinationSum(
        List<List<Integer>> ret,
        List<Integer> temp,
        int[] candidates, 
        int target,
        int remain,
        int start
    ) {
        if (remain == 0) ret.add(new ArrayList(temp));
        else if (remain < 0) return;
        for (int i = start; i < candidates.length; ++i) {
            temp.add(candidates[i]);
            combinationSum(ret, temp, candidates, target, remain - candidates[i], i);
            temp.remove(temp.size() - 1);
        }
    }
}
```

# Learned
오랜만에 백트래킹 구현하니 쉽지 않았다.