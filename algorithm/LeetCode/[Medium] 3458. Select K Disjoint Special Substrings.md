3458. Select K Disjoint Special Substrings

Given a string `s` of length `n` and an integer `k`, determine whether it is possible to select `k` disjoint special substrings.

A **special** substring is a **substring** where:

* Any character present inside the substring should not appear outside it in the string.
* The substring is not the entire string `s`.

**Note** that all `k` substrings must be disjoint, meaning they cannot overlap.

Return `true` if it is possible to select `k` such disjoint special substrings; otherwise, return `false`.

 

**Example 1:**
```
Input: s = "abcdbaefab", k = 2

Output: true

Explanation:

We can select two disjoint special substrings: "cd" and "ef".
"cd" contains the characters 'c' and 'd', which do not appear elsewhere in s.
"ef" contains the characters 'e' and 'f', which do not appear elsewhere in s.
```

**Example 2:**
```
Input: s = "cdefdc", k = 3

Output: false

Explanation:

There can be at most 2 disjoint special substrings: "e" and "f". Since k = 3, the output is false.
```

**Example 3:**
```
Input: s = "abeabe", k = 0

Output: true
```
 

**Constraints:**

* `2 <= n == s.length <= 5 * 10^4`
* `0 <= k <= 26`
* `s` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (String, Sort)**

__Intuition__
Iterate string s and
record first[c] and last[c] occurrence indice for each char c,
as well as its frequency count[c]

**Problem 1: find out all special substring**
Enumerate the start i and end j of special substring,
then check other characters c if all occurrences are in this range
by i <= first[c] <= last[c] <= j.
If the substring length j - i + 1 is same as the total count,
then we have a special substring.

**Problem 2: find out non ovelapping intervals**
Find out non ovelapping intervals, as many as possible.
You can reuse 435. Non-overlapping Intervals

Here I sort the interval by length
and greedily take the interval with samller length.

__Complexity__
Time O(n + c ^ 3)
Space O(c)
where c is the number of different chars and c <= 26

I noticed many solutions didn't give a right complexity,
or it's O(nc) instead of O(n)

```
Runtime: 332 ms, Beats 100.00%
Memory: 18.15 MB, Beats 100.00%
```
```python
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        first = {}
        last = {}
        count = Counter()
        for i,c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
            count[c] += 1

        ## find out all special substring
        intervals = []
        for c1,i in first.items():
            for c2,j in last.items():
                if i <= j:
                    cnt = 0
                    for c in count:
                        if i <= first[c] <= last[c] <= j:
                            cnt += count[c]
                    if cnt == j - i + 1 and cnt < len(s):
                        intervals.append([i, j])

        ## find out non ovelapping intervals
        intervals.sort(key = lambda s: s[1] - s[0])
        res = []
        for i,j in intervals:
            if all(y < i or j < x for x,y in res):
                res.append([i, j])
        return len(res) >= k
```
