# Intuition
빈도수 Map을 이용해서 빈도수를 계산한 후, PriorityQueue를 이용해서 가장 빈도수가 많은 값을 구한다.

# Approach
1. 빈도수 Map을 이용해서 빈도수를 구한다.
2. 빈도수 Map의 내용을 Pair클래스를 이용해서 pq에 넣는다.
3. pq에서 k개 만큼 꺼내서 배열로 반환한다.

# Complexity
- Time complexity: $O(NlogN)$
    - 빈도수를 계산하는 시간: $O(N)$
    - 우선순위큐에 Map의 내용을 넣는 비용: $O(NlogN)$
    - 우선순위큐에서 값을 빼는 비용: $O(N)$

- Space complexity: $O(N)$
    - Map의 크기: $O(N)$
    - 우선순위큐의 크기: $O(N)$
    - 반환배열의 크기: $O(N)$

# Code
```
class Solution {

    class Pair implements Comparable<Pair>{
        int num, freq;
        Pair(int num, int freq) {
            this.num = num;
            this.freq = freq;
        }
        public int compareTo(Pair other) {
            return other.freq - this.freq;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap(nums.length);
        for (int num: nums) freq.put(num, freq.getOrDefault(num, 0) + 1);
        PriorityQueue<Pair> pq = new PriorityQueue();
        for (Integer num: freq.keySet()) pq.add(new Pair(num, freq.get(num)));
        nums = new int[k];
        for (int i = 0; i < k; ++i) nums[i] = pq.poll().num;
        return nums;
    }
}
```

# Learned
예전에 비슷한 문제를 풀어봤던 경험이 있어서 비교적 쉽게 푼 것 같습니다. 빈도수를 계산하고 그것을 처리하는 방법에 대해 배웠습니다.