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

**Solution 2: (Counter, Stack, mono inc stack)**

            v     z     h     o    f    n    p     o
cnt  f:1<   f:1<  f:1<  f:1<  f:1< f:0  f:0  f:0   f:0
     h:1    h:1   h:1   h:0   h:0  h:0  h:0  h:0   h:0
     n:1    n:1   n:1   n:1   n:1  n:1< n:0  n:0   n:0
     o:2    o:2   o:2   o:2   o:1  o:1  o:1< o:1<  o:0
     p:1    p:1   p:1   p:1   p:1  p:1  p:1  p:0   p:0
     v:1    v:0   v:0   v:0   v:0  v:0  v:0  v:0   v:0
     z:1    z:1   z:0   z:0   z:0  z:0  z:0  z:0   z:0
                                                     <
stk         v     vz    vzh   vzho vzho vz   vzp
ans                                f    fnoh fnoh fnohopzv
    

```
Runtime: 107 ms, Beats 21.78%
Memory: 33.72 MB, Beats 56.93%
```
```c++
class Solution {
public:
    string robotWithString(string s) {
        unordered_map<char, int> cnt;
        for (char c : s) {
            cnt[c]++;
        }

        stack<char> stk;
        string res;
        char minCharacter = 'a';
        for (char c : s) {
            stk.emplace(c);
            cnt[c]--;
            while (minCharacter != 'z' && cnt[minCharacter] == 0) {
                minCharacter++;
            }
            while (!stk.empty() && stk.top() <= minCharacter) {
                res.push_back(stk.top());
                stk.pop();
            }
        }

        return res;
    }
};
```

**Solution 3: (Stack, mono inc stack)**

    v z h o f n p o
                ^
stk f n o
        ^
dp  v z h o
        ^
ans f n o h o p z v
        ^

```
Runtime: 68 ms, Beats 36.14%
Memory: 35.56 MB, Beats 28.22%
```
```c++
class Solution {
public:
    string robotWithString(string s) {
        string stk, dp, ans;
        int i;
        for (auto c: s) {
            while (stk.size() && stk.back() > c) {
                stk.pop_back();
            }
            stk += c;
        }
        i = 0;
        for (auto c: s) {
            if (i < stk.size() && stk[i] == c) {
                ans += c;
                i += 1;
                while (dp.size() && dp.back() <= stk[i]) {
                    ans += dp.back();
                    dp.pop_back();
                }
            } else {
                dp += c;
            }
        }
        while (dp.size()) {
            ans += dp.back();
            dp.pop_back();
        }
        return ans;
    }
};
```
