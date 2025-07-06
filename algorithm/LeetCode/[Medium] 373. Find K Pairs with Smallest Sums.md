373. Find K Pairs with Smallest Sums

You are given two integer arrays **nums1** and **nums2** sorted in ascending order and an integer **k**.

Define a pair **(u,v)** which consists of one element from the first array and one element from the second array.

Find the **k** pairs **(u1,v1),(u2,v2) ...(uk,vk)** with the smallest sums.

**Example 1:**
```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

**Example 2:**
```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

**Example 3:**
```
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
```

# Submissions
---
**Solution 1: (Sort)**
```
Runtime: 236 ms
Memory Usage: 43.5 MB
```
```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return sorted(list(itertools.product(nums1, nums2)), key=lambda x: x[0] + x[1])[:k]
```

**Solution 2: (Heap)**
```
Runtime: 284 ms
Memory Usage: 30.7 MB
```
```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = list(itertools.product(nums1, nums2))
        heapq.heapify(hq)
        return heapq.nsmallest(k, hq, key=lambda x: x[0]+x[1])
```

**Solution 3: (Heap)**
```
Runtime: 72 ms, Beats 59.80%
Memory: 142.10 MB, Beats 38.42%
```
```c++
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<tuple<int,int,int>>> pq;
        unordered_map<int,unordered_set<int>> visited;
        vector<vector<int>> ans;
        pq.push({nums1[0] + nums2[0], 0, 0});
        visited[0].insert(0);
        while (k) {
            auto [a, i, j] = pq.top();
            pq.pop();
            ans.push_back({nums1[i], nums2[j]});
            if (i+1 < m && !visited[i+1].count(j)) {
                pq.push({nums1[i+1] + nums2[j], i+1, j});
                visited[i+1].insert(j);
            }
            if (j+1 < n && !visited[i].count(j+1)) {
                pq.push({nums1[i] + nums2[j+1], i, j+1});
                visited[i].insert(j+1);
            }
            k -= 1;
        }
        return ans;
    }
};
```
