664. Strange Printer

There is a strange printer with the following two special requirements:

1. The printer can only print a sequence of the same character each time.
1. At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.

Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

**Example 1:**
```
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
```

**Example 2:**
```
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
```

**Hint:** Length of the given string will not exceed 100.

## Approach #1: Dynamic Programming [Accepted]
**Intuition**

It is natural to consider letting `dp(i, j)` be the answer for printing `S[i], S[i+1], ..., S[j]`, but proceeding from here is difficult. We need the following sequence of deductions:

Whatever turn creates the final print of `S[i]` might as well be the first turn, and also there might as well only be one print, since any later prints on interval `[i, k]` could just be on `[i+1, k]`.

Say the first print is on `[i, k]`. We can assume `S[i] == S[k]`, because if it wasn't, we could print up to the last occurrence of `S[i] in [i, k]` for the same result.

When correctly printing everything in `[i, k]` (with `S[i] == S[k]`), it will take the same amount of steps as correctly printing everything in `[i, k-1]`. This is because if `S[i]` and `S[k]` get completed in separate steps, we might as well print them first in one step instead.

**Algorithm**

With the above deductions, the algorithm is straightforward.

To compute a recursion for `dp(i, j)`, for every `i <= k <= j` with `S[i] == S[k]`, we have some candidate answer `dp(i, k-1) + dp(k+1, j)`, and we take the minimum of these candidates. Of course, when `k = i`, the candidate is just `1 + dp(i+1, j)`.

To avoid repeating work, we memoize our intermediate answers `dp(i, j)`.

```python
def strangePrinter(self, S):
    memo = {}
    def dp(i, j):
        if i > j: return 0
        if (i, j) not in memo:
            ans = dp(i+1, j) + 1
            for k in xrange(i+1, j+1):
                if S[k] == S[i]:
                    ans = min(ans, dp(i, k-1) + dp(k+1, j))
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, len(S) - 1)
```

**Complexity Analysis**

* Time Complexity: $O(N^3)$ where $N$ is the length of `s`. For each of $O(N^2)$ possible states representing a subarray of `s`, we perform $O(N)$ work iterating through `k`.

* Space Complexity: $O(N^2)$, the size of our `memo`.

# Submissions
---
**Solution 1: (Dynamic Programming Top-Down)**
```
Runtime: 744 ms
Memory Usage: 16.7 MB
```
```python
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)
```

**Solution 2: (DP Top-Down)**
```
Runtime: 544 ms
Memory Usage: 15.5 MB
```
```python
class Solution:
    def strangePrinter(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            ans = dp(i+1, j) + 1
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    ans = min(ans, dp(i, k-1) + dp(k+1, j))
            return ans

        return dp(0, len(s) - 1)
```

**Solution 3: (DP Top-Down)**
```
Runtime: 14 ms
Memory: 9.5 MB
```
```c++
class Solution {
    int n;
    vector<vector<int>> dp;
    int f(int i, int j, string& s){       
        if (dp[i][j]!=-1) return dp[i][j];
        if (i==j) return dp[i][j]=1;
        int ans;
        if (s[i]==s[j]||s[j-1]==s[j]) ans=f(i, j-1, s);
        else if (s[i]==s[i+1]) ans=f(i+1, j, s);
        else{
            ans=f(i,j-1, s)+1;
            for(int k=i+1; k<j; k++){
                if(s[k]==s[j])
                    ans=min(ans, f(i, k-1, s)+f(k, j-1, s));
            }
        }
        return dp[i][j]=ans;
    }
public:
    int strangePrinter(string s) {
        n=s.size();
        dp.assign(n, vector<int>(n, -1));
        return f(0, n-1, s);
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 34 ms
Memory: 9.5 MB
```
```c++
class Solution {
public:
    int strangePrinter(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        for (int i = 0; i < n; i++)
            dp[i][i] = 1;
        for (int l = 2; l < n + 1; l++) {
            for (int i = 0; i < n-l+1; i++) {
                int j = i + l - 1;
                dp[i][j] = dp[i+1][j]+1;
                for (int k = i+1; k <= j; k++) {
                    if (s[i] == s[k]) {
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + ((j>k) ? dp[k+1][j] : 0));
                    }
                }
            }
        }
        return dp[0][n-1];
    }
};
```

