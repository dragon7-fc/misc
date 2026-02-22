3848. Check Digitorial Permutation

You are given an integer `n`.

A number is called **digitorial** if the sum of the **factorials** of its digits is equal to the number itself.

Determine whether **any permutation** of `n` (including the original order) forms a **digitorial** number.

Return `true` if such a permutation exists, otherwise return `false`.

**Note:**

* The **factorial** of a non-negative integer `x`, denoted as `x!`, is the product of all positive integers less than or equal to `x`, and `0! = 1`.
* A **permutation** is a rearrangement of all the digits of a number that does **not** start with zero. Any arrangement starting with zero is invalid.
 

**Example 1:**
```
Input: n = 145

Output: true

Explanation:

The number 145 itself is digitorial since 1! + 4! + 5! = 1 + 24 + 120 = 145. Thus, the answer is true.
```

**Example 2:**
```
Input: n = 10

Output: false

Explanation:

10 is not digitorial since 1! + 0! = 2 is not equal to 10, and the permutation "01" is invalid because it starts with zero.
```
 

**Constraints:**

`1 <= n <= 10^9`

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.95 MB, Beats 70.23%
```
```c++
class Solution {
    static std::array<int, 10> digit_frequencies(int x) {
        std::array<int, 10> c{}; 
        do { 
            c[x % 10]++; 
            x /= 10; 
        } while (x);
        return c;
    }
public:
    bool isDigitorialPermutation(int n) {
        int factorials[10]; 
        factorials[0] = 1;
        for (int d = 1; d < 10; ++d) 
            factorials[d] = factorials[d - 1] * d;

        int digits_sum = 0, x = n;
        do { 
            digits_sum += factorials[x % 10]; 
            x /= 10; 
        } while (x);

        return digit_frequencies(digits_sum) == digit_frequencies(n);
    }
};
```
