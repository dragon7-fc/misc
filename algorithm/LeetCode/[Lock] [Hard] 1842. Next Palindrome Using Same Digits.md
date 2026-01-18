1842. Next Palindrome Using Same Digits

You are given a numeric string `num`, representing a very large **palindrome**.

Return the **smallest palindrome larger than** `num` that can be created by rearranging its digits. If no such palindrome exists, return an empty string `""`.

A **palindrome** is a number that reads the same backward as forward.

 

**Example 1:**
```
Input: num = "1221"
Output: "2112"
Explanation: The next palindrome larger than "1221" is "2112".
```

**Example 2:**
```
Input: num = "32123"
Output: ""
Explanation: No palindromes larger than "32123" can be made by rearranging the digits.
```

**Example 3:**
```
Input: num = "45544554"
Output: "54455445"
Explanation: The next palindrome larger than "45544554" is "54455445".
```

**Constraints:**

* `1 <= num.length <= 105`
* `num` is a palindrome.

# Submissions
---
**Solution 1: (Next Permutation over first half)**

    num = "4 5 5 4 4 5 5 4"
           ^^^^^^^
           5 4 4 5

```
Runtime: 0 ms, Beats 100.00%
Memory: 13.38 MB, Beats 100.00%
````
```c++
class Solution {
public:
    string nextPalindrome(string num) {
        int n = num.size(), i = n / 2 - 2, j;
        while (i >= 0 && num[i + 1] <= num[i]) {
            i -= 1;
        }
        if (i < 0)  {
            return "";
        }
        j = n / 2 - 1;
        while (num[j] <= num[i]) {
            j -= 1;
        }
        swap(num[i], num[j]);
        reverse(num.begin() + i + 1, num.begin() + n/2);
        for (i = 0; i < n / 2; ++i) {
            num[n - 1 - i] = num[i];
        }
        return num;
    }
};
```
