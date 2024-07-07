3211. Generate Binary Strings Without Adjacent Zeros

You are given a positive integer `n`.

A binary string `x` is **valid** if all **substrings** of `x` of length `2` contain at least one `"1"`.

Return all **valid** strings with length `n`, in any order.

 

**Example 1:**
```
Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".
```

**Example 2:**
```
Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".
```
 

**Constraints:**

* `1 <= n <= 18`

# Submissions
---
**Solution 1: (Bitmask)**
```
Runtime: 31 ms
Memory: 13.36 MB
```
```c++
class Solution {
public:
    vector<string> validStrings(int n) {
        int b;
        string pre;
        bool flag;
        vector<string> ans;
        for (int a = 0; a < 1<<n; a++) {
            b = (1<<n) + a;
            pre = "";
            flag = true;
            while (b != 1) {
                if (pre != "" && pre.back() == '0' && b%2 == 0) {
                    flag = false;
                    break;
                } 
                pre += b%2 + '0';
                b >>= 1;
            }
            if (flag) {
                ans.push_back(pre);
            }
        }
        return ans;
    }
};
```

**Solution 2: (Backtracking)**
```
Runtime: 11 ms
Memory: 21.59 MB
```
```c++
class Solution {
    vector<string> ans;
    void bt(int prev, string &str, int n){
        if(str.length() == n){
            ans.push_back(str);
            return;
        }
        str.push_back('1');
        bt(1, str, n);
        str.pop_back();
        if(prev == 1){
            str.push_back('0');
            bt(0, str, n);
            str.pop_back();
        } 
    }
public:
    vector<string> validStrings(int n) {
        string a = "0", b = "1";
        bt(0, a, n);
        bt(1, b, n);
        return ans;
    }
};
```
