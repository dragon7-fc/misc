316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

**Example 1:**
```
Input: "bcabc"
Output: "abc"
```

**Example 2:**
```
Input: "cbacdcbc"
Output: "acdb"
```

**Note:** This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# Submissions
---
**Solution 1: (Greedy, Stack, Monotonic stack)**
```
Runtime: 4 ms
Memory Usage: 7.1 MB
```
```c++
class Solution {
public:
    string removeDuplicateLetters(string s) {
        int cnt[256]={0};
        vector<int> vis(256,false);
        for(auto it:s)
            cnt[it]++;
        int n=s.length();
        string ans="0";
        for(int i=0;i<n;i++)
        {
            cnt[s[i]]--;
            if(vis[s[i]])continue;
            while(s[i]<ans.back() and cnt[ans.back()])
            {
                vis[ans.back()]=false;
                ans.pop_back();
            }
            ans+=s[i];
            vis[s[i]]=true;  // s[i] in stack
        }
        return ans.substr(1,string::npos);
    }
};
```

**Solution 2: (Greedy, Greedy add with count and visited, Stack)**
```
Runtime: 32 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        cnt = collections.Counter(s)
        visited = collections.defaultdict(int)
        ans = "0"
        for i in range(N):
            cnt[s[i]] -= 1
            if visited[s[i]]: continue
            while s[i] < ans[-1] and cnt[ans[-1]]:
                visited[ans[-1]] = 0
                ans = ans[:-1]
            ans += s[i]
            visited[s[i]] = 1

        return ans[1:]
```
