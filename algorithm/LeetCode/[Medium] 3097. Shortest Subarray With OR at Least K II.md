3097. Shortest Subarray With OR at Least K II

You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is at least `k`.

Return the length of **the shortest special non-empty** subarray  of `nums`, or return `-1` if no special subarray exists.

 

**Example 1:**
```
Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.
```

**Example 2:**
```
Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.
```

**Example 3:**
```
Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.
```
 

**Constraints:**

* `1 <= nums.length <= 2 * 10^5`
* `0 <= nums[i] <= 10^9`
* `0 <= k <= 10^9`

# Submissions
---
**Solution 1: (Sliding Window, Hash Table)**
```
Runtime: 1640 ms
Memory: 37.79 MB
```
```python
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit = [-1 for _ in range(32)]
        n = len(nums)
        i, cur, res = 0, 0, float("inf")
        for j in range(n):
            cur |= nums[j]
            for b in range(32):
                if nums[j] & (1 << b):
                    bit[b] = j
            while cur >= k and i <= j:
                res = min(res, j - i + 1)
                for b in range(32):
                    if nums[i] & (1 << b) and bit[b] == i:
                        bit[b] = -1
                        cur ^= (1 << b)
                i += 1     
        return res if res != float("inf") else -1

```

**Solution 2: (Sliding Window, Counter)**
```
Runtime: 4 ms
Memory: 88.40 MB
```
```c++
class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        if (k == 0) {
            return 1;
        }
        int n = nums.size(), i = 0, j = 0, cur = 0, b, cnt[32] = {0}, ans = INT_MAX;
        while (j < n) {
            while (j < n && cur < k) {
                b = 0;
                while ((1<<b) <= nums[j]) {
                    cnt[b] += ((nums[j]&(1<<b)) > 0);
                    b += 1;
                }
                cur |= nums[j];
                j += 1;
            }
            while (i <= j && cur >= k) {
                ans = min(ans, j-i);
                if (ans == 1) {
                    return ans;
                }
                b = 0;
                while ((1<<b) <= nums[i]) {
                    if ((1<<b) & nums[i]) {
                        cnt[b] -= 1;
                        if (cnt[b] == 0) {
                            cur -= (1<<b); 
                        }
                    }
                    b += 1;
                }
                i += 1;
            }
        }
        return ans != INT_MAX ? ans : -1;
    }
};
```

**Solution 3: (Sliding Window, Counter, Greedy)**
```
Runtime: 23 ms
Memory: 88.35 MB
```
```c++
class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int i = 0, j = 0, b, cur = 0, ans = INT_MAX, cnt[32] = {0};
        for (j = 0; j < nums.size(); j ++) {
            cur |= nums[j];
            for (b = 0; (1<<b) <= nums[j]; b ++) {
                if (nums[j] & (1<<b)) {
                    cnt[b] += 1;
                }
            }
            while (i <= j && cur >= k) {
                ans = min(ans, j-i+1);
                for (int b = 0; b < 32; b ++) {
                    if ((1<<b) & nums[i]) {
                        cnt[b] -= 1;
                        if (cnt[b] == 0) {
                            cur ^= (1<<b);
                        }
                    }
                }
                i += 1;
            }
        }
        return ans != INT_MAX ? ans : -1;

    }
};
```
