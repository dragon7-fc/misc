2593. Find Score of an Array After Marking All Elements

You are given an array `nums` consisting of positive integers.

Starting with `score = 0`, apply the following algorithm:

* Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
* Add the value of the chosen integer to score.
* Mark **the chosen element and its two adjacent elements if they exist**.
* Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.

 

**Example 1:**
```
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
```

**Example 2:**
```
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 1602 ms
Memory: 34.7 MB
```
```c++
class Solution:
    def findScore(self, nums: List[int]) -> int:
        N = len(nums)
        seen = [0]*N
        hq = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(hq)
        ans = 0
        while hq:
            cn, ci = heapq.heappop(hq)
            if seen[ci]:
                continue
            ans += cn
            seen[ci] = 1
            if ci+1 < N:
                seen[ci+1] = 1
            if ci-1 >= 0:
                seen[ci-1] = 1
                
        return ans
```

**Solution 2: (Heap)**
```
Runtime: 115 ms
Memory: 105.76 MB
```
```c++
class Solution {
public:
    long long findScore(vector<int>& nums) {
        int n = nums.size(), i;
        long long ans = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        vector<bool> visited(n);
        for (i = 0; i < n; i ++) {
            pq.push({nums[i], i});
        }
        while (pq.size()) {
            auto [s, j] = pq.top();
            pq.pop();
            if (visited[j]) {
                continue;
            }
            visited[j] = true;
            ans += s;
            for (auto nj: {j+1, j-1}) {
                if (0 <= nj && nj < n) {
                    visited[nj] = true;
                } 
            }
        }
        return ans;
    }
};
```
