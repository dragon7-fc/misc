467. Unique Substrings in Wraparound String

Consider the string `s` to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so `s` will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string `p`. Your job is to find out how many unique non-empty substrings of `p` are present in `s`. In particular, your input is the string `p` and you need to output the number of different non-empty substrings of `p` in the string s.

**Note:** `p` consists of only lowercase English letters and the size of `p` might be over 10000.

**Example 1:**
```
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
```

**Example 2:**
```
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
```

**Example 3:**
```
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
```

# Submissions
---
**Solution 1: (DFS, Time Limit Exceeded)**
```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        N = len(p)
        if N == 0: return 0
        ans = set()
        
        def dfs(i, path):
            ans.add(path)
            if i == N:
                return
            if ord(p[i]) - ord(p[i-1]) == 1 or p[i] == 'a' and p[i-1] == 'z':
                dfs(i+1, path+p[i])
            dfs(i+1, p[i])
            
        dfs(1, p[0])
        return len(ans)
        
        
```

**Solution 2: (DP Bottom-Up)**
```
Runtime: 104 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        L = len(p)
        if L == 0: return 0
        DP = [1] * L
        dic = collections.defaultdict(int)
        dic[p[0]] = 1
        for i in range(1, L):
            if ord(p[i]) - ord(p[i-1]) == 1 or (p[i] == 'a' and p[i-1] == 'z'):
                DP[i] = DP[i-1] + 1
            else:
                DP[i] = 1
            dic[p[i]] = max(dic[p[i]], DP[i])
        return sum(dic.values())
```

**Solution 3: (DP Bottom-Up)**
```
Runtime: 88 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {i: 1 for i in p}
        n = 1
        for i, j in zip(p, p[1:]):
            n = n + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], n)
        return sum(res.values())
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 4 ms
Memory Usage: 7.2 MB
```
```c++
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int> dp(26, 0);
    
        int i, count = 1;

        for(i=0; i < p.size(); i++)
        {

            if( i> 0 && (p[i-1]-p[i] == 25 || p[i]-p[i-1] == 1))
            {

                count++;
            }
            else{

                count = 1;
            }

            dp[p[i] - 'a'] = max(count, dp[p[i] - 'a']);
        }

        int ans = 0;

        for(int it : dp )
        {
            ans += it;
        }

        return ans;
    }
};
```
