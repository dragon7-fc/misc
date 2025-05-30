763. Partition Labels

A string `S` of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

**Example 1:**
```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

**Note:**

* `S` will have length in range `[1, 500]`.
* `S` will consist of lowercase letters (`'a'` to `'z'`) only.

# Solution
---
## Approach #1: Greedy [Accepted]
**Intuition**

Let's try to repeatedly choose the smallest left-justified partition. Consider the first label, say it's `'a'`. The first partition must include it, and also the last occurrence of `'a'`. However, between those two occurrences of `'a'`, there could be other labels that make the minimum size of this partition bigger. For example, in `"abccaddbeffe"`, the minimum first partition is `"abccaddb"`. This gives us the idea for the algorithm: For each letter encountered, process the last occurrence of that letter, extending the current partition `[anchor, j]` appropriately.

**Algorithm**

We need an array `last[char] -> index` of `S` where char occurs last. Then, let `anchor` and `j` be the start and end of the current partition. If we are at a label that occurs last at some index after `j`, we'll extend the partition `j = last[c]`. If we are at the end of the partition (`i == j`) then we'll append a partition size to our answer, and set the start of our new partition to `i+1`.

```python
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of $S$.

* Space Complexity: $O(N)$.

# Submissions
---
**Solution: (Greedy, Two Pointers)**
```
Runtime: 32 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

**Solution 1: (Prefix Sum)**

     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
     a  b  a  b  c  b  a  c  a  d  e  f  e  g  d  e  h  i  j  h  k  l  i  j
                                                                          ^  
last 8  8  8  8  8  8  8  8  8 14 15 15 15 15 15 15 19 22 23 22 23 23 23 23
                             ^                    ^                       ^
pre
    a 8
    b 5
    c 7
    d 14
    e 15
    f 11
    g 13
    h 19
    i 22
    j 23
    k 20
    l 21

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.65 MB, Beats 97.09%
```
```c++
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size(), i, pre[26], last = -1, k = 0;
        vector<int> ans;
        memset(pre, 0xff, sizeof(pre));
        for (i = 0; i < n; i ++) {
            pre[s[i] - 'a'] = i; 
        }
        for (i = 0; i < n; i ++) {
            last = max(last, pre[s[i] - 'a']);
            k += 1;
            if (last == i) {
                ans.push_back(k);
                k = 0;
            }
        }
        return ans;
    }
};
```
