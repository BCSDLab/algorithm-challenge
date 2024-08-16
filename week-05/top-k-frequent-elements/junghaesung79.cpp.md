# Top K Frequent Elements
---
## 문제 해결 방법
---
1
* unordered_map에 각 숫자와 빈도를 저장한다.
* 내림차순으로 정렬하는 람다함수를 만든다.
* 위 람다함수로 정렬되는 우선순위 큐를 만든다.
* 숫자와 빈도를 최대 k 개수만큼 우선순위 큐에 저장한다.
2
* unordered_map에 각 숫자와 빈도를 저장한다.
* 2중 배열을 만들고 빈도 개수를 인덱스로 해서 숫자를 저장한다.
* 배열의 끝부터(가장 많이 나온 순서) 배열에 k개 만큼 넣어서 반환한다.
## 자료구조 알고리즘
---
* 우선순위 큐
  * push에 O(log n)
## 성능
---
* O(n log k) / O(n + k)
* O(n) / O(n)
## 알게 된 것
---
* 우선순위 큐를 사용해보았다.
* 버킷 정렬 알고리즘을 알게 되었다.
  * 버킷 정렬을 응용한 풀이가 2번이다.

# 코드
```cpp
class Solution {
 public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) {
      freq[num]++;
    }

    auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
      return a.second > b.second;
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);

    for (auto& p : freq) {
      pq.push(p);
      if (pq.size() > k) pq.pop();
    }

    vector<int> result;
    while (!pq.empty()) {
      result.push_back(pq.top().first);
      pq.pop();
    }

    return result;
  }
};

///

class Solution {
 public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> counter;
    for (int num : nums) {
      counter[num]++;
    }

    vector<vector<int>> buckets(nums.size() + 1);
    for (const auto& [num, count] : counter) {
      buckets[count].push_back(num);
    }

    vector<int> result;
    for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--) {
      for (int num : buckets[i]) {
        result.push_back(num);
        if (result.size() == k) break;
      }
    }

    return result;
  }
};
```
