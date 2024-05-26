291. Word Pattern II

Given a `pattern` and a string `s`, return `true` if `s` **matches** the `pattern`.

A string `s` **matches** a `pattern` if there is some **bijective mapping** of single characters to strings such that if each character in `pattern` is replaced by the string it maps to, then the resulting string is `s`. A **bijective mapping** means that no two characters map to the same string, and no character maps to two different strings.

 

**Example 1:**
```
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
```

**Example 2:**
```
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
```

**Example 3:**
```
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
```

**Constraints:**

* `1 <= pattern.length, s.length <= 20`
* `pattern` and `s` consist of only lowercase English letters.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 39 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(cur: str, pattern: str, mappings: dict):
            # if the pattern is empty, we've exhausted our search
            if not pattern:
                # if the string is also empty, we've found a bijective mapping
                return not cur
            # if the pattern is already mapped, we must use the provided mapping
            if pattern[0] in mappings:
                # if this isn't a valid mapping, return false
                if cur[:len(mappings[pattern[0]])] != mappings[pattern[0]]:
                    return False
                # otherwise continue backtracking
                return backtrack(cur[len(mappings[pattern[0]]):], pattern[1:], mappings)
            # try each subset of the remaining string as a mapping
            for i in range(len(cur)):
                # if the current substring maps to another value, it isn't valid
                if cur[:i+1] in mappings.values():
                    continue
                # map the pattern to the substring
                mappings[pattern[0]] = cur[:i+1]
                # backtrack
                if backtrack(cur[i+1:], pattern[1:], mappings):
                    return True
                # delete the invalid mapping
                del mappings[pattern[0]]
            # none of the substrings were valid, so there is no valid mapping
            return False
        return backtrack(s, pattern, {})
```

**Solution 2; (Hash Table and Backtracking, O(p * n^3))**
```
Runtime: 0 ms
Memory: 8.64 MB
```
```c++
class Solution {
    bool isMatch(string& s, int sIndex, string& pattern, int pIndex,
                 unordered_map<char, string>& symbolMap,
                 unordered_set<string>& wordSet) {
        // Base case: reached end of pattern
        if (pIndex == pattern.length()) {
            return sIndex == s.length(); // True iff also reached end of s
        }

        // Get current pattern character
        char symbol = pattern[pIndex];

        // This symbol already has an associated word
        if (symbolMap.find(symbol) != symbolMap.end()) {
            string word = symbolMap[symbol];
            // Check if it matches s[sIndex...sIndex + word.length()]
            if (s.compare(sIndex, word.length(), word)) {
                return false;
            }
            // If it matches continue to match the rest
            return isMatch(s, sIndex + word.length(), pattern, pIndex + 1,
                           symbolMap, wordSet);
        }

        // This symbol does not exist in the map
        for (int k = sIndex + 1; k <= s.length(); k++) {
            string newWord = s.substr(sIndex, k - sIndex);
            if (wordSet.find(newWord) != wordSet.end()) {
                continue;
            }
            // Create or update it
            symbolMap[symbol] = newWord;
            wordSet.insert(newWord);
            // Continue to match the rest
            if (isMatch(s, k, pattern, pIndex + 1, symbolMap, wordSet)) {
                return true;
            }
            // Backtracking
            symbolMap.erase(symbol);
            wordSet.erase(newWord);
        }
        // No mappings were valid
        return false;
    }
public:
    bool wordPatternMatch(string pattern, string s) {
        unordered_map<char, string> symbolMap;
        unordered_set<string> wordSet;

        return isMatch(s, 0, pattern, 0, symbolMap, wordSet);
    }
};
```

**Solution 3: (Optimized Backtracking, O(p * n * (n−p)^2))**
```
Runtime: 0 ms
Memory: 7.75 MB
```
```c++
class Solution {
    bool isMatch(string& s, int sIndex, string& pattern, int pIndex,
                 vector<string>& symbols, unordered_set<string>& wordSet) {
        // Base case: reached end of pattern
        if (pIndex == pattern.length()) {
            return sIndex == s.length(); // True if and only if also reached end of s
        }

        // Get current pattern character
        char symbol = pattern[pIndex];

        // This symbol already has an associated word
        if (!symbols[symbol - 'a'].empty()) {
            string word = symbols[symbol - 'a'];
            // Check if it matches s[sIndex...sIndex + word.length()]
            if (s.compare(sIndex, word.length(), word)) {
                return false;
            }
            // If it matches continue to match the rest
            return isMatch(s, sIndex + word.length(), pattern, pIndex + 1,
                           symbols, wordSet);
        }

        // Count the number of spots the remaining symbols in the pattern take
        int filledSpots = 0;
        for (int i = pIndex + 1; i < pattern.length(); i++) {
            char p = pattern[i];
            filledSpots += symbols[p - 'a'].empty() ? 1 : symbols[p - 'a'].length();
        }

        // This symbol does not have an associated word
        for (int k = sIndex + 1; k <= s.length() - filledSpots; k++) {
            string newWord = s.substr(sIndex, k - sIndex);
            if (wordSet.find(newWord) != wordSet.end())
                continue;
            // Create or update it
            symbols[symbol - 'a'] = newWord;
            wordSet.insert(newWord);
            // Continue to match the rest
            if (isMatch(s, k, pattern, pIndex + 1, symbols, wordSet)) {
                return true;
            }
            // Backtracking
            symbols[symbol - 'a'] = "";
            wordSet.erase(newWord);
        }
        // No mappings were valid
        return false;
    }
public:
    bool wordPatternMatch(string pattern, string s) {
        vector<string> symbols(26, "");
        unordered_set<string> wordSet;

        return isMatch(s, 0, pattern, 0, symbols, wordSet);
    }
};
```
