2067. Number of Equal Count Substrings

You are given a **0-indexed** string `s` consisting of only lowercase English letters, and an integer `count`. A **substring** of `s` is said to be an **equal count substring** if, for each **unique** letter in the substring, it appears exactly `count` times in the substring.

Return the number of **equal count substrings** in `s`.

A **substring** is a contiguous non-empty sequence of characters within a string.

 

**Example 1:**
```
Input: s = "aaabcbbcc", count = 3
Output: 3
Explanation:
The substring that starts at index 0 and ends at index 2 is "aaa".
The letter 'a' in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is "bcbbcc".
The letters 'b' and 'c' in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is "aaabcbbcc".
The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
```

**Example 2:**
```
Input: s = "abcd", count = 2
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
```

**Example 3:**
```
Input: s = "a", count = 5
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0
```

**Constraints:**

* `1 <= s.length <= 3 * 10^4`
* `1 <= count <= 3 * 10^4`
* `s` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Sliding Window)**
```
Runtime: 2812 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        if count > len(s):
            return 0
        
        ans = 0
        
        n = len(s)
        uniqueChars = len(set(s))
        
        for uniqueLimit in range(1,uniqueChars+1):
            slidingWindow = defaultdict(int)
            
            left = 0
            for right in range(n):
                slidingWindow[s[right]] += 1
                
                while len(slidingWindow) > uniqueLimit or slidingWindow[s[right]] > count:
                    slidingWindow[s[left]] -= 1
                    if slidingWindow[s[left]] == 0:
                        del slidingWindow[s[left]]
                    left += 1
                        
                if len(slidingWindow) == uniqueLimit and \
                    all(value == count for value in slidingWindow.values()):
                    ans +=1
                    
        return ans
```
