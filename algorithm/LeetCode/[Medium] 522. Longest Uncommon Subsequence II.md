522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A **subsequence** is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

**Example 1:**
```
Input: "aba", "cdc", "eae"
Output: 3
```

**Note:**

* All the given strings' lengths will not exceed 10.
* The length of the given list will be in the range of `[2, 50]`.

# Submissions
---
**Solution 1: (Counter, String, Sort, Brute Force)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Checks if string `a` is a subsequence of `b`
        def subseq(a, b):
            if len(a) >= len(b):
                return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)
        
        count = collections.Counter(strs)
        # Exlude all strings that occure in `strs` more than once
        exclude = [s for s, c in count.items() if c > 1]
        
        # Rest of the strings go to `check` array
        check = [s for s, c in count.items() if c == 1]
        # Sort by length from longest to shortest
        check.sort(key = lambda x: len(x), reverse = True)
        
        # If there are no items in exclude than longest strings is the answer
        if not exclude:
            return len(check[0])
        
        # Otherwise we need to check remaining strings one by one
        for s in check:
            # Check if string is subsequece of one of excluded
            for e in exclude:
                if subseq(s, e):
                    # If subsequence than mark current string as also exluded and go to next one
                    exclude.append(s)
                    break
                else:
                    # If not a subsequence than it's length is the answer
                    return len(s)
        
        return -1
```

**Solution 2: (Counter, String, Sort, Brute Force)**

1. First, we keep the frequencies of all strings in a map. That's because we know that a string that has a duplicate can never be the longest uncommon subsequence.
1. Sort the string by length - from longest to shortest.
1. We iterate through the strings. If this word has a duplicate, continue.
  If not, we call the function checkSubsUptoI, which checks if the current string is a subsequence of any of the previous strings. 
  If it's not - this will be our LUS, return its size.
  Otherwise continue iterating.
  If we got to the end with no result - return -1.

```
Runtime: 3 ms
Memory Usage: 8.4 MB
```
```c++
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        unordered_map<string, int> freq;
        for (auto str : strs) freq[str]++;
        
        sort(strs.begin(), strs.end(), compare);
        
        for (int i = 0; i < strs.size(); i++) {
            if (freq[strs[i]] > 1) continue;
            if (!checkSubsUptoI(strs, strs[i], i-1)) return strs[i].size();
        }
        return -1;
    }
    
    static bool compare(string& a, string& b) {
        return a.size() > b.size();
    }
    
    bool isSubsequence(string s, string t) {
        int s_i = 0, t_i = 0;
        
        while (s_i < s.size() && t_i < t.size()) {
            if (s[s_i] == t[t_i]) s_i++; 
            t_i++;
        }
        
        return s_i == s.size();
    }
    
    bool checkSubsUptoI(vector<string>& strs, string sub, int idx) {
        for (int i = 0; i <= idx; i++) {
            if (isSubsequence(sub, strs[i])) return true;
        }
        return false;
    }
};
```
