3703. Remove K-Balanced Substrings

You are given a string `s` consisting of `'('` and `')'`, and an integer `k`.

A string is k-balanced if it is exactly `k` consecutive `'('` followed by `k` consecutive `')'`, i.e., `'(' * k + ')' * k`.

For example, if `k = 3`, k-balanced is `"((()))"`.

You must repeatedly remove all **non-overlapping k-balanced substrings** from `s`, and then join the remaining parts. Continue this process until no k-balanced substring exists.

Return the final string after all possible removals.

 

**Example 1:**
```
Input: s = "(())", k = 1

Output: ""

Explanation:

k-balanced substring is "()"

Step	Current s	k-balanced	Result s
1	(())	(())	()
2	()	()	Empty
Thus, the final string is "".
```

**Example 2:**
```
Input: s = "(()(", k = 1

Output: "(("

Explanation:

k-balanced substring is "()"

Step	Current s	k-balanced	Result s
1	(()(	(()(	((
2	((	-	((
Thus, the final string is "((".
```

**Example 3:**
```
Input: s = "((()))()()()", k = 3

Output: "()()()"

Explanation:

k-balanced substring is "((()))"

Step	Current s	k-balanced	Result s
1	((()))()()()	((()))()()()	()()()
2	()()()	-	()()()
Thus, the final string is "()()()".
```
 

**Constraints:**

* `2 <= s.length <= 10^5`
* `s` consists only of `'('` and `')'`.
* `1 <= k <= s.length / 2`

# Submissions
---
**Solution 1: (Stack, simulation)**
```
Runtime: 41 ms, Beats 14.29%
Memory: 47.22 MB, Beats 14.29%
```
```c++
class Solution {
public:
    string removeSubstring(string s, int k) {
        int n = s.size(), i;
        vector<pair<char, int>> pre;
        string ans;
        pre.push_back({'#', 0});
        for (i = 0; i < n; i ++) {
            if (s[i] != pre.back().first) {
                pre.push_back({s[i], 1});
            } else {
                pre.back().second += 1;
            }
            if (pre.size() > 2 && pre.back().first == ')' && pre.back().second >= k) {
                auto [a, c] = pre.back();
                pre.pop_back();
                if (pre.back().first == '(' && pre.back().second >= k) {
                    pre.back().second -= k;
                    if (pre.back().second == 0) {
                        pre.pop_back();
                    }
                } else {
                    pre.push_back({a, c});
                }
            }
        }
        for (i = 1; i < pre.size(); i ++) {
            ans += string(pre[i].second, pre[i].first);
        }
        return ans;
    }
};
```
