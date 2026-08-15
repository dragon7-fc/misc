4022. K-th Digit in Infinite String

You are given an integer `k`.

An **infinite** string is formed by **concatenating** the **decimal** representations of the **positive** integers, without separators.

For every nonnegative integer `b`, block `b` contains the positive integers from `10 * b` through `10 * b + 9`. The integers in each block are appended as follows:

* If `b` is even, append the integers in **increasing** order.
* If `b` is odd, append the integers in **decreasing** order.

Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.

Return the `k`^th digit (1-indexed) of this string.

 

**Example 1:**
```
Input: k = 4

Output: 4

Explanation:

The string begins as "123456789..". The 4th digit is '4'.
```

**Example 2:**
```
Input: k = 15

Output: 7

Explanation:

The string begins as "123456789191817..". The 15th digit is '7'.
```

**Example 3:**
```
Input: k = 11

Output: 9

Explanation:

The string begins as "12345678919..". The 11th digit is '9'.
```
 

**Constraints:**

* `1 <= k <= 10^15`

# Submissions
---
**Solution 1: (Math, Calculate the length)**

__Intuition__
k is very big,
we need to find the kth digit in the infinite string
by first determining the length of the numbers
in the current block.

__Explanation__
It loops through blocks of numbers grouped by their length,
subtracting the total digits in each block from k.

Once the target length is found,
it calculates the exact number,
represented by the variable d,
where the target digit resides.
Then finds the exact digit index within this specific number.

Finally,
based on the problem's parity rules
for odd and even blocks,
it returns either the original digit
or its 9's complement.

__Complexity__
Time O(logk)
Space O(1)

                                                       len
      1                2           9                   1 * 9 * 10^0
   19     18  17    20 21 22                           2 * 9 * 10^1
199  190  180                                          3 * 9 * 10^2
  ^    ^
  b is even/odd only affect last digit

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.42 MB, Beats 20.00%
```
```c++
class Solution {
public:
    int kthDigit(long long k) {
        int len = 1;
        while (len * 9LL * pow(10, len - 1) < k) {
            k -= len * 9LL * pow(10, len - 1);
            len += 1;
        }
        k -= 1;
        long long num = pow(10, len - 1) + k / len;
        k = k % len;
        int res = to_string(num)[k] - '0';
        return k < len - 1 || num / 10 % 2 == 0 ? res : 9 - res;
               // b is even/odd only affect last digit
    }
};
```
