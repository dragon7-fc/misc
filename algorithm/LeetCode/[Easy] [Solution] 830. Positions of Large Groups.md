830. Positions of Large Groups

In a string `S` of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like `S` = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

**Example 1:**
```
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
```
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

**Note**:  `1 <= S.length <= 1000`

# Solution
---
## Approach #1: Two Pointer [Accepted]
**Intuition**

We scan through the string to identify the start and end of each group. If the size of the group is at least 3, we add it to the answer.

**Algorithm**

Maintain pointers `i`, `j` with `i <= j`. The `i` pointer will represent the start of the current group, and we will increment `j` forward until it reaches the end of the group.

We know that we have reached the end of the group when `j` is at the end of the string, or `S[j] != S[j+1]`. At this point, we have some group `[i, j]`; and after, we will update `i = j+1`, the start of the next group.

```python
class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `S`.

* Space Complexity: $O(N)$, the space used by the answer.


# Submissions
---
**Solution: (Two Pointer)**
```
Runtime: 48 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0 # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
```

**Solution 2: (itertools)**
```
Runtime: 36 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        for k, grp in itertools.groupby(S):
            j = i + len(list(grp)) - 1
            if j - i + 1 >= 3:
                ans.append([i, j])
            i = j+1
        
        return ans
```

**Solution 3: (Two Pointers)**
```
Runtime: 0 ms
Memory: 7.7 MB
```
```c++
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int n = s.size(), i = 0, j = 0;
        vector<vector<int>> ans;
        while (j < n) {
            while (j < n && s[i] == s[j]) {
                j += 1;
            }
            if (j -i >= 3) {
                ans.push_back({i, j-1});
            }
            i = j;
        }
        return ans;
    }
};
```
