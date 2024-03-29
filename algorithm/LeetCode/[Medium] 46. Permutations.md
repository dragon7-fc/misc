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
Runtime: 0 ms
Memory: 7.4 MB
```
```c++
class Solution {
    void dfs(vector<int> &path, vector<bool> &seen, vector<vector<int>> &ans, vector<int> &nums) {
        if (path.size() == nums.size()) {
            ans.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i ++) {
            if (!seen[i]) {
                path.push_back(nums[i]);
                seen[i] = true;
                dfs(path, seen, ans, nums);
                path.pop_back();
                seen[i] = false;
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> path;
        vector<bool> seen(nums.size());
        dfs(path, seen, ans, nums);
        return ans;
    }
};
```
