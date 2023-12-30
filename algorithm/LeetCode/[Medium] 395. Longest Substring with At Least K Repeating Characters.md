395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring **T** of a given string (consists of lowercase letters only) such that every character in **T** appears no less than k times.

**Example 1:**
```
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```

**Example 2:**
```
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

# Submissions
---
**Solution: (Sliding Window)**
```
Runtime: 0 ms
Memory Usage: 6.3 MB
```
```c++
class Solution {
    // get the maximum number of unique letters in the string s
    int getMaxUniqueLetters(string s) {
        bool map[26] = {0};
        int maxUnique = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!map[s[i] - 'a']) {
                maxUnique++;
                map[s[i] - 'a'] = true;
            }
        }
        return maxUnique;
    }
public:
    int longestSubstring(string s, int k) {
        int countMap[26];
        int maxUnique = getMaxUniqueLetters(s);
        int result = 0;
        for (int currUnique = 1; currUnique <= maxUnique; currUnique++) {
            // reset countMap
            memset(countMap, 0, sizeof(countMap));
            int windowStart = 0, windowEnd = 0, idx = 0, unique = 0, countAtLeastK = 0;
            while (windowEnd < s.size()) {
                // expand the sliding window
                if (unique <= currUnique) {
                    idx = s[windowEnd] - 'a';
                    if (countMap[idx] == 0) unique++;
                    countMap[idx]++;
                    if (countMap[idx] == k) countAtLeastK++;
                    windowEnd++;
                }
                // shrink the sliding window
                else {
                    idx = s[windowStart] - 'a';
                    if (countMap[idx] == k) countAtLeastK--;
                    countMap[idx]--;
                    if (countMap[idx] == 0) unique--;
                    windowStart++;
                }
                if (unique == currUnique && unique == countAtLeastK)
                    result = max(windowEnd - windowStart, result);
            }
        }

        return result;
    }
};
```

**Solution 1: (Stack)**
```
Runtime: 36 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        ans = 0
        while stack:
            string = stack.pop()
            for char in set(string):
                if string.count(char) < k:
                    stack.extend(substring for substring in string.split(char))
                    break
            else:
                ans = max(ans, len(string))
        return ans
```

**Solution 2: (String, DFS)**
```
Runtime: 52 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        cnt = collections.Counter(s)
        minChar = min(cnt, key = cnt.get)
        if cnt[minChar] >= k:
            return len(s)
        return max(self.longestSubstring(substring, k) for substring in s.split(minChar))
```

**Solution 3: (Sliding Window, DFS)**
```
Runtime: 11 ms
Memory Usage: 6.8 MB
```
```c++
class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.size();
        if (n < k) {
            return 0;
        }
        unordered_map<char,int>m;
        for (auto x: s) {
            m[x] += 1;
        }
        int j = 0;
        while (j < n && m[s[j]] >= k) {
            j += 1;
        }
        if (j >= n-1) {
            return j;
        }
        int c1 = longestSubstring(s.substr(0, j), k);
        while (j < n && m[s[j]] < k) {
            j += 1;
        }
        int c2 = longestSubstring(s.substr(j), k);
        return max(c1, c2);
    }
};
```
