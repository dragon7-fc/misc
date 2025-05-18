3335. Total Characters in String After Transformations I

You are given a string `s` and an integer `t`, representing the number of transformations to perform. In one transformation, every character in `s` is replaced according to the following rules:

* If the character is `'z'`, replace it with the string `"ab`".
* Otherwise, replace it with the next character in the alphabet. For example, `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

Return the **length** of the resulting string after exactly `t` transformations.

Since the answer may be very large, return it modulo `10^9 + 7`.

 

**Example 1:**
```
Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
```

**Example 2:**
```
Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists only of lowercase English letters.
* `1 <= t <= 10^5`

# Submissions
---
**Solution 1: (Counter, Simulation, space transform)**

    s = "abcyy", t = 2
t:0
cnt
    a:1
    b:1
    c:1
    y:2
t:1
    b:1
    c:1
    d:1
    z:2
t:2
    a:2
    b:2
    c:1
    d:1
    e:1  

```
Runtime: 631 ms, Beats 52.22%
Memory: 494.76 MB, Beats 17.24%
```
```c++
class Solution {
    static constexpr int mod = 1000000007;
public:
    int lengthAfterTransformations(string s, int t) {
        vector<int> cnt(26);
        for (char ch : s) {
            ++cnt[ch - 'a'];
        }
        for (int round = 0; round < t; ++round) {
            vector<int> nxt(26);
            nxt[0] = cnt[25];
            nxt[1] = (cnt[25] + cnt[0]) % mod;
            for (int i = 2; i < 26; ++i) {
                nxt[i] = cnt[i - 1];
            }
            cnt = move(nxt);
        }
        int ans = 0;
        for (int i = 0; i < 26; ++i) {
            ans = (ans + cnt[i]) % mod;
        }
        return ans;
    }
};
```
