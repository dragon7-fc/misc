46. Permutations

Given a collection of **distinct** integers, return all possible permutations.

**Example:**
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 40 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return [[]]
        if length == 1: return [[nums[0]]]
        res=[]
        for i in range(length):
            r = self.permute(nums[:i] + nums[i+1:]) 
            res += [[nums[i]]+x for x in r]
            
        return res
```

**Solution 2: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for num in nums:
                if num not in path:
                    backtrack(path + [num])
        ans = []
        backtrack([])

        return ans
```

**Solution 3: (Backtracking)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.54 MB, Beats 69.19%
```
```c++
class Solution {
    void bt(vector<int> &nums, vector<int> &visited, vector<int> &p, vector<vector<int>> &ans) {
        if (p.size() == nums.size()) {
            ans.push_back(p);
            return;
        }
        for (int i = 0; i < nums.size(); i ++) {
            if (!visited[i]) {
                visited[i] = 1;
                p.push_back(nums[i]);
                bt(nums, visited, p, ans);
                p.pop_back();
                visited[i] = 0;
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> visited(nums.size()), p;
        vector<vector<int>> ans;
        bt(nums, visited, p, ans);
        return ans;
    }
};
```
