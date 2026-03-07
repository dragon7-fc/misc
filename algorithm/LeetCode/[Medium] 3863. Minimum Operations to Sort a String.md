3863. Minimum Operations to Sort a String

You are given a string s consisting of lowercase English letters.

In one operation, you can select any **substring** of `s` that is not the entire string and sort it in **non-descending** alphabetical order.

Return the **minimum** number of operations required to make s sorted in non-descending order. If it is not possible, return `-1`.

 

**Example 1:**
```
Input: s = "dog"

Output: 1

Explanation:

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
```

**Example 2:**
```
Input: s = "card"

Output: 2

Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
```

**Example 3:**
```
Input: s = "gf"

Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (3 case, middle as buffer)**


    x ... x ... x
    -------
          -------

```
Runtime: 16 ms, Beats 83.73%
Memory: 27.54 MB, Beats 89.74%
```
```c++
class Solution {
public:
    int minOperations(string s) {
        int n = s.length(), i, k = 0;
        char mn = s[0], mx = s[0];
        bool flag = true;
        for (i = 1; i < n; i ++) {
            if (s[i] < s[i - 1]) {
                flag = false;
            }
            mn = min(mn, s[i]);
            mx = max(mx, s[i]);
        }
        if (flag) {
            return 0;
        }
        if (s[0] == mx && s.back() == mn) {
            if (n == 2) {
                return -1;
            }
            for (i = 1; i < n - 1; i ++) {
                if (s[i] == mn || s[i] == mx) {
                    k += 1;
                    break;
                }
            }
            if (k) {
                return 2;
            }
            return 3;
        } else if (s[0] == mn || s.back() == mx) {
            return 1;
        }
        return 2;
    }
};
```

**Solution 2: (3 case)**

__Intuition__
We only ever need to sort [0, n-2] or [1, n-1] substrings.

And, in the worst case, we need to sort 3 times.

__Approach__
We do not actually need to sort, only check whether s[0] and s[-1] are min or max.

Handle the edge cases first (already sorted, cannot be sorted).

If s[0] is min, or s[-1] is max, sort once.
If s[0] is max and s[-1] is min, sort 3 times.
'CBA' -> 'BCA' -> 'BAC' -> 'ABC'
Otherwise, sort 2 times.

```
Runtime: 10 ms, Beats 90.93%
Memory: 27.42 MB, Beats 95.58%
```
```c++
class Solution {
public:
    int minOperations(string s) {
        if (is_sorted(begin(s), end(s)))
            return 0;
        if (s.size() == 2)
            return -1;
        auto [min_p, max_p] = minmax_element(next(begin(s)), prev(end(s)));
        if (s[0] <= s.back() && (*min_p >= s[0] || *max_p <= s.back()))
            return 1;
        return s.back() < *min_p && s[0] > *max_p ? 3 : 2;
    }
};
```
