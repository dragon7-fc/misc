39. Combination Sum

Given a set of candidate numbers (`candidates`) (without duplicates) and a target number (`target`), find all unique combinations in candidates where the `candidate` numbers sums to `target`.

The same repeated number may be chosen from `candidates` unlimited number of times.

**Note:**
* All numbers (including `target`) will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**
```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 92 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []
        candidates.sort()
        
        def dfs(total, index, path, res):
            if total < 0:
                return
            if total == 0:
                res.append(path)
                return
            for i in range(index, N):
                dfs(total-candidates[i], i, path+[candidates[i]], res)

        dfs(target, 0, [], res)
        return res
```

**Solution 2: (Backtrack)**
```
Runtime: 188 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        def backtrack(nums,i):
            if sum(nums) == target:
                arr.append([ele for ele in nums])
                return 
            elif sum(nums) < target and i < len(candidates):
                nums.append(candidates[i])
                backtrack(nums,i)
                nums.pop()
                backtrack(nums,i+1)
        backtrack([],0)
        return arr
```

**Solution 3: (DP)**
```
Runtime: 132 ms
Memory Usage: 14.9 MB
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[[] for _ in range(len(candidates))] for _ in range(target+1)]
        for n in range(1, target+1):
            for i, a in enumerate(candidates):
                if n == a:
                    dp[n][i].append([a])
                else:
                    if n - a < 0: continue
                    for b in dp[n-a][i:]:
                        for s in b:
                            dp[n][i].append([a, *s])
                            
        return [s for b in dp[-1] for s in b]
```

**Solution 4: (DFS)**
```
Runtime: 12 ms
Memory Usage: 8.8 MB
```
```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void subSUm(int* candidates, int candidatesSize, int target, int** columnSizes, int* returnSize, int index, int **sumArr, int curpos, int * sumbuff){
    
    if(target < 0){
         return;      
    }
    else if(0 == target){
        sumArr[*returnSize] = (int *)malloc(curpos*sizeof(int));
        memcpy(sumArr[*returnSize], sumbuff, curpos*sizeof(int));
        (*columnSizes)[*returnSize] = curpos;
        (*returnSize) = (*returnSize) + 1;
        return;
    }
    for(int i = index; i < candidatesSize; i++){
        int subtarget = target - candidates[i];
        sumbuff[curpos] = candidates[i];
        subSUm(candidates, candidatesSize, subtarget, columnSizes, returnSize, i, sumArr, curpos+1, sumbuff);
    }
    
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){
    int **sumArr = (int **)malloc(512*sizeof(int *));
    int *sumbuff = (int *)malloc(512*sizeof(int));
    *returnColumnSizes = (int *)malloc(512*sizeof(int));
    
    *returnSize = 0;
    subSUm(candidates, candidatesSize, target, returnColumnSizes, returnSize, 0, sumArr, 0, sumbuff);
    
    return sumArr;
}
```

**Solution 5: (Backtracking)**
```
Runtime: 12 ms
Memory Usage: 10.7 MB
```
```c++
class Solution {
public:
    void bt(vector<int>& cand, int r, int i, vector<int>& p, vector<vector<int>>& rst) {
        if (r <= 0) {
            if (r == 0)
                rst.push_back(p);
            return;
        }
        if (i < cand.size()) {
            p.push_back(cand[i]);
            bt(cand, r-cand[i], i, p, rst);
            p.pop_back();
            bt(cand, r, i+1, p, rst);
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> path;
        bt(candidates, target, 0, path, ans);
        return ans;
    }
};
```
