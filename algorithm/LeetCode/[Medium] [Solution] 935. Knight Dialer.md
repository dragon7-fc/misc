935. Knight Dialer

A chess knight can move as indicated in the chess diagram below:

![935_knight](img/935_knight.png) ![935_keypad](img/935_keypad.png)

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes `N-1` hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing `N` digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo `10^9 + 7`.

 

**Example 1:**

```
Input: 1
Output: 10
```

**Example 2:**

```
Input: 2
Output: 20
```

**Example 3:**

```
Input: 3
Output: 46
``` 

**Note:**

* `1 <= N <= 5000`

# Solution
---
## Approach 1: Dynamic Programming
**Intuition**

Let `f(start, n)` be the number of ways to dial an `n` digit number, where the knight starts at square `start`. We can create a recursion, writing this in terms of `f(x, n-1)`'s.

**Algorithm**

By hand or otherwise, have a way to query what moves are available at each square. This implies the exact recursion for `f`. For example, from `1` we can move to `6, 8`, so `f(1, n) = f(6, n-1) + f(8, n-1)`.

After, let's keep track of `dp[start] = f(start, n)`, and update it for each n from `1, 2, ..., N`.

At the end, the answer is `f(0, N) + f(1, N) + ... + f(9, N) = sum(dp)`.

```python
class Solution(object):
    def knightDialer(self, N):
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in xrange(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```

**Complexity Analysis**

* Time Complexity: $O(N)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Dynamic Programming Bottom-Up)**
```
Runtime: 1080 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD
```

**Solution 2: (DP Top-Down)**
```
Runtime: 3344 ms
Memory Usage: 74.9 MB
```
```python
class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        @functools.lru_cache(None)
        def dfs(number, rounds):
            if rounds == 1:
                return 1
            return sum([dfs(next_number, rounds-1) for next_number in moves[number]])

        return sum([dfs(number, N) for number in range(0,10)]) % (10**9+7)
```

**Solution 3: (Top-Down Dynamic Programming)**
```
Runtime: 166 ms
Memory: 39.4 MB
```
```c++
class Solution {
    vector<vector<int>> memo;
    int n;
    int MOD = 1e9 + 7;
    vector<vector<int>> jumps = {
        {4, 6},
        {6, 8},
        {7, 9},
        {4, 8},
        {3, 9, 0},
        {},
        {1, 7, 0},
        {2, 6},
        {1, 3},
        {2, 4}
    };
    
    int dp(int remain, int square) {
        if (remain == 0) {
            return 1;
        }
        
        if (memo[remain][square] != 0) {
            return memo[remain][square];
        }
        
        int ans = 0;
        for (int nextSquare : jumps[square]) {
            ans = (ans + dp(remain - 1, nextSquare)) % MOD;
        }
        
        memo[remain][square] = ans;
        return ans;
    }
public:
    int knightDialer(int n) {
        this->n = n;
        memo = vector(n + 1, vector(10, 0));
        int ans = 0;
        for (int square = 0; square < 10; square++) {
            ans = (ans + dp(n - 1, square)) % MOD;
        }
        
        return ans;
    }
};
```

**Solution 4: (Bottom-Up Dynamic Programming)**
```
Runtime: 112 ms
Memory: 37.7 MB
```
```c++
class Solution {
public:
    int knightDialer(int n) {
        vector<vector<int>> jumps = {
            {4, 6},
            {6, 8},
            {7, 9},
            {4, 8},
            {3, 9, 0},
            {},
            {1, 7, 0},
            {2, 6},
            {1, 3},
            {2, 4}
        };

        int MOD = 1e9 + 7;
        vector<vector<int>> dp(n, vector(10, 0));
        for (int square = 0; square < 10; square++) {
            dp[0][square] = 1;
        }

        for (int remain = 1; remain < n; remain++) {
            for (int square = 0; square < 10; square++) {
                int ans = 0;
                for (int nextSquare : jumps[square]) {
                    ans = (ans + dp[remain - 1][nextSquare]) % MOD;
                }

                dp[remain][square] = ans;
            }
        }

        int ans = 0;
        for (int square = 0; square < 10; square++) {
            ans = (ans + dp[n - 1][square]) % MOD;
        }

        return ans;
    }
};
```

