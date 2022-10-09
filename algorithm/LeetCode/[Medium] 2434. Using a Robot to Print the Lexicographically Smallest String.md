2434. Using a Robot to Print the Lexicographically Smallest String

You are given a string `s` and a robot that currently holds an empty string `t`. Apply one of the following operations until `s` and `t` **are both empty**:

* Remove the **first** character of a string `s` and give it to the robot. The robot will append this character to the string `t`.
* Remove the **last** character of a string `t` and give it to the robot. The robot will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.

 

**Example 1:**
```
Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
```

**Example 2:**
```
Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
```

**Example 3:**
```
Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
```

**Constraints:**

* 1 <= s.length <= 10^5`
* `s` consists of only English lowercase letters.

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 4283 ms
Memory: 17.8 MB
```
```python
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt, t, ans = Counter(s), [], []
        for c in s:
            t.append(c)
            if cnt[c] == 1:
                del cnt[c]
            else:
                cnt[c] -= 1
            while cnt and t and min(cnt) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return ''.join(ans)
```

**Solution 2: (Stack)**
```
Runtime: 202 ms
Memory: 29.7 MB
```
```c++
class Solution {
    char low(vector<int> & freq){    // this function return the smallest char present
        for(int i=0;i<26;i++){
            if(freq[i]!=0)return 'a'+i;
        } 
        return 'a';   
    }
public:
    string robotWithString(string s) {
        stack<char> t;
        string ans="";  
        vector<int> freq(26,0);
        for(char c:s){
            freq[c-'a']++;
        }
        
        for(char c:s){
            t.push(c);
            freq[c-'a']--; 
            while(t.size()>0 && t.top()<=low(freq)){
                char x = t.top(); 
                ans += x;
                t.pop();  
            }    
        }
         while(t.size()>0){
             ans += t.top();
             t.pop();   
        }
        return ans;
    }
};
```
