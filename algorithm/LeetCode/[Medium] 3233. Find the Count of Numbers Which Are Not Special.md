3233. Find the Count of Numbers Which Are Not Special

You are given 2 positive integers `l` and `r`. For any number `x`, all positive divisors of `x` except `x` are called the **proper divisors** of `x`.

A number is called **special** if it has exactly 2 **proper divisors**. For example:

* The number 4 is special because it has proper divisors 1 and 2.
* The number 6 is not special because it has proper divisors 1, 2, and 3.

Return the count of numbers in the range `[l, r]` that are **not special**.

 

**Example 1:**
```
Input: l = 5, r = 7

Output: 3

Explanation:

There are no special numbers in the range [5, 7].
```

**Example 2:**
```
Input: l = 4, r = 16

Output: 11

Explanation:

The special numbers in the range [4, 16] are 4 and 9.
```
 

**Constraints:**

`* 1 <= l <= r <= 109`

# Submissions
---
**Solution 1: (Math, Sieve of Eratosthenes)**
```
Runtime: 66 ms
Memory: 17.98 MB
```
```c++
class Solution {
public:
    int nonSpecialCount(int l, int r) {
        int n = sqrt(r);
        vector<bool> v(n+1,1);
        vector<int> prime;
        v[0] = v[1] = 0;
        for (int i = 2; i <= n; i++) {
            if (v[i] == 1){
                prime.push_back(i);
                for (int j = i*i; j <= n; j+=i) {
                    v[j] = 0;
                }
            }
        }
        vector<int> ans;
        for (int i : prime){
            int special = i*i;
            if (special >= l && special <= r) {
                ans.push_back(special);
            }
        }
        int c = r-l;
        return c - ans.size() + 1; 
    }
};
```
