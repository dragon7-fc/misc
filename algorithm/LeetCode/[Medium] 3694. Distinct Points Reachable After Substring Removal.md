3694. Distinct Points Reachable After Substring Removal

You are given a string `s` consisting of characters `'U'`, `'D'`, `'L'`, and `'R'`, representing moves on an infinite 2D Cartesian grid.

* `'U'`: Move from `(x, y)` to `(x, y + 1)`.
* `'D'`: Move from `(x, y)` to `(x, y - 1)`.
* `'L'`: Move from `(x, y)` to `(x - 1, y)`.
* `'R'`: Move from `(x, y)` to `(x + 1, y)`.

You are also given a positive integer `k`.

You must choose and remove exactly one contiguous substring of length `k` from `s`. Then, start from coordinate `(0, 0)` and perform the remaining moves in order.

Return an integer denoting the number of **distinct** final coordinates reachable.

 

**Example 1:**
```
Input: s = "LUL", k = 1

Output: 2

Explanation:

After removing a substring of length 1, s can be "UL", "LL" or "LU". Following these moves, the final coordinates will be (-1, 1), (-2, 0) and (-1, 1) respectively. There are two distinct points (-1, 1) and (-2, 0) so the answer is 2.
```

**Example 2:**
```
Input: s = "UDLR", k = 4

Output: 1

Explanation:

After removing a substring of length 4, s can only be the empty string. The final coordinates will be (0, 0). There is only one distinct point (0, 0) so the answer is 1.
```

**Example 3:**
```
Input: s = "UU", k = 1

Output: 1

Explanation:

After removing a substring of length 1, s becomes "U", which always ends at (0, 1), so there is only one distinct final coordinate.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of only `'U'`, `'D'`, `'L'`, and `'R'`.
* `1 <= k <= s.length`

# Submissions
---
**Solution 1: (Set, Counter, Sliding Window)**
```
Runtime: 316 ms, Beats 8.99%
Memory: 47.28 MB, Beats 69.23%
```
```c++
class Solution {
public:
    int distinctPoints(string s, int k) {
        int n = s.size(), i, x, y;
        unordered_map<char, int> cnt;
        string cur;
        unordered_set<string> st;
        for (i = n - 1; i >= k; i --) {
            cnt[s[i]] += 1;
        }
        x = cnt['R'] - cnt['L'];
        y = cnt['U'] - cnt['D'];
        cur = to_string(x) + "," + to_string(y);
        st.insert(cur);
        for (i = k; i < n; i ++) {
            cnt[s[i]] -= 1;
            cnt[s[i - k]] += 1;
            x = cnt['R'] - cnt['L'];
            y = cnt['U'] - cnt['D'];
            cur = to_string(x) + "," + to_string(y);
            st.insert(cur);
        }
        return st.size();
    }
};
```

**Solution 2: (Set, Sliding Window)**

    s = "L U L", k = 1
             ^
x         -1
y          1
             

```
Runtime: 115 ms, Beats 85.22%
Memory: 38.42 MB, Beats 76.92%
```
```c++
class Solution {
public:
    int distinctPoints(string s, int k) {
        set<pair<int,int>> seen;
        seen.insert({0, 0});
        int x = 0, y = 0;
        for (int i = k; i < s.size(); i++) {
            // add new step
            if (s[i] == 'U') y++;
            if (s[i] == 'D') y--;
            if (s[i] == 'L') x--;
            if (s[i] == 'R') x++;
            // remove old step
            if (s[i - k] == 'U') y--;
            if (s[i - k] == 'D') y++;
            if (s[i - k] == 'L') x++;
            if (s[i - k] == 'R') x--;
            seen.insert({x, y});
        }
        return seen.size();
    }
};
```
