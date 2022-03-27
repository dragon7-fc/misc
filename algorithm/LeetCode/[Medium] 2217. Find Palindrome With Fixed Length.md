2217. Find Palindrome With Fixed Length

Given an integer array `queries` and a positive integer `intLength`, return an array `answer` where `answer[i]` is either the `queries[i]`th smallest **positive palindrome** of length `intLength` or `-1` if no such palindrome exists.

A **palindrome** is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

 

**Example 1:**
```
Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
The 90th palindrome of length 3 is 999.
```

**Example 2:**
```
Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.
```

**Constraints:**

* `1 <= queries.length <= 5 * 10^4`
* `1 <= queries[i] <= 10^9`
* `1 <= intLength <= 15`

# Submissions
---
**Solution 1: (Math)**

Only the first `(intLength + 1) / 2` characters matter. The remaining characters are just a reflection.

Say `intLength == 7`, so we consider only `4` characters. The minimum number is `1000` and maximum = `9999`.

Therefore, we can have `9999 - 1000 + 1 == 9000` palindromes. To find out the palindrome, we add a `q - 1` to the minimum number, reverse, and concatenate.

For example, for query `8765`, the base number is `1000 + 8765 - 1 == 9764`. Concatenating it with `679`, we get `9764679` as the result.

```
Runtime: 143 ms
Memory Usage: 54.1 MB
```
```c++
class Solution {
    int reverse(long long n, bool skip) {
        long long res = 0;
        for (n = skip ? n / 10 : n; n > 0; n /= 10)
            res = res * 10 + n % 10;
        return res;
    }
    
public:
    vector<long long> kthPalindrome(vector<int>& queries, int intLength) {
        vector<long long> res;
        long long start = pow(10, (intLength + 1) / 2 - 1), end = pow(10, (intLength + 1 ) / 2), mul = pow(10, intLength / 2);    
        for (int q : queries)
            res.push_back(start + q > end ? -1 : 
                (start + q - 1) * mul + reverse(start + q - 1, intLength % 2));
        return res;
    }
};
```
