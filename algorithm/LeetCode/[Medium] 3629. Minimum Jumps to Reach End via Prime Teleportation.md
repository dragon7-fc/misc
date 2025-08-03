3629. Minimum Jumps to Reach End via Prime Teleportation

You are given an integer array `nums` of length `n`.

You start at index 0, and your goal is to reach index `n - 1`.

From any index `i`, you may perform one of the following operations:

* **Adjacent Step**: Jump to index `i + 1` or `i - 1`, if the index is within bounds.
* **Prime Teleportation**: If `nums[i]` is a prime number p, you may instantly jump to any index `j != i` such that `nums[j] % p == 0`.

Return the **minimum** number of jumps required to reach index `n - 1`.

 

**Example 1:**
```
Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.
```

**Example 3:**
```
Input: nums = [4,6,5,8]

Output: 3

Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.
```

**Constraints:**

* `1 <= n == nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Math, BFS, O(n * sqrt(m)))**
```
Runtime: 1163 ms, Beats 55.56%
Memory: 371.58 MB, Beats 50.00%
```
```c++
class Solution {
    vector<int> factor(int x){
        vector<int> res;
        for (int d = 2; d * d <= x; d++){
            if (x%d == 0){
                res.push_back(d);
                while (x%d == 0) {
                    x /= d;
                }
            }
        }
        if (x > 1) {
            res.push_back(x);
        }
        return res;
    }
public:
    int minJumps(vector<int>& nums) {
        unordered_map<int, vector<int>> g;
        int n = nums.size(), i, ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (auto &f: factor(nums[i])) {
                g[f].push_back(i);
            }
        }
        queue<array<int,2>> q;
        vector<int> visited(n);
        q.push({0, 0});
        visited[0] = 1;
        while (q.size()){
            auto [j, s] = q.front();
            q.pop();
            if (j == n-1) {
                ans = min(ans, s);
                continue;
            }
            if (j + 1 < n && !visited[j + 1]) {
                visited[j + 1] = 1;
                q.push({j + 1, s + 1});
            }
            if (j - 1 >= 0 && !visited[j - 1]) {
                visited[j - 1] = 1;
                q.push({j - 1, s + 1});
            }
            for (auto ni: g[nums[j]]){
                if (!visited[ni]){
                    visited[ni] = 1;
                    q.push({ni,  s + 1});
                }
            }
            g[nums[j]].clear(); 
        }
        return ans;
    }
};
```
