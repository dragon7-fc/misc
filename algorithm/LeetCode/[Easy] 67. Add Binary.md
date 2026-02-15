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

**Solution 3: (Bit Manipulation)**
```
Runtime: 58 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
```

**Solution 4: (Math)**
```
Runtime: 0 ms
Memory Usage: 5.7 MB
```
```c


char * addBinary(char * a, char * b){
    int i, j, k, c = 0;
    char *res;
    
    i = strlen(a);
    j = strlen(b);
    k = i > j ? i : j;
    k += 2;

    res = malloc(k * sizeof(char));
    
    i--;
    j--;
    res[--k] = '\0';
    
    while (--k >= 0) {
        c += i >= 0 ? a[i--] - '0': 0;
        c += j >= 0 ? b[j--] - '0': 0;
        
        res[k] = c % 2 + '0';
        c /= 2;
    }
    
    if (res[0] == '0')
       memmove(res, res + 1, strlen(res) * sizeof(char));
    
    return res;
}
```

**Solution 5: (Math)**

               i
    a = "1 0 1 0",
               j
    b = "1 0 1 1"
p      1   1   
ans    1 0 1 0 1

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.75 MB, Beats 95.82%
```
```c++
class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.length(), n = b.length(), i = m - 1, j = n - 1, c, p = 0;
        string ans;
        while (i >= 0 || j >= 0 || p) {
            c = (i >= 0 ? a[i] - '0': 0) + (j >= 0 ? b[j] - '0' : 0) + p;
            ans += c % 2 + '0';
            p = c / 2;
            i -= 1;
            j -= 1;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```
