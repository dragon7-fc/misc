2381. Shifting Letters II

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [starti, endi, directioni]`. For every `i`, shift the characters in `s` from the index `starti` to the index `endi` (inclusive) forward if `directioni = 1`, or shift the characters backward if `directioni = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return the final string after all such shifts to s are applied.

 

**Example 1:**
```
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
```

**Example 2:**
```
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
```

**Constraints:**

* `1 <= s.length, shifts.length <= 5 * 104`
* `shifts[i].length == 3`
* `0 <= starti <= endi < s.length`
* `0 <= directioni <= 1`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Prefix sum)**
```
Runtime: 5101 ms
Memory Usage: 39.5 MB
```
```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[end+1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[end+1] -= 1
        
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s
```

**Solution 2: (Prefix sum, counter)**

    a   b  c   [0,1,0],[1,2,1],[0,2,1]
    -------    -----------------------
          m-1                   n-1
cnt
    -1     1
       1     -1
    1        -1
cur 0  1   2 
    a  c   e

    [0,0,0],[1,1,1]
      ^
    d   z   t   z
    ------------
    -1  1    
        1  -1
    -1 0   -1

```
Runtime: 4 ms
Memory: 98.68 MB
```
```c++
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int m = s.size(), n = shifts.size(), i, cur = 0;
        vector<int> cnt(m+1);
        string ans;
        for (i = 0; i < n; i ++) {
            if (shifts[i][2]) {
                cnt[shifts[i][0]] += 1;
                cnt[shifts[i][1]+1] -= 1;
            } else {
                cnt[shifts[i][0]] -= 1;
                cnt[shifts[i][1]+1] += 1;
            }
        }
        for (i = 0; i < m; i ++) {
            cur += cnt[i];
            ans += string(1, 'a' + ((s[i] - 'a' + cur)%26 + 26)%26);
        }
        return ans;
    }
};
```
