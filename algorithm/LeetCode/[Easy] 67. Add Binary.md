67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 16 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)
        return bin(num_a+num_b)[2:]
```

**Solution 2: (Math)**
```
Runtime: 8 ms
Memory Usage: 7.1 MB
```
```c++
class Solution {
public:
    string addBinary(string a, string b) {
        int p = a.length()-1, q = b.length()-1;
        string ans ="";
        int carry = 0;
        while(p >= 0 || q >= 0 || carry == 1) {
            int m = p>=0 ? (a[p--]-'0') : 0;
            int n = q>=0 ? (b[q--]-'0') : 0;
            int sum  = (m^n^carry);
            carry = m + n + carry >= 2;
            ans = to_string(sum) + ans;
        }
        return ans;
    }
};
```