1930. Unique Length-3 Palindromic Subsequences

Given a string `s`, return the number of **unique palindromes of length three** that are a **subsequence** of `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

* For example, `"ace"` is a subsequence of `"abcde"`.
 

**Example 1:**
```
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
```

**Example 2:**
```
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
```

**Example 3:**
```
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
```

**Constraints:**

* `3 <= s.length <= 10^5`
* `s` consists of only lowercase English letters.

# Submissions
---
**Solution 1: (String, Set, Brute Force)**
```
Runtime: 220 ms
Memory Usage: 15 MB
```
```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res
```

**Solution 2: (Prefix Sum, counter, left and right)**
```
Runtime: 849 ms
Memory: 17.13 MB
```
```c++
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size(), i, j;
        vector<int> cur(26), right(26);
        unordered_set<string> st;
        for (i = n-1; i >= 2; i --) {
            right[s[i]-'a'] += 1;
        }
        cur[s[0]-'a'] += 1;
        for (i = 1; i < n-1; i ++) {
            for (j = 0; j < 26; j ++) {
                if (cur[j] && right[j]) {
                    st.insert(string(1, 'a'+j) + string(1, s[i]));
                }
            }
            cur[s[i]-'a'] += 1;
            right[s[i+1]-'a'] -= 1;
        }
        return st.size();
    }
};
```

**Solution 3: (Count Letters In-Between)**
```
Runtime: 300 ms
Memory: 13.4 MB
```
```c++
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<char> letters;
        for (char c : s) {
            letters.insert(c);
        }
        
        int ans = 0;
        for (char letter : letters) {
            int i = -1;
            int j = 0;
            
            for (int k = 0; k < s.size(); k++) {
                if (s[k] == letter) {
                    if (i == -1) {
                        i = k;
                    }
                    
                    j = k;
                }
            }
            
            unordered_set<char> between;
            for (int k = i + 1; k < j; k++) {
                between.insert(s[k]);
            }
            
            ans += between.size();
        }
        
        return ans;
    }
};
```

**Solution 4: (Prefix Sum, Counter)**
```
Runtime: 215 ms, Beats 26.52%
Memory: 21.10 MB, Beats 14.16%
```
```c++
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size(), i, j, pj, ci, ans = 0;
        char c;
        vector<vector<bool>> visited(26, vector<bool>(26));
        vector<deque<int>> pre(26);
        for (i = 0; i < n; i ++) {
            c = s[i];
            ci = c - 'a';
            if (pre[ci].size()) {
                if (pre[ci].size() == 2) {
                    visited[ci][ci] = true;
                }
                pj = pre[ci].back();
                for (j = 0; j < 26; j ++) {
                    if (ci != j && pre[j].size() && pre[j].back() > pj) {
                        visited[ci][j] = true;
                    }
                }
            }
            if (pre[ci].size() == 2) {
                pre[ci].pop_front();
            }
            pre[ci].push_back(i);
        }
        for (i = 0; i < 26; i ++) {
            for (j = 0; j < 26; j ++) {
                ans += visited[i][j];
            }
        }
        return ans;
    }
};
```

**Solution 5: (Pre-Compute First and Last Indices)**

    a a b c a
   -----------
    0 1 2 3 4
a   ^ . . . ^

    b b c b a b a
   ---------------
    0 1 2 3 4 5 6
a           ^ . ^
b   ^ . .   . ^

```
Runtime: 143 ms, Beats 77.75%
Memory: 15.91 MB, Beats 58.20%
```
```c++
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> first = vector(26, -1);
        vector<int> last = vector(26, -1);
        
        for (int i = 0; i < s.size(); i++) {
            int curr = s[i] - 'a';
            if (first[curr] == - 1) {
                first[curr] = i;
            }
            
            last[curr] = i;
        }
        
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) {
                continue;
            }
            
            unordered_set<char> between;
            for (int j = first[i] + 1; j < last[i]; j++) {
                between.insert(s[j]);
            }
            
            ans += between.size();
        }
        
        return ans;
    }
};
```
