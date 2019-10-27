1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings `arr`. String `s` is a concatenation of a sub-sequence of `arr` which have unique characters.

Return the maximum possible length of `s`.

 

**Example 1:**
```
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
```

**Example 2:**
```
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
```

**Example 3:**
```
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
```

**Constraints:**

* `1 <= arr.length <= 16`
* `1 <= arr[i].length <= 26`
* `arr[i]` contains only lower case English letters.

# Submissions
---
**Solution 1:**
```
Runtime: 104 ms
Memory Usage: 57.9 MB
```
```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for string in arr:
            if len(set(string)) != len(string): continue
            set_string = set(string)
            for set_concatenated_string in dp[:]:
                if set_string & set_concatenated_string: continue
                dp.append(set_string | set_concatenated_string)
        return max(len(set_concatenated_string) for set_concatenated_string in dp)
```