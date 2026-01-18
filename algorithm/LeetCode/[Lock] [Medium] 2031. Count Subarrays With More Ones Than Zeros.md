2031. Count Subarrays With More Ones Than Zeros

You are given a binary array `nums` containing only the integers `0` and `1`. Return the number of **subarrays** in `nums` that have more `1`'s than `0`'s. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subarray** is a contiguous sequence of elements within an array.

 

**Example 1:**
```
Input: nums = [0,1,1,0,1]
Output: 9
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]
```

**Example 2:**
```
Input: nums = [0]
Output: 0
Explanation:
No subarrays have more ones than zeros.
```

**Example 3:**
```
Input: nums = [1]
Output: 1
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1]
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `0 <= nums[i] <= 1`

# Submissions
---
**Solution 1: (DP, Hash Table)**
```
Runtime: 1220 ms
Memory Usage: 28.7 MB
```
```python
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        MOD = 10** 9 + 7
        counts = collections.Counter({0:1})
        res = s = dp = 0
        for n in nums:
            if n:
                s += 1
                dp += counts[s - 1]
            else:
                s -= 1
                dp -= counts[s]
            res = (res + dp) % MOD
            counts[s] += 1
        
        return res % MOD
```

**Solution 2: (BIT, DP)**


                               v
             0           i-1   i
nums         0  1              1
prefixSum 0 -1 +1         a  a+1
bit                       ka
ans                          +ka

             0  1  2  3  4
    nums = [ 0, 1, 1, 0, 1]
prefix   0  -1  0  1  0  1
bit
0  0000
1  0001
2  0010
3  0011
4  0100
5  0101      1                < -1
6  0110  1   2  3     4       < 0
7  0111            1          < 1
8  1000  1   2  3  4  5
9  1001
10 1010
ans            +1 +3 +1 +4

```
Runtime: 31 ms, Beats 84.21%
Memory: 86.74 MB, Beats 86.84%
```
```c++
class BIT {
    int n;
    vector<int> dp;
public:
    BIT(int n): n(n), dp(2 * n + 1) {}
    void update(int i, int delta) {
        i += n + 1;  // re-mapping
        while (i < dp.size()) {
            dp[i] += delta;
            i += i & -i;
        }
    }
    int query(int i) {
        i += n + 1;  // re-mapping
        int rst = 0;
        while (i > 0) {
            rst += dp[i];
            i -= i & -i;
        }
        return rst;
    }
};

class Solution {
public:
    int subarraysWithMoreOnesThanZeroes(vector<int>& nums) {
        int n = nums.size(), prefix = 0, ans = 0, MOD = 1e9 + 7;
        BIT bit(n);
        bit.update(0, 1);
        for (auto &num: nums) {
            prefix += num == 0 ? -1 : 1;
            ans += bit.query(prefix - 1);
            ans %= MOD;
            bit.update(prefix, 1);
        }
        return ans;
    }
};
```
