1234. Replace the Substring for Balanced String

You are given a string containing only 4 kinds of characters `'Q', 'W', 'E' and 'R'`.

A string is said to be **balanced** if each of its characters appears `n/4` times where `n` is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string `s` **balanced**.

Return `0` if the string is already **balanced**.

 

**Example 1:**
```
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
```

**Example 2:**
```
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
```

**Example 3:**
```
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
```

**Example 4:**
```
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
```

**Constraints:**

* `1 <= s.length <= 10^5`
* `s.length is a multiple of 4`
* `s contains only 'Q', 'W', 'E' and 'R'`.

# Submissions
---
**Solution 1:**

**Intuition**
We want a minimum length of substring,
which leads us to the solution of sliding window.
Specilly this time we don't care the count of elements inside the window,
we want to know the count outside the window.


**Explanation**
One pass the all frequency of "QWER".
Then slide the windon in the string `s`.

Imagine that we erase all character inside the window,
as we can modify it whatever we want,
and it will always increase the count outside the window.

So we can make the whole string balanced,
as long as `max(count[Q],count[W],count[E],count[R]) <= n / 4`.


**Complexity:**
* Time $O(N)$, one pass for counting, one pass for sliding window
* Space $O(1)$

**More Similar Sliding Window Problems**
Here are some similar sliding window problems.
Also find more explanations.
Good luck and have fun.

* 1234. Replace the Substring for Balanced String
* 992. Subarrays with K Different Integers
* 904. Fruit Into Baskets

```
Runtime: 540 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res = n = len(s)
        i = 0  ## sliding window start
        for j, c in enumerate(s):  ## sliding window end
            count[c] -= 1  ## try to clear character and enter sliding window
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):  ## balanced string
                res = min(res, j - i + 1)
                count[s[i]] += 1  ## restore character and leave sliding window
                i += 1 ## try to increase start
        return res
```