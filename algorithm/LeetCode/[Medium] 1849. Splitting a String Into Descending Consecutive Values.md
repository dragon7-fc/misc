1849. Splitting a String Into Descending Consecutive Values

You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent substrings** is equal to `1`.

* For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid.
* Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` if it is possible to split `s` as described above, or `false` otherwise.

A **substring** is a contiguous sequence of characters in a string.

 

**Example 1:**
```
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.
```

**Example 2:**
```
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
```

**Example 3:**
```
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.
```

**Example 4:**
```
Input: s = "10009998"
Output: true
Explanation: s can be split into ["100", "099", "98"] with numerical values [100,99,98].
The values are in descending order with adjacent values differing by 1.
```

**Constraints:**

* `1 <= s.length <= 20`
* `s` only consists of digits.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        
        def dfs(pre, i, r):
            if i >= N:
                if r >= 2:
                    return True
                return False
            for ni in range(i+1, N+1):
                if pre == float('inf') or int(s[i:ni]) == pre-1:
                    if dfs(int(s[i:ni]), ni, r+1):
                        return True
            return False
            
        return dfs(float('inf'), 0, 0)
```

**Solution 2: (Backtracking)**
```
Runtime: 0 ms
Memory: 6.4 MB
```
```c++
long long MX = 999999999999;
class Solution {
    bool dfs(string &s, long long prev, int idx, int cnt) {
        if(idx == s.size() ) return cnt > 1;
        long long num = 0;
        for(int i = idx; i < s.size(); i++) {
            num = num *  10l + s[i] - '0';
            if(num > MX) break;
            if(num == prev - 1 || prev == -1) {
                if(dfs(s, num, i + 1, cnt + 1)) return true;
            }
            if(num > prev && prev != -1) break;
        }
        return false;
    }
public:
    bool splitString(string s) {
        if(s.size() <= 1) return false;
        return dfs(s, -1, 0, 0);
    }
};
```
