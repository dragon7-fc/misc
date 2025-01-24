1593. Split a String Into the Max Number of Unique Substrings

Given a string `s`, return the maximum number of unique substrings that the given string can be split into.

You can split string `s` into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

**Example 1:**
```
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
```

**Example 2:**
```
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
```

**Example 3:**
```
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
```

**Constraints:**

* `1 <= s.length <= 16`

* `s` contains only lower case English letters.

# Submissions
---
**Solution 1: (Backtracking, Post Order)**
```
Runtime: 328 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        
        def dfs(s):
            ans = 0
            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        ans = max(ans, 1 + dfs(s[i:]))
                        seen.remove(candidate)
            return ans
        
        return dfs(s)     
```

**Solution 2: (Backtracking)**
```
Runtime: 368 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        ans = 1
        seen = set()
        
        def dfs(i):
            nonlocal ans 
            if i == N:
                ans = max(ans, len(seen))
                return
            for j in range(i+1, N+1): 
                if s[i:j] not in seen: 
                    seen.add(s[i:j])
                    dfs(j)
                    seen.remove(s[i:j])
            
        dfs(0)
        return ans
```

**Solution 3: (Bitmask)**
```
Runtime: 980 ms
Memory: 252.60 MB
```
```c++
class Solution {
public:
    int maxUniqueSplit(string s) {
        int n = s.size(), j, ans = 0;
        unordered_set<string> st;
        string cur;
        bool flag;
        for (int i = 0; i < (1<<n); i ++) {
            j = 0;
            flag = true;
            while (j < n) {
                cur = s[j];
                while (j+1 < n && (((i>>(j+1))&1) == ((i>>j)&1))) {
                    cur += s[j+1];
                    j += 1;
                }
                if (st.count(cur) || st.size() + (n-j) < ans) {
                    flag = false;
                    break;
                }
                st.insert(cur);
                j += 1;
            }
            if (flag) {
                ans = max(ans, (int)st.size());
            }
            st.clear();
        }
        return ans;
    }
};
```

**Solution 4: (Backtracking with Pruning, O(n * 2^n))**
```
Runtime: 15 ms
Memory: 12.72 MB
```
```c++
class Solution {
    void backtrack(const string& s, int i, unordered_set<string>& seen,
                   int count, int& maxCount) {
        // Prune: If the current count plus remaining characters can't exceed
        // maxCount, return
        if (count + (s.size() - i) <= maxCount) return;

        // Base case: If we reach the end of the string, update maxCount
        if (i == s.size()) {
            maxCount = max(maxCount, count);
            return;
        }

        // Try every possible substring starting from 'start'
        string substring = "";
        for (int j = i; j <= s.size()-1; j ++) {
            substring += s[j];
            // If the substring is unique
            if (!seen.count(substring)) {
                // Add the substring to the seen set
                seen.insert(substring);
                // Recursively count unique substrings from the next position
                backtrack(s, j+1, seen, count + 1, maxCount);
                // Backtrack: remove the substring from the seen set
                seen.erase(substring);
            }
        }
    }
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> seen;
        int maxCount = 0;
        backtrack(s, 0, seen, 0, maxCount);
        return maxCount;
    }
};
```
