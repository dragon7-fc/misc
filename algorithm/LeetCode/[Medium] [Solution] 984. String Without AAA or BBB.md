984. String Without AAA or BBB

Given two integers `A` and `B`, return any string `S` such that:

* `S` has length `A + B` and contains exactly `A` `'a'` letters, and exactly `B` `'b'` letters;
* The substring `'aaa'` does not occur in `S`;
* The substring `'bbb'` does not occur in `S`.
 

**Example 1:**
```
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
```

**Example 2:**
```
Input: A = 4, B = 1
Output: "aabaa"
``` 

**Note:**

* `0 <= A <= 100`
* `0 <= B <= 100`
* It is guaranteed such an `S` exists for the given `A` and `B`.

# Solution
---
## Approach 1: Greedy
**Intuition**

Intuitively, we should write the most common letter first. For example, if we have `A = 6, B = 2`, we want to write `'aabaabaa'`. The only time we don't write the most common letter is if the last two letters we have written are also the most common letter

**Algorithm**

Let's maintain `A, B`: the number of `'a'` and `'b'`'s left to write.

If we have already written the most common letter twice, we'll write the other letter. Otherwise, we'll write the most common letter.

```python
class Solution(object):
    def strWithout3a3b(self, A, B):
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity: $O(A+B)$.

* Space Complexity: $O(A+B)$.

# Submissions
---
**Solution: (Greedy)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = ''

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans += 'a'
            else:
                B -= 1
                ans += 'b'

        return ans
```
