4021. Minimum Operations to Make a Rotated Palindrome I

You are given a string s consisting of lowercase English letters.

You can perform the following operations any number of times (including zero) and in any order:

* **Increment**: Choose any index `i` and replace `s[i]` with the next lowercase English letter. The letter after `'z'` is `'a'`.
* **Left rotate**: Move the first character of the string to the end.

Return the **minimum** number of operations required to make `s` a **palindrome**.

 

**Example 1:**
```
Input: s = "abc"

Output: 2

Explanation:

One optimal solution:
Left rotate the string: "abc" -> "bca".
Increment 'a' to 'b': "bca" -> "bcb".
"bcb" is a palindrome. Thus, the answer is 2.
```

**Example 2:**
```
Input: s = "yb"

Output: 3

Explanation:

Increment the first character three times: "yb" -> "zb" -> "ab" -> "bb".
"bb" is a palindrome. Thus, the answer is 3.
```

**Constraints:**

`2 <= s.length <= 2000`
`s` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Brute Force, try move left every letter to index 0 then increment every palindrome pair)**

palindrome pair:
    0 1     n-2 n-1
      ---------
    ---------------
    i+j         i-j-1+n

```
Runtime: 103 ms, Beats 33.33%
Memory: 10.69 MB, Beats 83.33%
```
```c++
class Solution {
public:
    int minOperations(string s) {
        int n = s.length(), res = n * 20;
        for (int i = 0; i < n; i++) {

            // move to index 0
            int cur = i;
            for (int j = 0; j < n / 2; j++) {

                // palindrome pair
                int a = s[(i + j) % n];
                int b = s[(i - j - 1 + n) % n];
                int d = abs(a - b);
                cur += min(d, 26 - d);
                if (cur > res) {
                    break;
                }
            }
            res = min(res, cur);
        }
        return res;
    }
};
```
