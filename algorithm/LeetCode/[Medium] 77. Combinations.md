77. Combinations

Given two integers `n` and `k`, return all possible combinations of `k` numbers out of `1 ... n`.

**Example:**
```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 112 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(nums, combination):
            if len(nums) < k - len(combination):
                return
            if len(combination) == k:
                ans.append(combination)
            else:
                for i, num in enumerate(nums):
                    backtrack(nums[i+1:], combination + [num])
        backtrack([_ for _ in range(1, n+1)], [])
            
        return ans
```

**Solution 2: (itertools)**
```
Runtime: 72 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1,n+1)]
        return [_ for _ in itertools.combinations(nums, k)]
```

**Solution 3: (Backtracking)**
```
Runtime: 24 ms
Memory: 17.9 MB
```
```c++
[200~class Solution {
    void bt(int i, int n, int k, vector<int> &cur, vector<vector<int>> &ans) {
        if (i == n+1) {
            if (k == 0) {
                ans.push_back(cur);
            }
            return;
        }
        if (k < 0) {
            return;
        }
        cur.push_back(i);
        bt(i+1, n, k-1, cur, ans);
        cur.pop_back();
        bt(i+1, n, k, cur, ans);
    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> cur;
        bt(1, n, k, cur, ans);
        return ans;
    }
};
```
