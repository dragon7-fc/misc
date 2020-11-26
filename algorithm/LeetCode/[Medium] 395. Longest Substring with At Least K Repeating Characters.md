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

**Solution 3: (Sliding Window)**
```
Runtime: 4 ms
Memory Usage: 6.2 MB
```
```c++
class Solution {
public:
    int longestSubstring(string s, int k) {
        int i=0,j=s.length()-1,left=0,right=s.length()-1;
        vector<int>f(26,0);
        for(auto c:s){f[c-'a']++;}
        while(i<=j){
            if(f[s[i]-'a']<k){
            while(left<=i){f[s[left++]-'a']--;}
            i++;j=right;
            }
            else if(f[s[j]-'a']<k){
                while(right>=j){f[s[right--]-'a']--;}
                j--;i=left;
            }
            else{
                i++;
                j--;
            }
        }
        return right-left+1;
    }
};
```