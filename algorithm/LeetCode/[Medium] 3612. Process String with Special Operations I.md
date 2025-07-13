3612. Process String with Special Operations I

You are given a string s consisting of lowercase English letters and the special characters: `*`, `#`, and `%`.

Build a new string `result` by processing `s` according to the following rules from left to right:

* If the letter is a lowercase English letter append it to `result`.
* A `'*'` **removes** the last character from `result`, if it exists.
* A `'#'` **duplicates** the current `result` and appends it to itself.
* A `'%'` **reverses** the current `result`.

Return the final string `result` after processing all characters in `s`.

 

**Example 1:**
```
Input: s = "a#b%*"

Output: "ba"

Explanation:

i	s[i]	Operation	Current result
0	'a'	Append 'a'	"a"
1	'#'	Duplicate result	"aa"
2	'b'	Append 'b'	"aab"
3	'%'	Reverse result	"baa"
4	'*'	Remove the last character	"ba"
Thus, the final result is "ba".
```

**Example 2:**
```
Input: s = "z*#"

Output: ""

Explanation:

i	s[i]	Operation	Current result
0	'z'	Append 'z'	"z"
1	'*'	Remove the last character	""
2	'#'	Duplicate the string	""
Thus, the final result is "".
```
 

**Constraints:**

* `1 <= s.length <= 20`
* `s` consists of only lowercase English letters and special characters `*`, `#`, and `%`.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 39.72 MB, Beats 72.15%
```
```c++
class Solution {
public:
    string processStr(string s) {
        string ans;
        for (auto c: s) {
            if (c >= 'a' && c <= 'z') {
                ans += c;
            } else if (c == '*') {
                if (ans.length()) {
                    ans.pop_back();
                }
            } else if (c == '#') {
                ans = ans + ans;
            } else {
                reverse(ans.begin(), ans.end());
            }
        }
        return ans;
    }
};
```
