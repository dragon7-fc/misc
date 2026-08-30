4039. Sum of Decoded Numbers

You are given an integer array `nums`.

Each `nums[i]` is an **encoded** integer representing two positive integers `xi` and `yi`. To decode `nums[i]`, define:

* `widthi = nums[i] % 10`.
* `di = floor(nums[i] / 10)`.
* `xi` as the integer formed by the first `widthi` digits of the decimal representation of `di`.
* `yi` as the integer formed by all remaining digits of the decimal representation of `di`.

It is guaranteed that the decimal representation of `di` contains more than widthi digits. Therefore, both `xi` and `yi` contain at least one digit.

The **decoded value** of `nums[i]` is `xi^yi`.

Return the sum of the decoded values of all elements in `nums`, modulo `10^9 + 7`.

The `floor()` function returns the integer part of the division.

 

**Example 1:**
```
Input: nums = [231]

Output: 8

Explanation:

For 231, we have width = 1, d = 23, x = 2, and y = 3.
The decoded value of 231 is 23 = 8.
Since there is only one element in nums, the sum of the decoded values is 8.
```

**Example 2:**
```
Input: nums = [2522,2101]

Output: 1649

Explanation:

For 2522, we have width = 2, d = 252, x = 25, and y = 2.
The decoded value of 2522 is 252 = 625.
For 2101, we have width = 1, d = 210, x = 2, and y = 10.
The decoded value of 2101 is 210 = 1024.
The sum of the decoded values is 625 + 1024 = 1649.
```

**Example 3:**
```
Input: nums = [2301]

Output: 73741817

Explanation:

For 2301, we have width = 1, d = 230, x = 2, and y = 30.
The decoded value is 230 = 1073741824.
Therefore, the answer is 1073741824 modulo (109 + 7) = 73741817.
```

**Constraints:**

* `1 <= nums.length <= 10^5`
* `100 < nums[i] < 10^15`
* `1 <= widthi <= 9`
* `1 <= xi, yi < 10^9`
* The digit sequences used to form `xi` and `yi` do not have leading zeros.
* It is guaranteed that every element in `nums` is a valid encoded integer.

# Submissions
---
**Solution 1: (Math, Brute Force)**
```
Runtime: 131 ms, Beats 22.71%
Memory: 91.00 MB, Beats 37.67%
```
```c++
class Solution {
    const int MOD = 1e9 + 7;
    long long powmod(long long x, long long y, int MOD) {
        long long res = 1;
        for (; y; y >>= 1) {
            if (y & 1) {
                res = res * x % MOD;
            }
            x = x * x % MOD;
        }
        return res;
    }
public:
    int sumDecoded(vector<long long>& nums) {
        long long ans = 0;
        for (const auto num: nums) {
            int width = num % 10;
            long long d = num / 10;
            string s = to_string(d);
            long long x = stoll(s.substr(0, width));
            long long y = stoll(s.substr(width));
            long long cur = powmod(x, y, MOD);
            ans += cur;
            ans %= MOD;
        }
        return ans;
    }
};
```
