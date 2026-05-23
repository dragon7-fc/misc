3937. Minimum Operations to Make Array Modulo Alternating I

You are given an integer array `nums` and an integer `k`.

In one operation, you can **increase** or **decrease** any element of `nums` by 1.

An array is called modulo alternating if there exist two distinct integers `x` and `y` (`0 <= x, y < k`) such that:

* For every even index `i`, `nums[i] % k == x`
* For every odd index `i`, `nums[i] % k == y`

Return the minimum number of operations required to make `nums` **modulo alternating**.

 

**Example 1:**
```
Input: nums = [1,4,2,8], k = 3

Output: 2

Explanation:

Let's choose x = 1 for even indices and y = 2 for odd indices.
Perform the following operations:
Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8].
Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8].
Now, for even indices, nums[i] % k = 1, and for odd indices, nums[i] % k = 2.
Thus, the total number of operations required is 2.
```

**Example 2:**
```
Input: nums = [1,1,1], k = 3

Output: 1

Explanation:

Incrementing nums[1] by 1 gives nums = [1, 2, 1], which satisfies the condition with x = 1 and y = 2.
Thus, the total number of operations required is 1.
```

**Constraints:**

* `1 <= nums.length <= 100`
* `1 <= nums[i] <= 10^9`
* `2 <= k <= 100`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 121 ms, Beats 16.67%
Memory: 23.86 MB, Beats 41.67%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int cur, d, ans = INT_MAX;
        for (int x = 1; x <= k; x ++) {
            for (int y = 1; y <= k; y ++) {
                if (x == y) {
                    continue;
                }
                cur = 0;
                for (int i = 0; i < nums.size(); i ++) {
                    if (i & 1) {
                        d = abs((nums[i] % k) - x);
                        cur += min(d, k - d);
                    } else {
                        d = abs((nums[i] % k) - y);
                        cur += min(d, k - d);
                    }
                }
                ans = min(ans, cur);
            }
        }
        return ans;
    }
};
```

**Solution 2: (Brute Force, Optimal, cache data)**
```
Runtime: 1 ms, Beats 83.33%
Memory: 24.33 MB, Beats 33.33%
```
```c++
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int n = nums.size();
        int min_ops[101] = {0};

        for (int x = 0; x < k; x++) {
            int ops = 0;
            for (int i = 0; i < n; i += 2) {
                int rem = nums[i] % k;
                ops += min(abs(rem - x), k - abs(rem - x));
            }

            min_ops[x] = ops;
        }

        int ans = INT_MAX;
        for (int y = 0; y < k; y++) {
            int ops_y = 0;
            for (int i = 1; i < n; i += 2) {
                int rem = nums[i] % k;
                ops_y += min(abs(rem - y), k - abs(rem - y));
            }

            for (int x = 0; x < k; x++) {
                if (x == y) continue;
                int ops_x = min_ops[x];
                ans = min(ans, ops_x + ops_y);
            }
        }

        return ans;
    }
};
```
