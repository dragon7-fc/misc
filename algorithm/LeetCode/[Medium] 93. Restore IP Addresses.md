93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

# Submissions
---
> **Solution 1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(digits, ip):     
            if len(ip) >= 4:
                if len(digits) == 0:
                    ans.append('.'.join(ip))
                return
            for i in range(1, min(len(digits)+1, 4)):
                if int(digits[:i]) > 255 or int(digits[:i]) < 0 or (i > 1 and digits[0] == '0'):
                    continue 
                backtrack(digits[i:], ip + [digits[:i]])
                
        backtrack(s, [])
        return ans
```

**Solution 2: (Backtracking)**
```
Runtime: 4 ms
Memory Usage: 15.7 MB
```
```c++
class Solution {
    void helper(string s,int index, string res,int count,vector<string> &ans)
    {
        if(index>= s.length())
        {
            if(count==4){
                res = res.substr(0,res.length()-1);
                ans.push_back(res);
            }
            return;
        }
       
        if(s[index] == '0')
        {
            helper(s,index+1,res+"0.",count+1,ans);
        }
        else
        {
            helper(s,index+1,res+s[index]+".",count+1,ans);
            if(index+2<=s.length())
                helper(s,index+2,res+s[index]+s[index+1]+".",count+1,ans);
            if(index+3<=s.length() && stoi(s.substr(index,3))<=255)
                helper(s,index+3,res+s[index]+s[index+1]+s[index+2]+".",count+1,ans);
        }
        return;
    }
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        if(s.length()<4 || s.length()>12)
            return ans;
        
        helper(s,0,"",0,ans);
        return ans;
    }
};
```

**Solution 3: (Backtracking)**
```
Runtime: 39 ms
Memory: 13.8 MB
```
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        ans = []

        def bt(i, p):
            nonlocal ans
            if len(p) > 4:
                return
            if i == N:
                if len(p) == 4:
                    ans += ['.'.join(p)]
                return
            if s[i] == '0':
                bt(i+1, p+["0"])
            else:
                for j in range(i+1, min(i+4 ,N+1)):
                    if 0 <= int(s[i:j]) <= 255:
                        bt(j, p+[s[i:j]])

        bt(0, [])
        return ans
```

**Solution 4: (Backtracking)**
```
Runtime: 0 ms
Memory: 7 MB
```
```c++
class Solution {
    bool valid(const string& s, int start, int length) {
        return length == 1 || (s[start] != '0' && (length < 3 || s.substr(start, length) <= "255"));
    }

    void helper(const string& s, int startIndex, vector<int>& dots, vector<string>& ans) {
        const int remainingLength = s.length() - startIndex;
        const int remainingNumberOfIntegers = 4 - dots.size();

        if (remainingLength > remainingNumberOfIntegers * 3 ||
            remainingLength < remainingNumberOfIntegers) {
            return;
        }
        if (dots.size() == 3) {
            if (valid(s, startIndex, remainingLength)) {
                string temp;
                int last = 0;
                for (int dot : dots) {
                    temp.append(s.substr(last, dot));
                    last += dot;
                    temp.append(".");
                }
                temp.append(s.substr(startIndex));
                ans.push_back(temp);
            }
            return;
        }
        for (int curPos = 1; curPos <= 3 && curPos <= remainingLength; ++curPos) {
            // Append a dot at the current position.
            dots.push_back(curPos);
            // Try making all combinations with the remaining string.
            if (valid(s, startIndex, curPos)) {
                helper(s, startIndex + curPos, dots, ans);
            }
            // Backtrack, i.e. remove the dot to try placing it at the next position.
            dots.pop_back();
        }
    }
public:
    vector<string> restoreIpAddresses(string s) {
         vector<int> dots;
        vector<string> ans;
        helper(s, 0, dots, ans);
        return ans;
    }
};
```

**Solution 5: (Iterative)**
```
Runtime: 4 ms
Memory: 6.7 MB
```
```c++
class Solution {
    bool valid(const string& s, int start, int length) {
        return length == 1 || (s[start] != '0' && (length < 3 || s.substr(start, length) <= "255"));
    }
public:
    vector<string> restoreIpAddresses(string s) {
         vector<string> ans;
        int length = s.length();
        for (int len1 = max(1, length - 9); len1 <= 3 && len1 <= length - 3; ++len1) {
            if (!valid(s, 0, len1)) {
                continue;
            }
            for (int len2 = max(1, length - len1 - 6); len2 <= 3 && len2 <= length - len1 - 2;
                 ++len2) {
                if (!valid(s, len1, len2)) {
                    continue;
                }
                for (int len3 = max(1, length - len1 - len2 - 3);
                     len3 <= 3 && len3 <= length - len1 - len2 - 1; ++len3) {
                    if (valid(s, len1 + len2, len3) &&
                        valid(s, len1 + len2 + len3, length - len1 - len2 - len3)) {
                        ans.push_back(s.substr(0, len1) + "." + s.substr(len1, len2) + "." +
                                      s.substr(len1 + len2, len3) + "." +
                                      s.substr(len1 + len2 + len3));
                    }
                }
            }
        }
        return ans;
    }
};
```
