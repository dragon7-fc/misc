532. K-diff Pairs in an Array

Given an array of integers and an integer `k`, you need to find the number of unique `k`-diff pairs in the array. Here a `k`-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is `k`.

**Example 1:**
```
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

**Example 2:**
```
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

**Example 3:**
```
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

**Note:**
1. The pairs (i, j) and (j, i) count as the same pair.
1. The length of the array won't exceed 10,000.
1. All the integers in the given input belong to the range: [-1e7, 1e7].

# Submissions
---
**Solution 1: (Greedy, Two Pointers)**
```
Runtime: 360 ms
Memory Usage: 16 MB
```
```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = set()
        nums.sort()
        for i in range(N):
            for j in range(i+1, N):
                diff = nums[j]-nums[i]
                if diff == k:
                    ans.add((nums[i],nums[j]))
                elif diff > k:
                    break
        return len(ans)
```

**Solution 2: (Greedy, Hash Table, Two Pointers)**
```
Runtime: 160 ms
Memory Usage: 15.9 MB
```
```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        dic = {}
        for num in nums:
            if num in dic:
                res.append((dic[num],num))          
            dic[num+k] = num
        return len(set(res))
```

**Solution 3: (Counter)**
```
Runtime: 76 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        c=Counter(nums)
        
        if k==0:
            for key,v in c.items():
                if v>1:
                    cnt+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    cnt+=1
        return cnt
```

**Solution 4: (Counter)**
```
Runtime: 25 ms
Memory Usage: 13.3 MB
```
```c++
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        std::unordered_map<int,int> cnt;
        for(int num: nums)
            cnt[num]++;
        int ans = 0;
        for (auto el: cnt)
        {
            if(k==0)
            {    
                if (el.second > 1)
                ans++ ;
            }
            else if (cnt.find(el.first+k) != cnt.end())
                ans++ ;
        }
        
        return ans;
    }
};
```
