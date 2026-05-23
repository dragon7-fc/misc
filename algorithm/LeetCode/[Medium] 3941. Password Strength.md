3941. Password Strength

You are given a string `password`.

The **strength** of the password is calculated based on the following rules:

* 1 point for each distinct lowercase letter (`'a'` to `'z'`).
* 2 points for each distinct uppercase letter (`'A'` to `'Z'`).
* 3 points for each distinct digit (`'0'` to `'9'`).
* 5 points for each distinct special character from the set `"!@#$"`.

Each character contributes at most once, even if it appears multiple times.

Return an integer denoting the strength of the password.

 

**Example 1:**
```
Input: password = "aA1!"

Output: 11

Explanation:

The distinct characters are 'a', 'A', '1' and '!'.
Thus, the strength = 1 + 2 + 3 + 5 = 11.
```

**Example 2:**
```
Input: password = "bbB11#"

Output: 11

Explanation:

The distinct characters are 'b', 'B', '1' and '#'.
Thus, the strength = 1 + 2 + 3 + 5 = 11.
```

**Constraints:**

* `1 <= password.length <= 10^5`
* `password` consists of lowercase and uppercase English letters, digits, and special characters from `"!@#$"`.

# Submissions
---
**Solution 1: (String, Brute Force)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 15.70 MB, Beats 96.98%
```
```c++
class Solution {
public:
    int passwordStrength(string password) {
        vector<bool> visited(128);
        int ans = 0;
        for (auto &c: password) {
            if (!visited[c]) {
                visited[c] = true;
                if (islower(c)) {
                    ans += 1;
                } else if (isupper(c)) {
                    ans += 2;
                } else if (isdigit(c)) {
                    ans += 3;
                } else {
                    ans += 5;
                }
            }
        }
        return ans;
    }
};

```
