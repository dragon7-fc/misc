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
**Solution 1: (DP)**
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

**Solution 2: (Backtracking)**
```
Runtime: 108 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def hasDuplicates(s):
            return len(s) > len(set(s))
        def backtrack(index, path):
            self.ans = max(self.ans, len(path))
            if index == len(arr):
                return
            for i in range(index, len(arr)):
                if not hasDuplicates(path + arr[i]):
                    backtrack(i + 1, path + arr[i])
        if not arr:
            return 0
        self.ans = 0
        backtrack(0, '')
        
        return self.ans
```

**Solution 3: (DFS)**
```
Runtime: 124 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def maxLenRec(used, index):
            if index == len(arr):
                return 0
            maxLen = maxLenRec(used, index + 1)  # leave it
            s = arr[index]
            valid, currUsed = len(set(s)) == len(s), set(s)
            if valid and len(used & currUsed) == 0:  # take it if possible
                maxLen = max(maxLen, len(s) + maxLenRec(used | currUsed, index + 1))
            return maxLen

        return maxLenRec(set(), 0)
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory: 9.7 MB
```
```c++
class Solution {
public:
    int maxLength(vector<string>& arr) {
        int max_len = 0;
        
        // [1] we should first throw away all strings with any
        //    duplicate characters; strings with all unique 
        //    characters are the subsets of the alphabet, thus,
        //    can be encoded using binary form
        vector<bitset<26>> unique;
        for (auto s : arr)
        {
            bitset<26> bin;
            for (char ch : s) bin.set(ch - 'a');
            if (bin.count() == s.size())
                unique.push_back(bin);
        }
        
        // [2] now start with an empty concatenation and iteratively
        //    increase its length by trying to add more strings
        vector<bitset<26>> concat = {bitset<26>()};
        for (auto& u : unique)
            for (int i = concat.size() - 1; i >= 0; i--)
                if ((concat[i] & u).none())
                {
                    concat.push_back(concat[i] | u);
                    max_len = max(max_len, (int)(concat[i].count() + u.count()));
                }
        
        return max_len;
    }
};
```

**Solution 5: (DP Bottom-Up)**
```
Runtime: 0 ms
Memory: 10.41 MB
```
```c++
class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<int> dp = {0};
        int res = 0;
        
        for (const string& s : arr) {
            int a = 0, dup = 0;
            for (char c : s) {
                dup |= a & (1 << (c - 'a'));
                a |= 1 << (c - 'a');
            }
            
            if (dup > 0)
                continue;
            
            for (int i = dp.size() - 1; i >= 0; i--) {
                if ((dp[i] & a) > 0)
                    continue;
                dp.push_back(dp[i] | a);
                res = max(res, __builtin_popcount(dp[i] | a));
            }
        }
        
        return res;
    }
};
```
