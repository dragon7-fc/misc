1653. Minimum Deletions to Make String Balanced

You are given a string `s` consisting only of characters `'a'` and `'b'`.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return the **minimum** number of deletions needed to make `s` **balanced**.

**Example 1:**
```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
```

**Example 2:**
```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

**Constraints:**

* `1 <= s.length <= 105`
* `s[i] is 'a' or 'b'`.

# Submissions
---
**Solution 1: (Count from left and right side for each element)**

* `a_right_count[i]`: the number of a at the right of index i
* `b_left_count[i]`: the number of b at the left of index i
* `a_right_count[i] + b_left_count[i]`: the number of deleted characters at index i

```
Runtime: 1132 ms
Memory Usage: 19.6 MB
```
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right_count = [0] * len(s)
        b_left_count = [0] * len(s)
        
        count = 0
        for i in range(len(s)):
            b_left_count[i] = count
            if s[i] == 'b':
                count += 1
        
        count = 0
        for i in range(len(s) - 1 ,-1, -1):
            a_right_count[i] = count
            if s[i] == 'a':
                count += 1
        
        min_delete = len(s)
        for i in range(len(s)):
            min_delete = min(min_delete, a_right_count[i] + b_left_count[i])
        return min_delete
```

**Solution 1: (DP Bottom-Up)**

The problem can be formulated as DP.

At every point when you see 'a' , you have 2 options,

1. remove all the b's you found earlier. --> total cost = count_of_b
OR
1. delete the current 'a'. --> total cost = cur_total_cost + 1

If u see a 'b' , then no more cost.

Thus maintain the count of 'b's you found.

```
Runtime: 540 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        for c in s:
            if c == 'b':
                cnt_b+=1
                dp.append( dp[-1] )
            else:
                dp.append( min(cnt_b,dp[-1]+1) )
        return dp[-1]
```

**Solution 2: (Three-Pass Count Method)**
```
Runtime: 117 ms
Memory: 53.02 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        vector<int> count_a(n, 0);
        vector<int> count_b(n, 0);
        int b_count = 0;

        // First pass: compute count_b which stores the number of
        // 'b' characters to the left of the current position.
        for (int i = 0; i < n; i++) {
            count_b[i] = b_count;
            if (s[i] == 'b') b_count++;
        }

        int a_count = 0;
        // Second pass: compute count_a which stores the number of
        // 'a' characters to the right of the current position
        for (int i = n - 1; i >= 0; i--) {
            count_a[i] = a_count;
            if (s[i] == 'a') a_count++;
        }

        int min_deletions = n;
        // Third pass: iterate through the string to find the minimum deletions
        for (int i = 0; i < n; i++) {
            min_deletions = min(min_deletions, count_a[i] + count_b[i]);
        }

        return min_deletions;
    }
};
```

**Solution 3: (Combined Pass Method)**
```
Runtime: 97 ms
Memory: 38.41 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        vector<int> count_a(n, 0);
        int a_count = 0;

        // First pass: compute count_a which stores the number of
        // 'a' characters to the right of the current position
        for (int i = n - 1; i >= 0; i--) {
            count_a[i] = a_count;
            if (s[i] == 'a') a_count++;
        }

        int min_deletions = n;
        int b_count = 0;
        // Second pass: compute minimum deletions on the fly
        for (int i = 0; i < n; i++) {
            min_deletions = min(count_a[i] + b_count, min_deletions);
            if (s[i] == 'b') b_count++;
        }

        return min_deletions;
    }
};
```

**Solution 4: (Two-Variable Method)**
```
Runtime: 94 ms
Memory: 23.74 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        int a_count = 0;

        // First pass: count the number of 'a's
        for (int i = 0; i < n; i++) {
            if (s[i] == 'a') a_count++;
        }

        int b_count = 0;
        int min_deletions = n;

        // Second pass: iterate through the string to compute minimum deletions
        for (int i = 0; i < n; i++) {
            if (s[i] == 'a') a_count--;
            min_deletions = min(min_deletions, a_count + b_count);
            if (s[i] == 'b') b_count++;
        }

        return min_deletions;
    }
};
```

**Solution 5: (Using stack (one pass))**
```
Runtime: 111 ms
Memory: 24.48 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        stack<char> charStack;
        int deleteCount = 0;

        // Iterate through each character in the string
        for (int i = 0; i < n; i++) {
            // If stack is not empty, top of stack is 'b',
            // and current char is 'a'
            if (!charStack.empty() && charStack.top() == 'b' && s[i] == 'a') {
                charStack.pop();  // Remove 'b' from stack
                deleteCount++;    // Increment deletion count
            } else {
                charStack.push(s[i]);  // Push current character onto stack
            }
        }

        return deleteCount;
    }
};
```

**Solution 6: (Using DP (One Pass))**
```
Runtime: 76 ms
Memory: 38.40 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        vector<int> dp(n + 1, 0);
        int b_count = 0;

        // dp[i]: The number of deletions required to
        // balance the substring s[0, i)
        for (int i = 0; i < n; i++) {
            if (s[i] == 'b') {
                dp[i + 1] = dp[i];
                b_count++;
            } else {
                // Two cases: remove 'a' or keep 'a'
                dp[i + 1] = min(dp[i] + 1, b_count);
            }
        }

        return dp[n];
    }
};
```

**Solution 7: (Optimized DP)**
```
Runtime: 68 ms
Memory: 23.69 MB
```
```c++
class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.length();
        int min_deletions = 0;
        int b_count = 0;

        // min_deletions variable represents dp[i]
        for (int i = 0; i < n; i++) {
            if (s[i] == 'b') {
                b_count++;
            } else {
                // Two cases: remove 'a' or keep 'a'
                min_deletions = min(min_deletions + 1, b_count);
            }
        }

        return min_deletions;
    }
};

```
