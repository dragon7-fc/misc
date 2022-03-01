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
Runtime: 458 ms
Memory Usage: 109.9 MB
```
```c++
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<pair<int,pair<int,int>>> pq;
        for(int i=0;i<min((int)nums1.size(),k);i++)
        {
            for(int j=0;j<min((int)nums2.size(),k);j++)
            {
                int sum=nums1[i]+nums2[j];
                if(pq.size()<k)pq.push({sum,{nums1[i],nums2[j]}});
                else if(sum<pq.top().first)
                {
                    pq.pop();
                    pq.push({sum,{nums1[i],nums2[j]}});
                }
                else
                    break;
            }
        }
        vector<vector<int>> ans;
        while(!pq.empty())
        {
            ans.push_back({pq.top().second.first,pq.top().second.second});
            pq.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
```
