3871. Count Commas in Range II

You are given an integer `n`.

Return the total number of commas used when writing all integers from `[1, n]` (inclusive) in standard number formatting.

In standard formatting:

* A comma is inserted after **every three** digits from the right.
* Numbers with **fewer** than 4 digits contain no commas.
 

**Example 1:**
```
Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.
```

**Example 2:**
```
Input: n = 998

Output: 0

Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.
```
 

**Constraints:**

* `1 <= n <= 10^15`

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.14 MB, Beats 17.64%
```
```c++
class Solution {
public:
    long long countCommas(long long n) {
        long long b = 1000, k = 1, ans = 0;
        while (b <= n) {
            ans += ((min(b * 1000 - 1, n) - b) + 1) * k;
            b *= 1000;
            k += 1;
        }
        return ans;
    }
};
```
