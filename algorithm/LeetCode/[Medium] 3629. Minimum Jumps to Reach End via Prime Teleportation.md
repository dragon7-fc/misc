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
**Solution 1: (Math, BFS, view from prime to multiple)**
```
Runtime: 1017 ms, Beats 35.06%
Memory: 315.94 MB, Beats 55.35%
```
```c++
class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size(), i, j, mx = *max_element(nums.begin(), nums.end());
        unordered_map<int, vector<int>> mp;
        for (i = 0; i < n; i ++) {
            mp[nums[i]].push_back(i);
        }
        vector<bool> p(mx + 1);
        for (i = 2; i <= mx; i ++) {
            if (!p[i]) {
                for (j = 2 * i; j <= mx; j += i) {
                    p[j] = true;
                }
            }
        }
        unordered_map<int, vector<int>> pre;
        // view from prime to multiple
        for (i = 2; i <= mx; i ++) {
            if (!p[i] && mp.count(i)) {
                for (auto &i0: mp[i]) {
                    pre[i].push_back(i0);
                }
                for (j = 2 * i; j <= mx; j += i) {
                    if (mp.count(j)) {
                        for (auto &i0: mp[j]) {
                            pre[i].push_back(i0);
                        }
                    }
                }
            }
        }
        queue<array<int, 2>> q;
        vector<bool> visited(n);
        visited[0] = true;
        q.push({0, 0});
        while (!q.empty()) {
            auto [i, s] = q.front();
            q.pop();
            if (i == n - 1) {
                return s;
            }
            if (i - 1 >= 0 && !visited[i - 1]) {
                visited[i - 1] = true;
                q.push({i - 1, s + 1});
            }
            if (i + 1 < n && !visited[i + 1]) {
                visited[i + 1] = true;
                q.push({i + 1, s + 1});
            }
            if (pre.count(nums[i])) {
                for (auto &i0: pre[nums[i]]) {
                    if (!visited[i0]) {
                        visited[i0] = true;
                        q.push({i0, s + 1});
                    }
                }
                pre[nums[i]].clear();
            }
        }
        return -1;
    }
};
```

**Solution 2: (Math, BFS, O(n * sqrt(m)))**
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

**Solution 3: (Reversed Breadth-First Search, O(MX log MX) + O(n log MX))**
```
Runtime: 325 ms, Beats 90.41%
Memory: 333.71 MB, Beats 46.49%
```
```c++
const int MX = 1000001;
vector<int> factors[MX];
bool initialized = []() {
    for (int i = 2; i < MX; ++i) {
        if (factors[i].empty()) {
            for (int j = i; j < MX; j += i) {
                factors[j].push_back(i);
            }
        }
    }
    return true;
}();

class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> edges;
        for (int i = 0; i < n; ++i) {
            int a = nums[i];
            if (factors[a].size() == 1) {
                edges[a].push_back(i);
            }
        }
        int res = 0;
        vector<bool> seen(n, false);
        seen[n - 1] = true;
        vector<int> q = {n - 1};
        while (true) {
            vector<int> q2;
            for (int i : q) {
                if (i == 0) return res;
                if (i > 0 && !seen[i - 1]) {
                    seen[i - 1] = true;
                    q2.push_back(i - 1);
                }
                if (i < n - 1 && !seen[i + 1]) {
                    seen[i + 1] = true;
                    q2.push_back(i + 1);
                }
                for (int p : factors[nums[i]]) {
                    if (edges.count(p)) {
                        for (int j : edges[p]) {
                            if (!seen[j]) {
                                seen[j] = true;
                                q2.push_back(j);
                            }
                        }
                        edges[p].clear();
                    }
                }
            }
            q = move(q2);
            res++;
        }
    }
};
```

**Solution 4: (Forward Breadth-First Search, O(MX log MX) + O(n log MX))**
```
Runtime: 431 ms, Beats 84.87%
Memory: 375.60 MB, Beats 30.63%
```
```c++
const int MX = 1000001;
vector<int> factors[MX];
bool initialized = []() {
    for (int i = 2; i < MX; ++i) {
        if (factors[i].empty()) {
            for (int j = i; j < MX; j += i) {
                factors[j].push_back(i);
            }
        }
    }
    return true;
}();

class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> edges;
        for (int i = 0; i < n; ++i) {
            for (int p : factors[nums[i]]) {
                edges[p].push_back(i);
            }
        }
        int res = 0;
        vector<bool> seen(n, false);
        seen[0] = true;
        vector<int> q = {0};
        while (true) {
            vector<int> q2;
            for (int i : q) {
                if (i == n - 1) return res;
                if (i > 0 && !seen[i - 1]) {
                    seen[i - 1] = true;
                    q2.push_back(i - 1);
                }
                if (i < n - 1 && !seen[i + 1]) {
                    seen[i + 1] = true;
                    q2.push_back(i + 1);
                }
                if (factors[nums[i]].size() == 1) {
                    int p = nums[i];
                    if (edges.count(p)) {
                        for (int j : edges[p]) {
                            if (!seen[j]) {
                                seen[j] = true;
                                q2.push_back(j);
                            }
                        }
                        edges[p].clear();
                    }
                }
            }
            q = move(q2);
            res++;
        }
    }
};
```

**Solution 5: (BFS, Math, precompute factor for each number then bfs to all possible location)**
```
Runtime: 370 ms, Beats 87.82%
Memory: 360.23 MB, Beats 38.01%
```
```c++
const int MX = 1000001;
vector<int> factors[MX];
bool initialized = []() {
    for (int f = 2; f < MX; f ++) {
        if (factors[f].empty()) {
            for (int a = f; a < MX; a += f) {
                factors[a].push_back(f);
            }
        }
    }
    return true;
}();

class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size(), i, p, ans = 0;
        unordered_map<int, vector<int>> g;
        // view from multiple to prime
        for (i = 0; i < n; i ++) {
            for (auto &f :factors[nums[i]]) {
                g[f].push_back(i);
            }
        }
        vector<bool> visited(n);
        queue<array<int, 2>> q;
        visited[0] = true;
        q.push({0, 0});
        while (true) {
            auto [j, s] = q.front();
            q.pop();
            if (j == n - 1) {
                return s;
            }
            if (j && !visited[j - 1]) {
                visited[j - 1] = true;
                q.push({j - 1, s + 1});
            }
            if (j + 1 < n && !visited[j + 1]) {
                visited[j + 1] = true;
                q.push({j + 1, s + 1});
            }
            if (factors[nums[j]].size() == 1) {
                p = nums[j];
                if (g.count(p)) {
                    for (auto i0 : g[p]) {
                        if (!visited[i0]) {
                            visited[i0] = true;
                            q.push({i0, s + 1});
                        }
                    }
                    g[p].clear();
                }
            }
        }
    }
};
```
