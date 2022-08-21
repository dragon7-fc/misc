2384. Largest Palindromic Number

You are given a string num consisting of digits only.

Return the **largest palindromic** integer (in the form of a string) that can be formed using digits taken from `num`. It should not contain **leading zeroes**.

Notes:

* You do **not** need to use all the digits of `num`, but you must use **at least** one digit.
* The digits can be reordered.
 

**Example 1:**
```
Input: num = "444947137"
Output: "7449447"
Explanation: 
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.
```

**Example 2:**
```
Input: num = "00009"
Output: "9"
Explanation: 
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.
```

**Constraints:**

* `1 <= num.length <= 10^5`
* `num` consists of digits.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 71 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')
        mid = max(count[i] % 2 * i for i in count)
        return (res + mid + res[::-1]) or '0'
```

**Solution 2: (Counter)**
```
Runtime: 45 ms
Memory Usage: 13.2 MB
```
```c++
class Solution {
public:
    string largestPalindromic(string num) {
        vector<int> v(10);
        for(char c:num)v[c-'0']++;
        string ans;
        int single=-1;
        for(int i=9;i>=0;i--){
            if(ans.empty() && i==0) continue;
            while(v[i]>1){
                ans.push_back(i+'0');
                v[i]-=2;
            }
            if(v[i]==1 && single==-1)single=i;
        }
        string res=string(ans.rbegin(),ans.rend());
        if(ans.empty() && single==-1) return "0";
        if(single!=-1)
            ans.push_back(single+'0');
        ans+=res;
        return ans;
    }
};
```
