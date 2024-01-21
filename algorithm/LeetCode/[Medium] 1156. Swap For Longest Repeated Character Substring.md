1156. Swap For Longest Repeated Character Substring

Given a string `text`, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 

**Example 1:**
```
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
```

**Example 2:**
```
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
```

**Example 3:**
```
Input: text = "aaabbaaa"
Output: 4
```

**Example 4:**
```
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
```

**Example 5:**
```
Input: text = "abcdef"
Output: 1
```

**Constraints:**

* `1 <= text.length <= 20000`
* text consist of lowercase English characters only.

# Submissions
---
**Solution 1:**

**Intuition**
There are only 2 cases that we need to take care of:

* extend the group by 1
* merge 2 adjacent groups together, which are separated by only 1 character

**Explanation**
For `S = "AAABBCB"`
`[[c, len(list(g))] for c, g in groupby(S)] --> [[A,3],[B,2],[C,1],[B,1]]`
collections.Counter(S) --> {A:3, B:3, C:1}
With these two data, calculate the best solution for the two cases above.


**Complexity**
* Time $O(N)$
* Space $O(N)$

```
Runtime: 68 ms
Memory Usage: 14.3 MB
```
```python
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res
            
```

**Solution 2: (Sliding Window)**
```
Runtime: 9 ms
Memory: 7.04 MB
```
```c++

class Solution {
public:
    int maxRepOpt1(string text) {
        int res = 0;
        for (auto ch = 'a'; ch <= 'z'; ++ch) {
            int i = 0, j = 0, gap = 0;
            while (i < text.size()) {
                gap += text[i++] != ch;
                if (gap > 1)
                    gap -= text[j++] != ch;
            }
            res = max(res, min(i - j, (int)count_if(begin(text), end(text), [&](char ch1) { return ch1 == ch; })));
        }
        return res;
    }
};
```

**Solution 3: (Group and Count)**
```
Runtime: 0 ms
Memory: 7.96 MB
```
```c++
class Solution {
public:
    int maxRepOpt1(string text) {
        vector<vector<int>> idx(26);
        int res = 0;
        for (auto i = 0; i < text.size(); ++i) 
            idx[text[i] - 'a'].push_back(i);
        for (auto n = 0; n < 26; ++n) {
            auto cnt = 1, cnt1 = 0, mx = 0;
            for (auto i = 1; i < idx[n].size(); ++i) {
                if (idx[n][i] == idx[n][i - 1] + 1) ++cnt;
                else {
                    cnt1 = idx[n][i] == idx[n][i - 1] + 2 ? cnt : 0;
                    cnt = 1;
                }
                mx = max(mx, cnt1 + cnt);        
            }
            res = max(res, mx + (idx[n].size() > mx ? 1 : 0));
        }
        return res;
    }
};
```
