3922. Minimum Flips to Make Binary String Coherent

You are given a binary string `s`.

A string is considered **coherent** if it does not contain `"011"` or `"110"` as subsequences.

In one operation, you can flip any character in `s` (`'0'` to `'1'` or `'1'` to `'0'`).

Return an integer denoting the **minimum** number of modifications required to make `s` coherent.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

**Example 1:**
```
Input: s = "1010"

Output: 1

Explanation:

Flip s[0] to get "0010", which contains no "011" or "110" subsequences.
```

**Example 2:**
```
Input: s = "0110"

Output: 1

Explanation:

Flip s[1] to get "0010", removing all forbidden subsequences "011" and "110".
```

**Example 3:**
```
Input: s = "1000"

Output: 0

Explanation:

The string already has no "011" or "110" subsequences, so no flips are needed.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Case Study)**

__Intuition__
What's "011" and "110" in common?
They both have a 1 in the middle,
and differnent number on left and right.

So if no middle 1, or only one 1, or all 1,
it's coherent.

__Explanation__
If n < 3, return 0.

There 3 valid cases in total:
A string with only 1.
A string with at most one 1.
A string with 1 only at the two ends.

__Complexity__
Time O(n)
Space O(1)

```
Runtime: 14 ms, Beats 25.34%
Memory: 19.78 MB, Beats 27.42%
```
```c++
class Solution {
public:
    int minFlips(string s) {
        int n = s.length();
        if (n < 3) return 0;
        int cnt0 = count(s.begin(), s.end(), '0');
        int cnt1 = n - cnt0;
        // only 1
        int res1 = cnt0;
        // at most one 1
        int res2 = max(cnt1 - 1, 0);
        // 1 only at the two ends
        int res3 = cnt1 - (s[0] - '0') - (s[n - 1] - '0');
        return min({res1, res2, res3});
    }
};
```
