1088. Confusing Number II

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer `N`, return the number of confusing numbers between `1` and `N` inclusive.

 

**Example 1:**
```
Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
```

**Example 2:**
```
Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
```

**Note:**

* `1 <= N <= 10^9`

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 3504 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

        self.res = 0
        def dfs(forward, backward):
            if forward != backward:
                self.res += 1
            for digit in valid:
                if int(forward + digit) > N:
                    continue
                dfs(forward + digit, valid[digit] + backward)

        dfs('1', '1')
        dfs('6', '9')
        dfs('8', '8')
        dfs('9', '6')

        return self.res       
```

**Solution 2: (DFS)**
```
Runtime: 2338 ms
Memory Usage: 10.8 MB
```
```c++
class Solution {
    void bt(string f, string b, int &ans, unordered_map<string, string> &g, int n) {
        if (stol(f) > n) {
            return;
        }
        if (stoi(f) != stoi(b)) {
            ans += 1;
        }
        for (auto [k, v]: g) {
            bt(f+k, v+b, ans, g, n);
        }
    }
public:
    int confusingNumberII(int n) {
        unordered_map<string, string> g;
        g["0"] = "0";
        g["1"] = "1";
        g["6"] = "9";
        g["8"] = "8";
        g["9"] = "6";
        int ans = 0;
        bt("1", "1", ans, g, n);
        bt("6","9", ans, g, n);
        bt("8", "8", ans, g, n);
        bt("9", "6", ans, g, n);
        return ans;
    }
};
```
