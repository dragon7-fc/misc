254. Factor Combinations

Numbers can be regarded as the product of their factors.

* For example, `8 = 2 x 2 x 2 = 2 x 4`.

Given an integer `n`, return all possible combinations of its factors. You may return the answer in **any order**.

Note that the factors should be in the range `[2, n - 1]`.

 

**Example 1:**
```
Input: n = 1
Output: []
```

**Example 2:**
```
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
```

**Example 3:**
```
Input: n = 37
Output: []
```

**Constraints:**

* `1 <= n <= 10^7`

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 94 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        
        def dfs(target, path, factor):
            if len(path) > 0:
                self.ans.append(path + [target])
            
            for i in range(factor, int(sqrt(target)) + 1):
                if target % i != 0: continue
                dfs(target // i, path + [i], i)
                
        dfs(n, [], 2)
        return self.ans
```

**Solution 2: (Backtracking)**
```
Runtime: 8 ms
Memory Usage: 9.2 MB
```
```c++
class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> ans;
        vector<int>factors;
        getResult(ans,factors,n);
        return ans;
    }
    void getResult(vector<vector<int>>&ans,vector<int>&factors,int n){
        int i=factors.empty()?2:factors.back();
        for(;i<=n/i;i++){
            if(n%i==0){
                factors.push_back(i);
                factors.push_back(n/i);
                ans.push_back(factors);
                factors.pop_back();
                getResult(ans,factors,n/i);
                factors.pop_back();
            }
        } 
    }
};
```
