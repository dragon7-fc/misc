1969. Minimum Non-Zero Product of the Array Elements

You are given a positive integer `p`. Consider an array `nums` (**1-indexed**) that consists of the integers in the **inclusive** range [1, $2^{p}$ - 1] in their binary representations. You are allowed to do the following operation any number of times:

* Choose two elements `x` and `y` from `nums`.
* Choose a bit in `x` and swap it with its corresponding bit in `y`. Corresponding bit refers to the bit that is in the **same position** in the other integer.

For example, if `x = 1101` and `y = 0011`, after swapping the $2^{nd}$ bit from the right, we have `x = 1111` and `y = 0001`.

Find the **minimum non-zero** product of `nums` after performing the above operation **any** number of times. Return this product **modulo** `10^9 + 7`.

**Note:** The answer should be the minimum product **before** the modulo operation is done.

 

**Example 1:**
```
Input: p = 1
Output: 1
Explanation: nums = [1].
There is only one element, so the product equals that element.
```

**Example 2:**
```
Input: p = 2
Output: 6
Explanation: nums = [01, 10, 11].
Any swap would either make the product 0 or stay the same.
Thus, the array product of 1 * 2 * 3 = 6 is already minimized.
```

**Example 3:**
```
Input: p = 3
Output: 1512
Explanation: nums = [001, 010, 011, 100, 101, 110, 111]
- In the first operation we can swap the leftmost bit of the second and fifth elements.
    - The resulting array is [001, 110, 011, 100, 001, 110, 111].
- In the second operation we can swap the middle bit of the third and fourth elements.
    - The resulting array is [001, 110, 001, 110, 001, 110, 111].
The array product is 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512, which is the minimum possible product.
```

**Constraints:**

* `1 <= p <= 60`

# Submissions
---
**Solution 1: (Math)**

Actually, in this problem there is HUGE hint in examples, at least I was able to get the direct formula from example 3.

Let us look at our numbers and see what happens, when we swap two bits: in fact the sum of all numbers will rest the same! So, we need to minimize product of numbers, if we have fixed sum and not allowed to have zeroes. Let us provide estimation and example:

1. **Estimation** (let p = 4 for simplicity, but logic is the same for general case) then we have numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15). Notice that if we take two numbers, say 4 and 7 and decrease smallest of them by one and increase biggest by one, sum will be the same and product become smaller - it can be proved easily for any `a <= b: (a-1)*(b+1) < a*b`. Let us continue this process until we can: we do it for pairs until one element in pair become equal to 1. Then in the end we have (1, 1, 1, 1, 1, 1, 1, 14, 14, 14, 14, 14, 14, 14, 15).
1. **Example:** in fact we can do this if we allowed to manipulate bits: we can make each pair (i, 15 - i) equal to (1, 14), because in this pair for all bits places, we have different bits, like 1001 and 0110. Number 1111 will not have pair because its pair is 0.

So, finally, we just can write direct formula.

**Complexity**

* Time complexity is `O(p)`, because python allows to do fast power, space complexity is `O(1)`.

```
Runtime: 24 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(2**p -2, 2**(p-1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)
```
