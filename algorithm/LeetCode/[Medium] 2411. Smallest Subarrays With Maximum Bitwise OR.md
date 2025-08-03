2411. Smallest Subarrays With Maximum Bitwise OR

You are given a **0-indexed** array `nums` of length `n`, consisting of non-negative integers. For each index `i` from `0` to `n - 1`, you must determine the size of the **minimum sized** non-empty subarray of `nums` starting at `i` (**inclusive**) that has the **maximum** possible **bitwise OR**.

* In other words, let `Bij` be the bitwise OR of the subarray `nums[i...j]`. You need to find the smallest subarray starting at `i`, such that bitwise OR of this subarray is equal to `max(Bik)` where `i <= k <= n - 1`.

The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array `answer` of size `n` where `answer[i]` is the length of the **minimum** sized subarray starting at `i` with **maximum** bitwise OR.

A **subarray** is a contiguous non-empty sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]
Explanation:
The maximum possible bitwise OR starting at any index is 3. 
- Starting at index 0, the shortest subarray that yields it is [1,0,2].
- Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
- Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
- Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
- Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
Therefore, we return [3,3,2,2,1]. 
```

**Example 2:**
```
Input: nums = [1,2]
Output: [2,1]
Explanation:
Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
Therefore, we return [2,1].
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 10^5`
* `0 <= nums[i] <= 10^9`

# Submissions
---
**±Solution 1: (Bit Manipulation, prefix sum)**
```
Runtime: 3785 ms
Memory Usage: 28.6 MB
```
```python
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [0] * 32
        n = len(nums)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            res[i] = max(1, max(last) - i + 1)
        return res
```

**±Solution 2: (Bit Manipulation, Counter, Sliding Window)**
```
Runtime: 154 ms Beats 20.69%
Memory: 92.11 MB Beats 13.36%
```
```
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size(), i, j = n-1, k;
        vector<int> cnt(32), ans(n);
        unordered_map<int, vector<int>> g;
        for (i = 0; i < n; i ++) {
            if (nums[i] && !g.count(nums[i])) {
                for (k = 0; (1<<k) <= nums[i]; k ++) {
                    if ((1<<k)&nums[i]) {
                        g[nums[i]].push_back(k);
                    }
                }
            }
        }
        for (i = n-1; i >= 0; i --) {
            for (auto &bi: g[nums[i]]) {
                cnt[bi] += 1;
            }
            while (i < j && all_of(g[nums[j]].begin(), g[nums[j]].end(), [&](auto &bi){
                return cnt[bi] > 1;
            })) {
                for (auto &bi: g[nums[j]]) {
                    cnt[bi] -= 1;
                }
                j -= 1;
            }
            ans[i] = j-i+1;
        }
        return ans;
    }
};
```

**±Solution 3: (Bit Manipulation, prefix sum)**
```
Runtime: 39 ms, Beats 39.66%
Memory: 60.76 MB Beats 54.74%
```
```c++
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size(), i, k;
        vector<int> pre(32), ans(n,1);
        for (i = n-1; i >= 0; i --) {
            for (k = 0; k < 31; k ++) {
                if (nums[i]&(1<<k)) {
                    pre[k] = i;
                }
                ans[i] = max(ans[i], pre[k]-i+1);
            }
        }
        return ans;
    }
};
```
