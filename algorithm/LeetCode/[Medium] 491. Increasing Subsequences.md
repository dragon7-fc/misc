491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

**Example:**
```
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```

**Note:**

* The length of the given array will not exceed `15`.
* The range of integer in the given array is `[-100,100]`.
* The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 244 ms
Memory Usage: 25.6 MB
```
```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # graph 
        # nodes are index
        # edges are if greater than or eq
        
        # construct
        graph = collections.defaultdict(list)
        for i, v in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[j] >= v:
                    graph[i].append(j)
        
        res = set()
        stack = []
        def dfs(node):
            stack.append(nums[node])
            
            if (len(stack) >= 2):
                seq = tuple(stack)
                res.add(seq)
            
            if node in graph:  # prevent defaultdict adding key on access
                for nei in graph[node]:
                    dfs(nei)
            
            stack.pop()
        
        # dfs each root 
        for root in graph:
            dfs(root)
            
        return [list(seq) for seq in res]
```

**Solution 2: (Backtracking)**
```
Runtime: 97 ms
Memory Usage: 22 MB
```
```c++
class Solution {
public:
    int n;
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        n = nums.size();
        vector<int> curr;
        set<vector<int>> s;
        solve(nums, 0, curr, s, INT_MIN);
        return vector<vector<int>>(s.begin(), s.end());
    }
    
    void solve(vector<int>&nums, int i, vector<int>&curr, set<vector<int>>&s, int prev){
        if(i==nums.size()) return;
        
        for(int j=i; j<n; j++){
            if(nums[j] >= prev){
                curr.push_back(nums[j]);
                if(curr.size() >= 2) s.insert(curr);
                solve(nums, j+1, curr, s, nums[j]);
                curr.pop_back();
            }
        }     
    }
};
```

**Solution 4: (Backtracking)**
```
Runtime: 231 ms
Memory: 22.6 MB
```
```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sequence = []

        def backtrack(index):
            # if we have checked all elements
            if index == len(nums):
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            # if the sequence remains increasing after appending nums[index]
            if not sequence or sequence[-1] <= nums[index]:
                # append nums[index] to the sequence
                sequence.append(nums[index])
                # call recursively
                backtrack(index + 1)
                # delete nums[index] from the end of the sequence
                sequence.pop()
            # call recursively not appending an element
            backtrack(index + 1)
        backtrack(0)
        return result
```

**Solution 5: (Bitmasks)**
```
Runtime: 1218 ms
Memory: 22.4 MB
```
```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        for bitmask in range(1, 1 << n):
            # build the sequence
            sequence = [nums[i] for i in range(n) if (bitmask >> i) & 1]
            # check if its length is at least 2, and it is increasing
            if len(sequence) >= 2 and all([sequence[i] <= sequence[i + 1]
                                          for i in range(len(sequence) - 1)]):
                result.add(tuple(sequence))
        return result
```
