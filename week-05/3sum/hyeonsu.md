# Intuition
nums를 정렬한 후 앞에서부터 기준을 잡고 포인터 2개를 이용해서 sum이 0이 되는 것을 찾는다.

# Approach
1. 입력 배열 nums를 정렬한다.
2. nums배열의 0번째 index부터 순회한다.
3. 각각의 index에서 low, high로 point를 잡고 sum이 0이 되는 것을 찾는다.
4. sum이 0이 되는 것을 찾았을 때 while문을 통해 중복 검사 최적화를 한다.

# Complexity
- Time complexity: $O(N^2)$
    - nums정렬 $O(NlogN)$
    - 외부 `for`문 $O(N)$, 내부 `while`문 $O(N)$ → $O(N^2)$

- Space complexity: $O(1)$
    - 별도의 저장공간을 사용하지 않기 때문에 $O(1)$

# Code
```
class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret = new ArrayList();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; ++i) {
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            int low = i + 1;
            int high = nums.length - 1;
            while(low < high) {
                int sum = nums[i] + nums[low] + nums[high];
                if (sum < 0) ++low;
                else if (sum > 0) --high;
                else {
                    ret.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    while (low < high && nums[low] == nums[low + 1]) ++low;
                    while (low < high && nums[high] == nums[high - 1]) --high;
                    ++low;
                    --high;
                }
            }
        }
        return ret;
    }
}
```

# Learned
두개의 포인터를 이용하여 문제를 해결하는 것을 익혔고, 문제를 정렬했을 때 어떤 이점을 얻을 수 있는지 고민하는 연습을 할 수 있었다.