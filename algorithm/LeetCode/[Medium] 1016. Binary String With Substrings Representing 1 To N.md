1016. Binary String With Substrings Representing 1 To N

Given a binary string `S` (a string consisting only of '0' and '1's) and a positive integer `N`, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of `S`.

 

**Example 1:**
```
Input: S = "0110", N = 3
Output: true
```

**Example 2:**
```
Input: S = "0110", N = 4
Output: false
```

**Note:**

* `1 <= S.length <= 1000`
* `1 <= N <= 10^9`

# Submissions
---
**Solution 1: (Brute Force)**
```
Runtime: 24 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(bin(i)[2:] in S for i in range(1, N+1))
```

**Solution 2: (Brute Force)**
```
Runtime: 0 ms
Memory: 6.8 MB
```
```c++
class Solution {
public:
    bool queryString(string s, int n) {
        for (int i = 1; i <= n; ++i) {
            vector<int> binary;
            int temp = i;
            while (temp != 0) {
                int digit = temp % 2;
                binary.push_back(digit);
                temp /= 2;
            }
            reverse(binary.begin(), binary.end());

            string result;
            for (int num : binary) {
                result += to_string(num);
            }

            if (s.find(result) == string::npos) {
                return false;
            }
        }
        return true;
    }
};
```
