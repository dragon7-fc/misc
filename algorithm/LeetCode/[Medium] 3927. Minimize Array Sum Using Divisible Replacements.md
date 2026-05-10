3927. Minimize Array Sum Using Divisible Replacements

You are given an integer array `nums`.

You can perform the following operation any number of times:

* Choose two indices `a` and `b` such that `nums[a] % nums[b] == 0`.
* Replace `nums[a]` with `nums[b]`.

Return the **minimum** possible sum of the array after performing any number of operations.

 

**Example 1:**
```
Input: nums = [3,6,2]

Output: 7

Explanation:

Choose a = 1, b = 2, where nums[a] = 6 and nums[b] = 2. Since 6 % 2 == 0, replace nums[1] with nums[2].
The array becomes [3, 2, 2].
No further operation reduces the sum. Thus, the final sum is 3 + 2 + 2 = 7.
```

**Example 2:**
```
Input: nums = [4,2,8,3]

Output: 9

Explanation:

Choose a = 0, b = 1, where nums[a] = 4 and nums[b] = 2. Since 4 % 2 == 0, replace nums[0] with nums[1].
Choose a = 2, b = 1, where nums[a] = 8 and nums[b] = 2. Since 8 % 2 == 0, replace nums[2] with nums[1].
The array becomes [2, 2, 2, 3].
No further operation reduces the sum. Thus, the final sum is 2 + 2 + 2 + 3 = 9.
```

**Example 3:**
```
Input: nums = [7,5,9]

Output: 21

Explanation:

There is no pair (a, b) such that nums[a] % nums[b] == 0.
Hence, no operation can be performed. The sum remains 7 + 5 + 9 = 21.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^5`

# Submissions
---
**Solution 1: (Math, Sieve)**

__Intuition__
Factors -> Sieve approach,
to find the smallest divisor for each number in the array.

__Explanation__
First, we find the maximum value M in the array.

Then, we initialize a list f of size M + 1,
where f[a] means the minimum divisor we can find for a.
Each index initially points to itself.

We iterate through the sorted A.
For each value a,
if f[a] = a,
it means a has not been replaced.

We then iterate through all multiples b of a,
If f[b] = b,
we update f[b] = a,
replacing it with the smaller divisor.

Finally,
we sum up all f[a] for all elements in A.

Time O(nlogn + kn), where is the number of factors.
Space O(M)

```
Runtime: 193 ms, Beats 80.84%
Memory: 241.04 MB, Beats 26.05%
```
```c++
class Solution {
public:
    long long minArraySum(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> dp(mx + 1);
        for (int i = 0; i <= mx; i++) {
            dp[i] = i;
        }
        set<int> st(nums.begin(), nums.end());
        for (auto &a: st) {
            if (dp[a] == a) {
                for (int b = a; b <= mx; b += a) {
                    if (dp[b] == b) {
                        dp[b] = a;
                    }
                }
            }
        }
        long long res = 0;
        for (int num : nums) {
            res += dp[num];
        }
        return res;
    }
};
```
