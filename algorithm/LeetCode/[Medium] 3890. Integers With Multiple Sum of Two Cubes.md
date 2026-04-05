3890. Integers With Multiple Sum of Two Cubes

You are given an integer `n`.

An integer `x` is considered **good** if there exist **at least** two **distinct** pairs `(a, b)` such that:

* `a` and `b` are positive integers.
* `a <= b`
* `x = a^3 + b^3`

Return an array containing all good integers **less than or equal** to `n`, sorted in ascending order.

 

**Example 1:**
```
Input: n = 4104

Output: [1729,4104]

Explanation:

Among integers less than or equal to 4104, the good integers are:

1729: 13 + 123 = 1729 and 93 + 103 = 1729.
4104: 23 + 163 = 4104 and 93 + 153 = 4104.
Thus, the answer is [1729, 4104].
```

**Example 2:**
```
Input: n = 578

Output: []

Explanation:

There are no good integers less than or equal to 578, so the answer is an empty array.
```
 

**Constraints:**

* `1 <= n <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 599 ms, Beats 84.48%
Memory: 181.15 MB, Beats 51.91%
```
```c++
class Solution {
public:
    vector<int> findGoodIntegers(int n) {
        int a, b, c;
        unordered_set<int> st;
        set<int> ans;
        for (a = 1; a < 1000; a ++) {
            for (b = a; b < 1000; b ++) {
                c = a * a * a + b * b * b;
                if (c <= n) {
                    if (st.count(c)) {
                        ans.insert(c);
                    } else {
                        st.insert(c);
                    }
                } else {
                    break;
                }
            }
        }
        return vector<int>(ans.begin(), ans.end());
    }
};
```
