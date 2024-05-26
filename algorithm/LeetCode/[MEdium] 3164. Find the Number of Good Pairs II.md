3164. Find the Number of Good Pairs II

You are given 2 integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively. You are also given a positive integer `k`.

A pair `(i, j)` is called **good** if `nums1[i]` is divisible by `nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1)`.

Return the total number of **good** pairs.

 

**Example 1:**
```
Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
```

**Example 2:**
```
Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).
```

 

**Constraints:**

* `1 <= n, m <= 10^5`
* `1 <= nums1[i], nums2[j] <= 10^6`
* `1 <= k <= 10^3`

# Submissions
---
**Solution 1: (Hash Table, Math, Check all factors of nums1)**

nums1[i] = nums2[j]*k*?
-> nums1[i]/k = nums2[j]*?
                ---------
                  factor

```
Runtime: 880 ms
Memory: 175.48 MB
```
```c++
class Solution {
public:
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        long long ans = 0;
        unordered_map<int,int> freq;
        for (auto num: nums2) {
            freq[num]++;
        }
        for (auto num: nums1) {
            if (num%k != 0) {
                continue;
            }
            int sr = sqrt(num/k);
            for (int i = 1, t = num/k; i <= sr; ++i) {
                if (t%i != 0) continue;
                ans += freq[i];
                if (i != t/i) {
                    ans += freq[t/i];
                }
            }
        }
        return ans;
    }
};
```
