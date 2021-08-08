1963. Minimum Number of Swaps to Make the String Balanced

You are given a **0-indexed** string `s` of even length `n`. The string consists of **exactly** `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.

A string is called balanced if and only if:

* It is the empty string, or
* It can be written as `AB`, where both `A` and `B` are **balanced** strings, or
* It can be written as `[C]`, where `C` is a **balanced** string.

You may swap the brackets at **any** two indices **any** number of times.

Return the **minimum** number of swaps to make `s` **balanced**.

 

**Example 1:**
```
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
```

**Example 2:**
```
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][[]".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
```

**Example 3:**
```
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
```

**Constraints:**

* `n == s.length`
* `2 <= n <= 10^6`
* `n` is even.
* `s[i]` is either `'['` or `']'`.
* The number of opening brackets `'['` equals `n / 2`, and the number of closing brackets `']'` equals `n / 2`.

# Submissions
---
**Solution 1: (Stack)**

Traverse the input `s`, remove all `[]`. Since the number of `['`s and `]'`s are same, the remaining must be `]]]...[[[`. Otherwise, if left half had any `[`, there would be at least a `[]` among them.

1. For every `2` pairs of square brackets, a swap will make them balanced;
1. If only `1` pair not in balance, we need a swap.

Therefore, we need at least `(pairs + 1) / 2` swaps.

```
Runtime: 552 ms
Memory Usage: 31.6 MB
```
```python
class Solution:
    def minSwaps(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and stk[-1] == '[' and c == ']':
                stk.pop()
            else:
                stk.append(c)
        return (len(stk) // 2 + 1) // 2
```
