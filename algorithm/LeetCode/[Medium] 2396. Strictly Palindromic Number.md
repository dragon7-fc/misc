2396. Strictly Palindromic Number

An integer `n` is **strictly palindromic** if, for every base `b` between `2` and `n - 2` (**inclusive**), the string representation of the integer `n` in base `b` is **palindromic**.

Given an integer `n`, return `true` if `n` is **strictly palindromic** and `false` otherwise.

A string is **palindromic** if it reads the same forward and backward.

 

**Example 1:**
```
Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
```

**Example 2:**
```
Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.
```
 

**Constraints:**

* `4 <= n <= 10^5`

# Submissions
---
**Solution 1: (return false)**

**Intuition**

The condition is extreme hard to satisfy, think about it...
for every base b between 2 and n - 2...
4 is not strictly palindromic number
5 is not strictly palindromic number
..
then the bigger, the more impossible.
Just return false


**Prove**

4 = 100 (base 2), so 4 is not strictly palindromic number
for n > 4, consider the base n - 2.
In base n - 1, n = 11.
In base n - 2, n = 12, so n is not strictly palindromic number.

There is no strictly palindromic number n where n >= 4


**More**

I think it may make some sense to ask if there a base b
between 2 and n - 2 that n is palindromic,
otherwise why it bothers to mention n - 2?

It's n - 2, not n - 1,
since for all n > 1,
n is 11 in base n - 2.
(Because n = (n - 1) + (1))

Then it's at least a algorithme problem to solve,
instead of a brain-teaser.

Maybe Leetcode just gave a wrong description.


**Complexity**

* Time O(1)
* Space O(1)

```
Runtime: 51 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
```

**Solution 2: (return false)**
```
Runtime: 3 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        return false;
    }
};
```
