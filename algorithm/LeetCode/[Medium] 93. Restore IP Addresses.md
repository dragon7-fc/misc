93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

**Example:**
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

# Submissions
---
**Solution 1: (Backtracking)**
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
