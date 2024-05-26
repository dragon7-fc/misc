2847. Smallest Number With Given Digit Product

Given a positive integer `n`, return a string representing the **smallest positive** integer such that the product of its digits is equal to `n`, or `"-1"` if no such number exists.

 

**Example 1:**
```
Input: n = 105
Output: "357"
Explanation: 3 * 5 * 7 = 105. It can be shown that 357 is the smallest number with a product of digits equal to 105. So the answer would be "105".
```

**Example 2:**
```
Input: n = 7
Output: "7"
Explanation: Since 7 has only one digit, its product of digits would be 7. We will show that 7 is the smallest number with a product of digits equal to 7. Since the product of numbers 1 to 6 is 1 to 6 respectively, so "7" would be the answer.
```

**Example 3:**
```
Input: n = 44
Output: "-1"
Explanation: It can be shown that there is no number such that its product of digits is equal to 44. So the answer would be "-1".
```

**Constraints:**

* `1 <= n <= 10^18`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 2 ms
Memory: 7.92 MB
```
```c++
class Solution {
public:
    string smallestNumber(long long n) {
        if (n == 1) return "1";
        string ans = "";
        for (int d = 9; d > 1; d--) {
            while (n % d == 0) {
                ans += to_string(d);
                n /= d;
            }
        }
        if (n > 1) return "-1";
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```
