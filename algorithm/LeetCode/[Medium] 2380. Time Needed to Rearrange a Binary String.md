2380. Time Needed to Rearrange a Binary String

You are given a binary string `s`. In one second, all occurrences of `"01`" are simultaneously replaced with `"10"`. This process repeats until no occurrences of `"01"` exist.

Return the number of seconds needed to complete this process.

 

**Example 1:**
```
Input: s = "0110101"
Output: 4
Explanation: 
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.
```

**Example 2:**
```
Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.
```

**Constraints:**

* `1 <= s.length <= 1000`
* `s[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 222 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while s.find("01") >= 0:
            s = s.replace("01","10")
            ans += 1
        return ans
        
```

**Solution 2: (Greedy)**

* Time: O(n * n) - OK for n <= 1,000. We process n characters in the string n times in the worst case (0111...1).
* Memory: O(n) to store an interim string.

```
Runtime: 0 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int secondsToRemoveOccurrences(string s) {
        int zeros = 0, seconds = 0;
        for (int i = 0; i < s.size(); ++i) {
            zeros += s[i] == '0';
            if (s[i] == '1' && zeros)
                seconds = max(seconds + 1, zeros);
        }
        return seconds;
    }
};
```
