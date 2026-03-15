1415. The k-th Lexicographical String of All Happy Strings of Length n

A **happy string** is a string that:

* consists only of letters of the set `['a', 'b', 'c']`.
* `s[i] != s[i + 1]` for all values of i from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc"**, **"ac"**, **"b"** and **"abcbabcbcb"** are all happy strings and strings **"aa"**, **"baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return the `k`th string of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

 

**Example 1:**
```
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
```

**Example 2:**
```
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
```

**Example 3:**
```
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
```

**Example 4:**
```
Input: n = 2, k = 7
Output: ""
```

**Example 5:**
```
Input: n = 10, k = 100
Output: "abacbabacb"
```

**Constraints:**

* `1 <= n <= 10`
* `1 <= k <= 100`

# Submissions
---
**Solution 1: (DFS)**

**Idea**

The property of DFS helps us iterate through all the possibilities in ascending order automatically. All we need to do is to output the kth result.

```
Runtime: 40 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def generate(prev, i, path):
            if i == n:
                yield path
                return
            for nei in 'abc':
                if nei != prev:
                    yield from generate(nei, i+1, path+nei)
            
        for i, res in enumerate(generate('', 0, ''), 1):            
            if i == k:
                return res
        return ''
```

**Solution 2: (Backtracking, enumerate and sort, O(2^(n - 1) * 3) = O(2^n))**
```
Runtime: 43 ms, Beats 16.40%
Memory: 26.80 MB, Beats 10.90%
```
```c++
class Solution {
    void bt(int n, string &path, vector<string> &ans) {
        if (path.length() == n) {
            ans.push_back(path);
            return;
        }
        if (path.length() == 0) {
            path = "a";
            bt(n, path, ans);
            path = "b";
            bt(n, path, ans);
            path = "c";
            bt(n, path, ans);
        } else {
            for (auto &c: {'a', 'b', 'c'}) {
                if (c != path.back()) {
                    path.push_back(c);
                    bt(n, path, ans);
                    path.pop_back();
                }
            }
        }
    }
public:
    string getHappyString(int n, int k) {
        vector<string> ans;
        string path;
        bt(n, path, ans);
        if (ans.size() < k) {
            return "";
        }
        sort(ans.begin(), ans.end());
        return ans[k - 1];
    }
};
```

**Solution 3: (Backtracking, Optimized, O(k * n) = O(2^n))**
```
Runtime: 2 ms, Beats 63.03%
Memory: 8.87 MB, Beats 70.11%
```
```c++
class Solution {
    bool dfs(int n, int &k, string &ans) {
        if (ans.size() == n) {
            k -= 1;
            if (k == 0) {
                return true;
            }
            return false;
        }
        for (auto &c: {'a', 'b', 'c'}) {
            if (ans == "" || c != ans.back()) {
                ans += c;
                if (dfs(n, k, ans)) {
                    return true;
                }
                ans.pop_back();
            }
        }
        return false;
    }
public:
    string getHappyString(int n, int k) {
        string ans;
        dfs(n, k, ans);
        return ans;
    }
};
```

**Solution 4: (Math, O(n))**

       n = 3, k = 9
---------------------
       "aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"
         1                           5                           9
        startA                      startB                      startC
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^                              ans
                4 = 1 << (n - 1)

1  aba
   -
2         |
3         |4 = 1 << (n - 1)
4         |
5  bab    |
   -=
6             |2 = 1 << (n - 1 - 1)
7  bca        |
    = 
8  bcb        |1 = 1 << (n - 1 - 2)
     -
9  c
    

total  12
startA  1
startB  1 + 4 = 5
startC  5 + 4 = 9

k       9 0 0
mid       2 1
result  c a b  

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.47 MB, Beats 84.68%
```
```c++
class Solution {
public:
    string getHappyString(int n, int k) {
        // Calculate the total number of happy strings of length n
        int total = 3 * (1 << (n - 1));
        //          ^first char
        //              ^^^^^^^^^^^^^^remainder char

        // If k is greater than the total number of happy strings, return an
        // empty string
        if (k > total) return "";

        string result(n, 'a');

        // Define mappings for the next smallest and greatest valid characters
        unordered_map<char, char> nextSmallest = {
            {'a', 'b'}, {'b', 'a'}, {'c', 'a'}};
        unordered_map<char, char> nextGreatest = {
            {'a', 'c'}, {'b', 'c'}, {'c', 'b'}};

        // Calculate the starting indices for strings beginning with 'a', 'b',
        // and 'c'
        int startA = 1;
        int startB = startA + (1 << (n - 1));
        int startC = startB + (1 << (n - 1));

        // Determine the first character based on the value of k
        if (k < startB) {
            result[0] = 'a';
            k -= startA;
        } else if (k < startC) {
            result[0] = 'b';
            k -= startB;
        } else {
            result[0] = 'c';
            k -= startC;
        }

        // Iterate through the remaining positions in the result string
        for (int charIndex = 1; charIndex < n; charIndex++) {
            // Calculate the midpoint of the group for the current character
            // position
            int midpoint = (1 << (n - charIndex - 1));

            // Determine the next character based on the value of k
            if (k < midpoint) {
                result[charIndex] = nextSmallest[result[charIndex - 1]];
            } else {
                result[charIndex] = nextGreatest[result[charIndex - 1]];
                k -= midpoint;
            }
        }

        return result;
    }
};
```