**Solution 5: (Space-Optimized Dynamic Programming)**
```
Runtime: 116 ms
Memory: 29.3 MB
```
```c++
class Solution {
public:
    int knightDialer(int n) {
        vector<vector<int>> jumps = {
            {4, 6},
            {6, 8},
            {7, 9},
            {4, 8},
            {3, 9, 0},
            {},
            {1, 7, 0},
            {2, 6},
            {1, 3},
            {2, 4}
        };

        int MOD = 1e9 + 7;
        vector<int> dp(10, 0);
        vector<int> prevDp(10, 1);

        for (int remain = 1; remain < n; remain++) {
            dp = vector(10, 0);
            for (int square = 0; square < 10; square++) {
                int ans = 0;
                for (int nextSquare : jumps[square]) {
                    ans = (ans + prevDp[nextSquare]) % MOD;
                }

                dp[square] = ans;
            }
            
            prevDp = dp;
        }

        int ans = 0;
        for (int square = 0; square < 10; square++) {
            ans = (ans + prevDp[square]) % MOD;
        }

        return ans;
    }
};
```

**Solution 6: (Efficient Iteration On States)**
```
Runtime: 0 ms
Memory: 6.2 MB
```
```c++
class Solution {
public:
    int knightDialer(int n) {
        if (n == 1) {
            return 10;
        }
        
        int A = 4;
        int B = 2;
        int C = 2;
        int D = 1;
        int MOD = 1e9 + 7;
        
        for (int i = 0; i < n - 1; i++) {
            int tempA = A;
            int tempB = B;
            int tempC = C;
            int tempD = D;
            
            A = ((2 * tempB) % MOD + (2 * tempC) % MOD) % MOD;
            B = tempA;
            C = (tempA + (2 * tempD) % MOD) % MOD;
            D = tempC;
        }
        
        int ans = (A + B) % MOD;
        ans = (ans + C) % MOD;
        return (ans + D) % MOD;
    }
};
```

**Solution 7: (Linear Algebra)**
```
Runtime: 27 ms
Memory: 9.4 MB
```
```c++
class Solution {
    int MOD = 1e9 + 7;
    vector<vector<long>> multiply(vector<vector<long>>& A, vector<vector<long>>& B) {
        vector<vector<long>> result(A.size(), vector<long>(B[0].size(), 0));
        
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B[0].size(); j++) {
                for (int k = 0; k < B.size(); k++) {
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        
        return result;
    }
public:
    int knightDialer(int n) {
        if (n == 1) {
            return 10;
        }
        
        vector<vector<long>> A = {
            {0, 0, 0, 0, 1, 0, 1, 0, 0, 0},
            {0, 0, 0, 0, 0, 0, 1, 0, 1, 0},
            {0, 0, 0, 0, 0, 0, 0, 1, 0, 1},
            {0, 0, 0, 0, 1, 0, 0, 0, 1, 0},
            {1, 0, 0, 1, 0, 0, 0, 0, 0, 1},
            {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
            {1, 1, 0, 0, 0, 0, 0, 1, 0, 0},
            {0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
            {0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
            {0, 0, 1, 0, 1, 0, 0, 0, 0, 0}
        };
        
        vector<vector<long>> v = {
            {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
        };
        
        n--;
        while (n > 0) {
            if ((n & 1) != 0) {
                v = multiply(v, A);
            }
            
            A = multiply(A, A);
            n >>= 1;
        }
        
        int ans = 0;
        for (long num : v[0]) {
            ans = (ans + num) % MOD;
        }
        
        return ans;
    }
};
````
