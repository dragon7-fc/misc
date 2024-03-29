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

**Solution 1: (Greedy, Two Pointers)**
```
Runtime: 7 ms
Memory Usage: 6.7 MB
```
```c++
class Solution {
public:
    unordered_map<char, int> last;
    vector<int> partitionLabels(string s) {
        for (int i = 0; i < s.size(); i ++)
            last[s[i]] = i;
        int j = 0, anchor = 0;
        vector<int>ans;
        for (int i = 0; i < s.size(); i ++) {
            j = max(j, last[s[i]]);
            if (i == j) {
                ans.push_back(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return ans;
    }
};
```
