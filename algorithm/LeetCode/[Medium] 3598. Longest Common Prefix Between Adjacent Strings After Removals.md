3598. Longest Common Prefix Between Adjacent Strings After Removals

You are given an array of strings `words`. For each index `i` in the range `[0, words.length - 1]`, perform the following steps:

* Remove the element at index `i` from the words array.
* Compute the length of the **longest common prefix** among all adjacent pairs in the modified array.

Return an array `answer`, where `answer[i]` is the length of the longest common prefix between the adjacent pairs after removing the element at index `i`. If no adjacent pairs remain or if **none** share a common prefix, then `answer[i]` should be 0.

 

**Example 1:**
```
Input: words = ["jump","run","run","jump","run"]

Output: [3,0,0,3,3]

Explanation:

Removing index 0:
words becomes ["run", "run", "jump", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 1:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 2:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 3:
words becomes ["jump", "run", "run", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 4:
words becomes ["jump", "run", "run", "jump"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
```

**Example 2:**
```
Input: words = ["dog","racer","car"]

Output: [0,0,0]

Explanation:

Removing any index results in an answer of 0.
```

Constraints:

* `1 <= words.length <= 10^5`
* `1 <= words[i].length <= 10^4`
* `words[i]` consists of lowercase English letters.
* The sum of `words[i].length` is smaller than or equal 10^5.

# Submissions
---
**Solution 1: (Prefix Sum, left and right)**

    words = ["jump","run","run","jump","run"]
                            ^
    dp          0     3     0     0     0
    right       3     3     0     0     0
    left        0     0     0     3     3
    mid         0     0     0     3     0
    ans         3     0     0     3     3

```
Runtime: 35 ms, Beats 70.11%
Memory: 206.77 MB, Beats 84.47%
```
```c++
class Solution {
    int getlcp(string &w1, string &w2) {
        int n1 = w1.length(), n2 = w2.length(), j = 0;
        while (j < n1 && j < n2 && w1[j] == w2[j]) {
            j += 1;
        }
        return j;
    }
public:
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size(), i, j;
        vector<int> dp(n), left(n), right(n), ans(n);
        for (i = n-1; i >= 0; i --) {
            j = 0;
            if (i != n-1) {
                j = getlcp(words[i], words[i+1]);
            }
            dp[i] = j;
            if (i != n-1) {
                right[i] = max(right[i+1], dp[i]);
            }
        }
        for (i = 0; i < n; i ++) {
            if (i >= 2) {
                left[i] = max(left[i-1], dp[i-2]);
            }
            j = 0;
            if (i && i != n-1) {
                j = getlcp(words[i-1], words[i+1]);
            }
            ans[i] = j;
            if (i >= 2) {
                ans[i] = max(ans[i], left[i]);
            }
            if (i != n-1) {
                ans[i] = max(ans[i], right[i+1]);
            }
        }
        return ans;
    }
};
```
