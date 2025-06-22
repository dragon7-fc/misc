3589. Count Prime-Gap Balanced Subarrays

You are given an integer array `nums` and an integer `k`.

A **subarray** is called **prime-gap balanced** if:

* It contains **at least two prime** numbers, and
* The difference between the **maximum** and **minimum** prime numbers in that **subarray** is less than or equal to `k`.

Return the count of **prime-gap balanced subarrays** in `nums`.

**Note:**

* A **subarray** is a contiguous **non-empty** sequence of elements within an array.
* A prime number is a natural number greater than 1 with only two factors, 1 and itself.
 

**Example 1:**
```
Input: nums = [1,2,3], k = 1

Output: 2

Explanation:

Prime-gap balanced subarrays are:

[2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
[1,2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,3,5,7], k = 3

Output: 4

Explanation:

Prime-gap balanced subarrays are:

[2,3]: contains two primes (2 and 3), max - min = 3 - 2 = 1 <= k.
[2,3,5]: contains three primes (2, 3, and 5), max - min = 5 - 2 = 3 <= k.
[3,5]: contains two primes (3 and 5), max - min = 5 - 3 = 2 <= k.
[5,7]: contains two primes (5 and 7), max - min = 7 - 5 = 2 <= k.
Thus, the answer is 4.
```
 

**Constraints:**

* `1 <= nums.length <= 5 * 10^4`
* `1 <= nums[i] <= 5 * 10^4`
* `0 <= k <= 5 * 10^4`

# Submissions
---
**Solution 1: (Sliding Window, multiset, track 2 previous prime index)**
```
Runtime: 499 ms, Beats 80.00%
Memory: 349.01 MB, Beats 40.00%
```
```c++
class Solution {
public:
    int primeSubarray(vector<int>& nums, int k) {
        int n = nums.size(), i, pj, ppj, j, ans = 0;
        multiset<int> st;
        vector<int> dp(50001);
        dp[1] = 1;
        for (i = 2; i <= sqrt(50000); i ++) {
            if (dp[i] == 0) {
                for (j = i+i; j <= 50000; j += i) {
                    dp[j] = 1;
                }
            }
        }
        i = 0;
        for (j = 0; j < n; j ++) {
            if (dp[nums[j]] == 0) {
                ppj = pj;
                pj = j;
                st.insert(nums[j]);
            }
            while (st.size() && *st.rbegin() - *st.begin() > k) {
                if (dp[nums[i]] == 0) {
                    st.erase(st.find(nums[i]));
                }
                i += 1;
            }
            if (st.size() >= 2) {
                ans += ppj - i + 1;
            }
        }
        return ans;
    }
};
```
