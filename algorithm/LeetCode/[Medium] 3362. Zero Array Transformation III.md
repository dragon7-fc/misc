3362. Zero Array Transformation III

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [li, ri]`.

Each `queries[i]` represents the following action on `nums`:

* Decrement the value at each index in the range `[li, ri]` in `nums` by at most `1`.
* The amount by which the value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to `0`.

Return the **maximum** number of elements that can be removed from `queries`, such that `nums` can still be converted to a **zero array** using the remaining queries. If it is not possible to convert nums to a **zero array**, return `-1`.

 

**Example 1:**
```
Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
```

**Example 2:**
```
Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].
```

**Example 3:**
```
Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.
```
 

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 10^5`
* `1 <= queries.length <= 10^5`
* `queries[i].length == 2`
* `0 <= li <= ri < nums.length`

# Submissions
---
**Solution 1: (Heap, 2 Heap)**

    [[0,2],[0,2],[1,1]]
             ^

    2  0  2
    -------   <
    -------   <
       -
            ^  
pq  33   
dp  33
    xx
k   12

    [[1,3],[0,2],[1,3],[1,2]]
     [0,2] [1,2] [1,3] [1,3]
       ^

    0   1   2   3   4
----------------------
    1   1   1   1
        ----------     <
    -----------        <
        ----------
        -------
                 ^
pq  3            3
                 x
                 4
dp  3   4433     4433
    x            x   
k   1            2 

```
Runtime: 111 ms, Beats 74.94%
Memory: 224.46 MB, Beats 40.72%
```
```c++
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int m = nums.size(), n = queries.size(), i, j = 0, k = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        priority_queue<int> dp;
        sort(queries.begin(), queries.end());
        for (i = 0; i < m; i ++) {
            while (pq.size() && pq.top() <= i) {
                pq.pop();
            }
            while (j < n && queries[j][0] == i) {
                dp.push(queries[j][1] + 1);
                j += 1;
            }
            while (pq.size() < nums[i] && dp.size() && dp.top() > i) {
                auto ed = dp.top();
                dp.pop();
                pq.push(ed);
                k += 1;
            }
            if (pq.size() < nums[i]) {
                return -1;
            }
        }
        return n - k;
    }
};
```

**Solution 2: (Heap, 1 heap, open close event, least elements cover all range)**

    nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

       0   1   2   3    4
nums   1   1   1   1
       ----------     <
           ---------- <
           ----------
           ------
       ^
dp                 -1   -1
pq     3   4433    4433 433
       x           x    x
k      1           1    1
```
Runtime: 85 ms, Beats 89.64%
Memory: 224.00 MB, Beats 94.94%
```
```c++
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int m = nums.size(), n = queries.size(), i, j = 0, k = 0;
        priority_queue<int> pq;
        vector<int> dp(m+1);
        sort(queries.begin(), queries.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });
        for (i = 0; i < m; i ++) {
            k += dp[i];
            while (j < n && queries[j][0] == i) {
                pq.push(queries[j][1] + 1);
                j += 1;
            }
            while (k < nums[i] && pq.size() && pq.top() > i) {
                dp[pq.top()] -= 1;
                pq.pop();
                k += 1;
            }
            if (k < nums[i]) {
                return -1;
            }
        }
        return pq.size();
    }
};
```
