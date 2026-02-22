696. Count Binary Substrings

Give a string `s`, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

**Example 1:**
```
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
```

**Example 2:**
```
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
```

**Note:**

* `s.length` will be between `1` and `50,000`.
* `s` will only consist of `"0"` or `"1"` characters.

# Solution
---
## Approach #1: Group By Character [Accepted]
**Intuition**

We can convert the string `s` into an array groups that represents the length of same-character contiguous blocks within the string. For example, if `s = "110001111000000"`, then `groups = [2, 3, 4, 6]`.

For every binary string of the form `'0' * k + '1' * k` or `'1' * k + '0' * k`, the middle of this string must occur between two groups.

Let's try to count the number of valid binary strings between `groups[i]` and `groups[i+1]`. If we have `groups[i] = 2, groups[i+1] = 3`, then it represents either `"00111"` or `"11000"`. We clearly can make `min(groups[i], groups[i+1])` valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.

**Algorithm**

Let's create groups as defined above. The first element of `s` belongs in it's own group. From then on, each element either doesn't match the previous element, so that it starts a new group of size `1`; or it does match, so that the size of the most recent group increases by `1`.

Afterwards, we will take the sum of `min(groups[i-1], groups[i])`.

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
```

Alternate Implentation
```python
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `s`. Every loop is through $O(N)$ items with $O(1)$ work inside the for-block.

* Space Complexity: $O(N)$, the space used by groups.

## Approach #2: Linear Scan [Accepted]
**Intuition and Algorithm**

We can amend our Approach #1 to calculate the answer on the fly. Instead of storing groups, we will remember only `prev = groups[-2]` and `cur = groups[-1]`. Then, the answer is the sum of `min(prev, cur)` over each different final `(prev, cur)` we see.

```python
class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `s`. Every loop is through $O(N)$ items with $O(1)$ work inside the for-block.

* Space Complexity: $O(1)$, the space used by `prev`, `cur`, and `ans`.

# Submissions
---
**Solution: (Linear Scan)**
```
Runtime: 168 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
```

**Solution 2: (Greedy)**
```
Runtime: 3 ms, Beats 67.83%
Memory: 13.08 MB, Beats 61.91%
```
```c++
class Solution {
public:
    int countBinarySubstrings(string s) {
        int n = s.length(), i, pre = 0, cur = 1, ans = 0;
        for (i = 1; i < n; i ++) {
            if (s[i] == s[i - 1]) {
                cur += 1;
            } else {
                ans += min(pre, cur);
                pre = cur;
                cur = 1;
            }
        }
        ans += min(pre, cur);
        return ans;
    }
};
```
