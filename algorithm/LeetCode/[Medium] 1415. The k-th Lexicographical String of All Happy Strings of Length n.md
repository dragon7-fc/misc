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

**Solution 2: (Backtracking, O(n * 2^n))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 7.90 MB, Beats 95.26%
```
```c++
class Solution {
    bool bt(int n, int &k, string &cur) {
        if (cur.size() == n) {
            k -= 1;
            if (k == 0) {
                return true;
            } else {
                return false;
            }
        }
        for (int i = 0; i < 3; i ++) {
            if (cur == "" || i != cur.back()-'a') {
                cur += i+'a';
                if (bt(n, k, cur)) {
                    return true;
                }
                cur.pop_back();
            }
        }
        return false;
    }
public:
    string getHappyString(int n, int k) {
        string ans;
        bt(n, k, ans);
        return ans;
    }
};
```

**Solution 3: (Math, O(n))**

       n = 3, k = 9
---------------------
total  12
startA  1
startB  1 + 4 = 5
startC  5 + 4 = 9

k       9 0 0 0
mid         2 1
result    c a b

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
