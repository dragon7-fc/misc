3645. Maximum Total from Optimal Activation Order

You are given two integer arrays `value` and `limit`, both of length `n`.

Initially, all elements are inactive. You may activate them in any order.

* To activate an inactive element at index `i`, the number of currently active elements must be strictly less than `limit[i]`.
* When you activate the element at index `i`, it adds `value[i]` to the total activation value (i.e., the sum of `value[i]` for all elements that have undergone activation operations).
* After each activation, if the number of **currently** active elements becomes `x`, then all elements `j` with `limit[j] <= x` become **permanently** inactive, even if they are already active.

Return the **maximum** total you can obtain by choosing the activation order optimally.

 

**Example 1:**
```
Input: value = [3,5,8], limit = [2,1,3]

Output: 16

Explanation:

One optimal activation order is:

Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
1	1	5	0	1	j = 1 as limit[1] = 1	[1]	5
2	0	3	0	1	-	[1]	8
3	2	8	1	2	j = 0 as limit[0] = 2	[1, 2]	16
Thus, the maximum possible total is 16.
```

**Example 2:**
```
Input: value = [4,2,6], limit = [1,1,1]

Output: 6

Explanation:

One optimal activation order is:

Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
1	2	6	0	1	j = 0, 1, 2 as limit[j] = 1	[0, 1, 2]	6
Thus, the maximum possible total is 6.
```

**Example 3:**
```
Input: value = [4,1,5,2], limit = [3,3,2,3]

Output: 12

Explanation:

One optimal activation order is:

Step	Activated i	value[i]	Active Before i	Active After i	Becomes Inactive j	Inactive Elements	Total
1	2	5	0	1	-	[ ]	5
2	0	4	1	2	j = 2 as limit[2] = 2	[2]	9
3	1	1	1	2	-	[2]	10
4	3	2	2	3	j = 0, 1, 3 as limit[j] = 3	[0, 1, 2, 3]	12
Thus, the maximum possible total is 12.
```
 

**Constraints:**

* `1 <= n == value.length == limit.length <= 10^5`
* `1 <= value[i] <= 10^5`
* `1 <= limit[i] <= n`

# Submissions
---
**Solution 1: (Simulation, Sort, Greedy)**
```
Runtime: 253 ms, Beats 56.08%
Memory: 298.79 MB, Beats 57.55%
```
```c++
class Solution {
public:
    long long maxTotal(vector<int>& value, vector<int>& limit) {
        int n = value.size(), i, k = 0;
        long long ans = 0;
        vector<int> dp(n), visited(n);
        vector<vector<int>> g(n+1);
        for (i = 0; i < n; i ++) {
            dp[i] = i;
            g[limit[i]].push_back(i);
        }
        sort(dp.begin(), dp.end(), [&](int &i, int &j){
            if (limit[i] != limit[j]) {
                return limit[i] < limit[j];
            } else {
                return value[i] > value[j];
            }
        });
        for (i = 0; i < n; i ++) {
            if (!visited[dp[i]]) {
                visited[dp[i]] = 2;
                if (k < limit[dp[i]]) {
                    ans += value[dp[i]];
                    k += 1;
                    for (auto j: g[k]) {
                        if (visited[j] == 2) {
                            k -= 1;
                            visited[j] = 1;
                        } else if (!visited[j]) {
                            visited[j] = 1;
                        }
                    }
                }
            }
        }
        return ans;
    }
};
```

**Solution 2: (Heap)**

This is basically about choosing the most valuable elements we can at each “limit stage” before they get locked out.

```
Runtime: 222 ms, Beats 58.47%
Memory: 306.13 MB, Beats 47.86%
```
```c++
class Solution {
public:
    long long maxTotal(vector<int>& value, vector<int>& limit) {
        unordered_map<int, priority_queue<int>> umap;

        long long ans = 0;

        int n = value.size();

        for (int i = 0; i < n; i++) {
            umap[limit[i]].push(value[i]);
        }

        for (auto &[lim, pq]: umap) {
            for (int i = 0; i < lim && !pq.empty(); i++) {
                ans += pq.top();
                pq.pop();
            }
        }


        return ans;
    }
};
```
