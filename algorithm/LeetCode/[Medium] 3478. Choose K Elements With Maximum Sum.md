3478. Choose K Elements With Maximum Sum

You are given two integer arrays, `nums1` and `nums2`, both of length `n`, along with a positive integer `k`.

For each index `i` from `0` to `n - 1`, perform the following:

* Find all indices `j` where `nums1[j]` is less than `nums1[i]`.
* Choose at most `k` values of `nums2[j]` at these indices to maximize the total sum.

Return an array `answer` of size `n`, where `answer[i]` represents the result for the corresponding index `i`.

 

**Example 1:**
```
Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2

Output: [80,30,0,80,50]

Explanation:

For i = 0: Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0], resulting in 50 + 30 = 80.
For i = 1: Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1], resulting in 30.
For i = 2: No indices satisfy nums1[j] < nums1[2], resulting in 0.
For i = 3: Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3], resulting in 50 + 30 = 80.
For i = 4: Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4], resulting in 30 + 20 = 50.
```

**Example 2:**
```
Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1

Output: [0,0,0,0]

Explanation:

Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i, resulting in 0 for all positions.
```
 

**Constraints:**

`n == nums1.length == nums2.length`
`1 <= n <= 10^5`
`1 <= nums1[i], nums2[i] <= 10^6`
`1 <= k <= n`

# Submissions
---
**Solution 1: (Sort, Heap)**
```
Runtime: 77 ms, Beats 100.00%
Memory: 159.61 MB, Beats 87.50%
```
```c++
class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size(), i;
        vector<tuple<int,int,int>> arr;
        priority_queue<int, vector<int>, greater<int>> pq;
        long long cur = 0;
        vector<long long> ans(n);
        for (i = 0; i < n; i ++) {
            arr.push_back({nums1[i], nums2[i], i});
        }
        sort(arr.begin(), arr.end());
        auto [pa, pb, pj] = arr[0];
        ans[pj] = 0;
        cur = pb;
        pq.push(pb);
        for (i = 1; i < n; i ++) {
            auto [a, b, j] = arr[i];
            if (a == pa) {
                ans[j] = ans[pj];
            } else {
                ans[j] = cur;
                pa = a, pj = j;
            }
            cur += b;
            pq.push(b);
            if (pq.size() > k) {
                cur -= pq.top();
                pq.pop();
            }
        }
        return ans;
    }
};
```
