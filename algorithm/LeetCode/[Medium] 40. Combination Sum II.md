40. Combination Sum II

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in candidates where the `candidate` numbers sums to `target`.

Each number in `candidates` may only be used once in the combination.

**Note:**
* All numbers (including `target`) will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1:**
```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**
```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 72 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    # slight modification on Combination Sum problem
    def dfs(self, nums, target, index, path, ans):
        if target < 0:
            return None
        if target == 0 and (path not in ans):
            ans.append(path)
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ans)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort() # this is for the break in dfs function, which makes it much faster
        self.dfs(candidates, target, 0, [], ans)
        return ans
```

**Solution 2: (Backtracking)**
```
Runtime: 1368 ms
Memory Usage: 13.8 MB
```
```python
class Solution:    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        def backtrack(nums,i):
            if sum(nums) == target and nums not in arr:
                arr.append([ele for ele in nums])
                return 
            elif sum(nums) < target and i < len(candidates):
                nums.append(candidates[i])
                backtrack(nums,i+1)
                nums.pop()
                backtrack(nums,i+1)
        backtrack([],0)
        return arr
```

**Solution 3: (DFS)**
```
Runtime: 4 ms
Memory Usage: 6.7 MB
```
```c
#define MAX_COMBINATION_LEN 30 //since min of nums[i] is 1 and max target is 30, the max combination length is 30

int *new_combination(int *arr, int len)
{
        int *new = malloc(sizeof(int) * len);
        memcpy(new, arr, sizeof(int) * len);
        return new;
}

void __combination_sum(int *cdd, int cdd_size, int start, int target, int *arr, int len, int **ret, int *rcs, int *idx)
{
        if (!target) {
                ret[*idx] = new_combination(arr, len);
                rcs[*idx] = len;
                (*idx)++;
                return;
        }
        if (len == MAX_COMBINATION_LEN)
                return;
        

        int i;
        int prev = 0;
        for (i = start; i < cdd_size; i++) {
                if (cdd[i] > target)
                        return;
                //to avoid duplication, skip cdd[i] that equals to cdd[i - 1]
                if (cdd[i] == prev)
                        continue;
                
                //we pass 'i + 1' to the next recursion so as to make arr[len + 1] >= arr[len].
                //this make arr[] monotonously non-decreasing thus avoid duplicated combinations
                arr[len] = cdd[i];
                __combination_sum(cdd, cdd_size, i + 1, target - cdd[i], arr, len + 1, ret, rcs, idx);
                
                prev = cdd[i];
        }
}

int cmp(int *a, int *b)
{
        return *a - *b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){
    int **ret = malloc(150 * sizeof(int *));
    int *rcs = malloc(150 * sizeof(int)); //return column sizes

    qsort(candidates, candidatesSize, sizeof(int), cmp);

    int idx = 0;
    int arr[MAX_COMBINATION_LEN];
    __combination_sum(candidates, candidatesSize, 0, target, arr, 0, ret, rcs, &idx);

    *returnSize = idx;
    *returnColumnSizes = rcs;
    return ret;
}
```

**Solution 4: (Backtracking)**
```
Runtime: 4 ms
Memory: 12.92 MB
```
```c++
class Solution {
    void bt(int i, int cur, vector<int> &p, vector<vector<int>> &ans, vector<int> &candidates) {
        if (cur == 0) {
            ans.push_back(p);
            return;
        }
        for (int j = i; j < candidates.size() && candidates[j] <= cur; j++) {
            // skip duplicate
            if (j == i || candidates[j] != candidates[j-1]) {
                p.push_back(candidates[j]);
                bt(j+1, cur-candidates[j], p, ans, candidates);
                p.pop_back();
            }
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> p;
        vector<vector<int>> ans;
        bt(0, target, p, ans, candidates);
        return ans;
    }
};
```
