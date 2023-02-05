2559. Count Vowel Strings in Ranges

You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [li, ri]` asks us to find the number of strings present in the range `li` to `ri` (both inclusive) of words that start and end with a vowel.

Return an array `ans` of size `queries.length`, where `ans[i]` is the answer to the ith query.

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 

**Example 1:**
```
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
```

**Example 2:**
```
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
```

**Constraints:**

* `1 <= words.length <= 10^5`
* `1 <= words[i].length <= 40`
* `words[i]` consists only of lowercase English letters.
* `sum(words[i].length) <= 3 * 10^5`
* `1 <= queries.length <= 10^5`
* `0 <= li <= ri < words.length`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 614 ms
Memory: 54.9 MB
```
```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = "aeiou"
        pre = [0]
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                pre += [pre[-1] + 1]
            else:
                pre += [pre[-1]]
        ans = []
        for l, r in queries:
            ans += [pre[r+1]-pre[l]]
        return ans
```

**Solution 2: (Prefix Sum)**
```
Runtime: 147 ms
Memory: 64.6 MB
```
```c++
class Solution {
    bool check(char ch){
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ) return true;
        return false;
    }
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        vector<int> ans;
        vector<int> pre = {0};
        int count = 0;
        for (int i = 0; i < words.size(); i ++){
            if (check(words[i][0]) && check(words[i].back())) count++;
            pre.push_back(count);
        }
        for (int i = 0; i < queries.size(); i ++) {
            int l = queries[i][0];
            int r = queries[i][1];
            ans.push_back(pre[r+1] - pre[l]);
        }
        return ans;
    }
};
```
