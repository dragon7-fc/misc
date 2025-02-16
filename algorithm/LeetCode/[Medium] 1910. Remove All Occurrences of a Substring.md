1910. Remove All Occurrences of a Substring

Given two strings `s` and `part`, perform the following operation on `s` until all occurrences of the substring `part` are removed:

* Find the **leftmost** occurrence of the substring `part` and remove it from `s`.

Return `s` after removing all occurrences of `part`.

A **substring** is a contiguous sequence of characters in a string.

 

**Example 1:**
```
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
```

**Example 2:**
```
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
```

**Constraints:**

* `1 <= s.length <= 1000`
* `1 <= part.length <= 1000`
* `s` and `part` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 52 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        cur = []
        for c in s:
            cur += [c]
            while cur and len(cur) >= N and ''.join(cur[-N:]) == part:
                i = N
                while i > 0:
                    cur.pop()
                    i -= 1
        return ''.join(cur)
```

**Solution 2: (String)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        r = ''
        for ch in s:
            r = (r + ch).removesuffix(part)
        return r
```

**Solution 3: (reduce)**
```
Runtime: 36 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        return reduce(lambda a, b: (a + b).removesuffix(part), s, '')
```

**Solution 4: (String)**
```
Runtime: 0 ms
Memory: 7.1 MB
```
```c++
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int pos=s.find(part);
        while(pos!=string::npos)
        {
            s.erase(pos,part.length());
            pos=s.find(part);
        }
        return s;
    }
};
```

**Solution 3: (Stack)**
```
Runtime: 4 ms, Beats 15.12%
Memory: 12.31 MB, Beats 6.15%
```
```c++
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int m = s.size(), n = part.size(), i, k;
        string ans;
        for (i = 0; i < m; i ++) {
            ans += s[i];
            if (ans.size() >= n && ans.substr(ans.size()-n) == part) {
                k = 0;
                while (k < n) {
                    ans.pop_back();
                    k += 1;
                }
            }
        }
        return ans;
    }
};
```

**Solution 5: (KMP)**
```
Runtime: 2 ms, Beats 40.90%
Memory: 11.23 MB, Beats 10.07%
```
```c++
class Solution {
    vector<int> computeLongestPrefixSuffix(string pattern) {
        // Array to store the longest proper prefix which is also a suffix
        vector<int> lps(pattern.length(), 0);

        // Initialize tracking variables for prefix and current position
        for (int current = 1, prefixLength = 0; current < pattern.length();) {
            // If characters match, extend the prefix length
            if (pattern[current] == pattern[prefixLength]) {
                // Store the length of matching prefix
                lps[current] = ++prefixLength;
                current++;
            }
            // If characters don't match and we're not at the start of the
            // pattern
            else if (prefixLength != 0) {
                // Backtrack to the previous longest prefix-suffix
                prefixLength = lps[prefixLength - 1];
            }
            // If no match and no prefix to backtrack
            else {
                // No prefix-suffix match found
                lps[current] = 0;
                current++;
            }
        }

        // Return the computed longest prefix-suffix array
        return lps;
    }
public:
    string removeOccurrences(string s, string part) {
        // Precompute KMP longest prefix-suffix array for the pattern
        vector<int> kmpLPS = computeLongestPrefixSuffix(part);

        // Using stack to track characters and support pattern matching
        stack<char> charStack;

        // Array to store pattern matching indices during traversal
        vector<int> patternIndexes(s.length() + 1, 0);

        for (int strIndex = 0, patternIndex = 0; strIndex < s.length();
             strIndex++) {
            char currentChar = s[strIndex];
            charStack.push(currentChar);

            if (currentChar == part[patternIndex]) {
                // Track the next pattern index when characters match
                patternIndexes[charStack.size()] = ++patternIndex;

                if (patternIndex == part.length()) {
                    // Remove entire matched pattern from stack
                    int remainingLength = part.length();
                    while (remainingLength != 0) {
                        charStack.pop();
                        remainingLength--;
                    }

                    // Restore pattern index for next potential match
                    patternIndex = charStack.empty()
                                       ? 0
                                       : patternIndexes[charStack.size()];
                }
            } else {
                if (patternIndex != 0) {
                    // Backtrack pattern matching using KMP LPS
                    strIndex--;
                    patternIndex = kmpLPS[patternIndex - 1];
                    charStack.pop();
                } else {
                    // Reset pattern index tracking when no match is possible
                    patternIndexes[charStack.size()] = 0;
                }
            }
        }

        // Convert remaining stack characters to result string
        string result = "";
        while (!charStack.empty()) {
            result = charStack.top() + result;
            charStack.pop();
        }

        return result;
    }
};
```

**Solution 6: (KMP)**

    a b c
dp  0 0 0

      d a a b c b a a b c b c
                ^
k   0 0 1 1 2 3 0 1 1 2 3 
dp2   0 1 1 2 3 
      0 1       0 1       2 3
ans
      d
            daab
              da
                      dabaab
                        daba
                            dab

```
Runtime: 0 ms, Beats 100.00%
Memory: 10.26 MB, Beats 11.34%
```
```c++
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int m = s.size(), n = part.size(), i, k = 0;
        vector<int> dp(n);  // pattern index -> pattern length
        for (i = 1; i < n; i ++) {
            while (k && part[i] != part[k]) {
                k = dp[k-1];
            }
            if (part[i] == part[k]) {
                k += 1;
            }
            dp[i] = k;
        }
        
        string ans;
        vector<int> dp2(m + 1, 0);  // s index -> pattern length
        k = 0;
        for (i = 0; i < m; i++) {
            ans += s[i];
            if (s[i] == part[k]) {
                k += 1;
                dp2[ans.size()] = k;
                if (k == n) {
                    while (k) {
                        ans.pop_back();
                        k -= 1;
                    }
                    k = ans.empty()? 0 : dp2[ans.size()];
                }
            } else {
                if (k != 0) {
                    i -= 1;
                    k = dp[k - 1];
                    ans.pop_back();
                } else {
                    dp2[ans.size()] = 0;
                }
            }
        }

        return ans;
    }
};
```
