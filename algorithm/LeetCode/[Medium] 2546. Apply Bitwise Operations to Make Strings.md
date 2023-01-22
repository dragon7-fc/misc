2546. Apply Bitwise Operations to Make Strings

You are given two **0-indexed** binary strings `s` and `target` of the same length `n`. You can do the following operation on `s` any number of times:

* Choose two different indices `i` and `j` where `0 <= i, j < n`.
* Simultaneously, replace `s[i]` with (`s[i]` **OR** `s[j]`) and `s[j]` with (`s[i]` **XOR** `s[j]`).

For example, if `s = "0110"`, you can choose `i = 0` and `j = 2`, then simultaneously replace `s[0]` with (`s[0] OR s[2] = 0 OR 1 = 1`), and `s[2]` with (`s[0] XOR s[2] = 0 XOR 1 = 1`), so we will have `s = "1110"`.

Return `true` if you can make the string `s` equal to `target`, or `false` otherwise.

 

**Example 1:**
```
Input: s = "1010", target = "0110"
Output: true
Explanation: We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "0010".
- Choose i = 2 and j = 1. We have now s = "0110".
Since we can make s equal to target, we return true.
```

**Example 2:**
```
Input: s = "11", target = "00"
Output: false
Explanation: It is not possible to make s equal to target with any number of operations.
```

**Constraints:**

* `n == s.length == target.length`
* `2 <= n <= 10^5`
* `s` and `target` consist of only the digits `0` and `1`.

# Submissions
---
**Solution 1: (Math)**

__Intuition__

Enumerate the values for s[i] and s[j]
(0, 0) -> (0, 0)
(1, 0) -> (1, 1)
(0, 1) -> (1, 1)
(1, 1) -> (1, 0)


__Explanation__

__To summrize the rule__

Two 0s stay 0s.
If we have 1, we can make any 0 to 1.
If we have at least two 1s, we can make any 1 to 0.

__Continue to sunmmrize__

All 0 string can not change.
Any other strings can transform from each other.

__So we only need to check__

if s has 1.
if target has 1.


__Complexity__

Time O(n)
Space O(1)

```
Runtime: 41 ms
Memory: 15.1 MB
```
```python
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)
```
