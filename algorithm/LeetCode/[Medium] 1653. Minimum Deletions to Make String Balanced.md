1653. Minimum Deletions to Make String Balanced

You are given a string `s` consisting only of characters `'a'` and `'b'`.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return the **minimum** number of deletions needed to make `s` **balanced**.

**Example 1:**
```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
```

**Example 2:**
```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

**Constraints:**

* `1 <= s.length <= 105`
* `s[i] is 'a' or 'b'`.

# Submissions
---
**Solution 1: (Count from left and right side for each element)**

* `a_right_count[i]`: the number of a at the right of index i
* `b_left_count[i]`: the number of b at the left of index i
* `a_right_count[i] + b_left_count[i]`: the number of deleted characters at index i

```
Runtime: 1132 ms
Memory Usage: 19.6 MB
```
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right_count = [0] * len(s)
        b_left_count = [0] * len(s)
        
        count = 0
        for i in range(len(s)):
            b_left_count[i] = count
            if s[i] == 'b':
                count += 1
        
        count = 0
        for i in range(len(s) - 1 ,-1, -1):
            a_right_count[i] = count
            if s[i] == 'a':
                count += 1
        
        min_delete = len(s)
        for i in range(len(s)):
            min_delete = min(min_delete, a_right_count[i] + b_left_count[i])
        return min_delete
```

**Solution 1: (DP Bottom-Up)**

The problem can be formulated as DP.

At every point when you see 'a' , you have 2 options,

1. remove all the b's you found earlier. --> total cost = count_of_b
OR
1. delete the current 'a'. --> total cost = cur_total_cost + 1

If u see a 'b' , then no more cost.

Thus maintain the count of 'b's you found.

```
Runtime: 540 ms
Memory Usage: 17.5 MB
```
```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        for c in s:
            if c == 'b':
                cnt_b+=1
                dp.append( dp[-1] )
            else:
                dp.append( min(cnt_b,dp[-1]+1) )
        return dp[-1]
```