**Solution 5: (Top Down Dynamic Programming (Memoization))**
```
Runtime: 11 ms
Memory: 10.68 MB
```
```c++
class Solution {
     int minimumTurns(int start, int end, string& s, vector<vector<int>>& memo) {
        // Base case: empty string requires 0 turns
        if (start > end) {
            return 0;
        }

        // If result is memoized, return it
        if (memo[start][end] != -1) {
            return memo[start][end];
        }

        // Initialize with worst case: print each character separately
        int minTurns = 1 + minimumTurns(start + 1, end, s, memo);

        // Try to optimize by finding matching characters
        for (int k = start + 1; k <= end; k++) {
            if (s[k] == s[start]) {
                // If match found, try splitting the problem
                int turnsWithMatch = minimumTurns(start, k - 1, s, memo) +
                                     minimumTurns(k + 1, end, s, memo);
                minTurns = min(minTurns, turnsWithMatch);
            }
        }

        // Memoize and return the result
        return memo[start][end] = minTurns;
    }

    string removeDuplicates(string& s) {
        string uniqueChars;
        int i = 0;
        while (i < s.length()) {
            char currentChar = s[i];
            uniqueChars += currentChar;
            // Skip all consecutive occurrences of the current character
            while (i < s.length() && s[i] == currentChar) {
                i++;
            }
        }
        return uniqueChars;
    }
public:
    int strangePrinter(string s) {
        // Preprocess the string to remove consecutive duplicate characters
        s = removeDuplicates(s);
        int n = s.length();
        // Initialize memoization array
        vector<vector<int>> memo(n, vector<int>(n, -1));
        // Start the recursive process
        return minimumTurns(0, n - 1, s, memo);
    }
};
```

**Solution 6: (Bottom Up Dynamic Programming (Tabulation))**
```
Runtime: 39 ms
Memory: 10.68 MB
```
```c++
class Solution {
    string removeDuplicates(string& s) {
        string uniqueChars;
        int i = 0;
        while (i < s.length()) {
            char currentChar = s[i];
            uniqueChars += currentChar;
            // Skip all consecutive occurrences of the current character
            while (i < s.length() && s[i] == currentChar) {
                i++;
            }
        }
        return uniqueChars;
    }
public:
    int strangePrinter(string s) {
        // Preprocess the string to remove consecutive duplicate characters
        s = removeDuplicates(s);
        int n = s.length();

        // dp[i][j] represents the minimum number of turns to print s[i] to s[j]
        vector<vector<int>> minTurns(n, vector<int>(n, 0));

        // Initialize base case
        for (int i = 0; i < n; i++) {
            // It takes 1 turn to print a single character
            minTurns[i][i] = 1;
        }

        // Fill the dp table
        for (int length = 2; length <= n; length++) {
            for (int start = 0; start + length - 1 < n; start++) {
                int end = start + length - 1;

                // Initialize with worst case: print each character separately
                minTurns[start][end] = length;

                // Try all possible splits and find the minimum
                for (int split = 0; split < length - 1; split++) {
                    int totalTurns = minTurns[start][start + split] +
                                     minTurns[start + split + 1][end];

                    // If the characters at the split and end match, we can save
                    // one turn
                    if (s[start + split] == s[end]) {
                        totalTurns--;
                    }

                    minTurns[start][end] =
                        min(minTurns[start][end], totalTurns);
                }
            }
        }

        // Return the minimum turns needed to print the entire string
        return minTurns[0][n - 1];
    }
};
```
