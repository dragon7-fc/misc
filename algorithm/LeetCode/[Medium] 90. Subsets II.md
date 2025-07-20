90. Subsets II

Given a collection of integers that might contain duplicates, `nums`, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums and iterate through it
        # For every new element, append that element to every list in result
        # If you see same number, then only append to lists 
        # that you created when you added it in previous iteration
        res = [[]]
        prev = -1
        nums.sort()

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                from_pos = prev
            else:
                from_pos = 0

            prev = len(res)
            for item in res[from_pos:prev]:
                res.append(item + [n])

        return res
```
**Solution 2: (Recursion)**
```
Runtime: 36 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return set(tuple(el) for el in output)
```

**Solution3: (itertools)**
```
Runtime: 32 ms
Memory Usage: 12.5 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        m = [[i for i in itertools.combinations(nums,j)] for j in range(len(nums)+1)]
        m1 = [tuple(sorted(i)) for j in m for i in j]
        return list(set(m1))
```

**Solution 4: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
    
        def backtrack(index, choosen):
            if index >= len(nums):
                result.add(tuple(choosen[:]))
                return
            backtrack(index+1, choosen + [nums[index]])
            backtrack(index+1, choosen)

        nums.sort()
        backtrack(0, [])
        return result
```

**Solution 5: (Backtracking, Sort)**

    1 2 2
   -------
    []
    1
      2
         2x
    1 2
    1   2x
      2 2
    1 2 2


        1,2,2
              ^
                      1
                  /      \
               2             2
           /       \       /    \
       2           [1]    2      []
  /      \              /   \
[1,2,2] [1,2]         [2,2] [2]
```
Runtime: 0 ms, Beats 100.00%
Memory: 10.24 MB, Beats 96.83%
```
```c++
class Solution {
    void bt(int i, int n, vector<int> &nums, vector<int> &p, vector<vector<int>> &ans) {
        if (i == n) {
            ans.push_back(p);
            return;
        }
        p.push_back(nums[i]);
        bt(i+1, n, nums, p, ans);
        p.pop_back();
        while (i+1 < n && nums[i+1] == nums[i]) {
            i += 1;
        }
        bt(i+1, n, nums, p, ans);
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        int n = nums.size();
        vector<int> p;
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        bt(0, n, nums, p, ans);
        return ans;
    }
};
```
