3670. Maximum Product of Two Integers With No Common Bits

You are given an integer array `nums`.

Your task is to find two distinct indices `i` and `j` such that the product `nums[i] * nums[j]` is **maximized**, and the binary representations of `nums[i]` and `nums[j]` do not share any common set bits.

Return the **maximum** possible product of such a pair. If no such pair exists, return 0.

 

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7]

Output: 12

Explanation:

The best pair is 3 (011) and 4 (100). They share no set bits and 3 * 4 = 12.
```

**Example 2:**
```
Input: nums = [5,6,4]

Output: 0

Explanation:

Every pair of numbers has at least one common set bit. Hence, the answer is 0.
```

**Example 3:**
```
Input: nums = [64,8,32]

Output: 2048

Explanation:

No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 (64 * 32 = 2048).
```
 

**Constraints:**

* `2 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^6`

# Submissions
---
**Solution 1: (Bit Complement)**

__Explanation__
For any given bitmask m,
dp[m] will store the largest number from the original array that is a submask of m.
In math dp[m] = a, where a is the biggest number in A that m | a = m.

For each a in A,
we find the complement of a,
the biggest a * b is a * dp[complement].

__Complexity__
Time O(max(A))
Space O(max(A))

```
Runtime: 384 ms, Beats 63.24%
Memory: 159.06 MB, Beats 59.67%
```
```c++
class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        int max_val = *max_element(nums.begin(), nums.end());
        int k = static_cast<int>(floor(log2(max_val))) + 1;
        int mask = 1 << k;
        vector<int> dp(mask, 0);
        for (int a : nums) {
            dp[a] = a;
        }

        for (int j = 0; j < k; ++j) {
            for (int i = 0; i < mask; ++i) {
                if (i & (1 << j)) {
                    dp[i] = max(dp[i], dp[i ^ (1 << j)]);
                }
            }
        }

        long long res = 0;
        for (int a : nums) {
            int complement = (mask - 1) ^ a;
            res = max(res, 1LL * a * dp[complement]);
        }
        return res;
    }
};
```
