761. Special Binary String

Special binary strings are binary strings with the following two properties:

* The number of 0's is equal to the number of 1's.
* Every prefix of the binary string has at least as many 1's as 0's.

Given a special string `S`, a move consists of choosing two consecutive, non-empty, special substrings of `S`, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

**Example 1:**
```
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
```

**Note:**

* `S` has length at most `50`.
* `S` is guaranteed to be a special binary string as defined above.

# Submissions
---
**Solution 1: (Recursion)**

**Explanation:**

Just 4 steps:

1. Split S into several special strings (as many as possible).
1. Special string starts with 1 and ends with 0. Recursion on the middle part.
1. Sort all special strings in lexicographically largest order.
1. Join and output all strings.

**Update**

The middle part of a special string may not be another special string. But in my recursion it is.
For example, `1M0` is a splitted special string. `M` is its middle part and it must be another special string.

**Because:**

1. The number of 0's is equal to the number of 1's in M
1. If there is a prefix `P` of M which has one less 1's than 0's, `1P` will make up a special string. `1P` will be found as special string before `1M0` in my solution.
1. It means that every prefix of M has at least as many 1's as 0's.

Based on 2 points above, M is a special string.
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        count = i = 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v=='1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])
```

**Solution 2: (DFS, Sort)**

__Explanation:__
Just 4 steps:

Split S into several special strings (as many as possible).
Special string starts with 1 and ends with 0. Recursion on the middle part.
Sort all special strings in lexicographically largest order.
Join and output all strings.

__Update__
The middle part of a special string may not be another special string. But in my recursion it is.
For example, 1M0 is a splitted special string. M is its middle part and it must be another special string.

Because:

The number of 0's is equal to the number of 1's in M
If there is a prefix P of Mwhich has one less 1's than 0's, 1P will make up a special string. 1P will be found as special string before 1M0 in my solution.
It means that every prefix of M has at least as many 1's as 0's.
Based on 2 points above, M is a special string.
                               
            s = "11011000"
                 /11100100  < ans
                   ^^^^
                       ^^
                    sort
        1 + 101100 + 0
            /10   \1100
         1 + 0   1 + 10 + 0
                     /10
                  1 + 0

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.19 MB, Beats 90.83%
```
```c++
class Solution {
public:
    string makeLargestSpecial(string s) {
        int count = 0, i = 0, j;
        vector<string> dp;
        for (j = 0; j < s.size(); ++j) {
            if (s[j] == '1') {
                count += 1;
            } else {
                count -= 1;
            }
            if (count == 0) {
                dp.push_back('1' + makeLargestSpecial(s.substr(i + 1, j - i - 1)) + '0');
                i = j + 1;
            }
        }
        sort(dp.begin(), dp.end(), greater<string>());
        string ans = "";
        for (i = 0; i < dp.size(); i ++) {
            ans += dp[i];
        }
        return ans;
    }
};
```
