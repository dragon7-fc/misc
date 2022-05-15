47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

# Submissions
---
**Solution 1: (Backtracking with Groups of Numbers)**
```
Runtime: 56 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
```

**Solution 2: (itertools)**
```
Runtime: 84 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a = {tuple(x) for x in itertools.permutations(nums)}
        res = []
        for x in a: res.append(list(x))
        return res
```

**Solution 3: (Sort, DFS)**
```
Runtime: 56 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def shouldSwap(start,curr,nums):
            for i in range(start,curr):
                if nums[i]==nums[curr]:
                    return False
            return True
        
        def dfs(nums,path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if shouldSwap(0,i,nums):
                    dfs(nums[:i]+nums[i+1:],path+[nums[i]])

        dfs(nums,[])
        return res
```

**Solution 4: (DFS)**
```
Runtime: 11 ms
Memory Usage: 9.1 MB
```
```c++
class Solution {
public:
    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
        if (i == j-1) {
            res.push_back(num);
            return;
        }
        for (int k = i; k < j; k++) {
            if (i != k && num[i] == num[k]) continue;
            swap(num[i], num[k]);
            recursion(num, i+1, j, res);
        }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int> >res;
        recursion(nums, 0, nums.size(), res);
        return res;
    }
};
```
