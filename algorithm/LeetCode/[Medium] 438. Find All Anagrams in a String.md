438. Find All Anagrams in a String

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s** and **p** will not be larger than `20,100`.

The order of output does not matter.

**Example 1:**
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

# Submissions
---
**Solution 1:**
```
Runtime: 172 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_counter = collections.Counter(p)
        running_counter = collections.Counter()
        len_p = len(p)
        result = []

        for i in range(len(s)):
            
            # If index  >= length of the pattern.
            # then decrement the count of the (i - len_p)th character to remove it from 
            # the current (sliding) window.
            if i >= len_p:
                if running_counter[s[i - len_p]] == 1:
                    del running_counter[s[i  - len_p]]
                else:
                    running_counter[s[i - len_p]] -= 1
            
            # Default: just increment the count of the current character.
            running_counter[s[i]] += 1
            
            # At any time, if running_counter == pattern_counter then append the result.
            if running_counter == pattern_counter:
                result.append(i - len_p + 1)

        return result
```