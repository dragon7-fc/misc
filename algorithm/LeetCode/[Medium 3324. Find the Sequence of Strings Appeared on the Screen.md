3324. Find the Sequence of Strings Appeared on the Screen

You are given a string `target`.

Alice is going to type `target` on her computer using a special keyboard that has only two keys:

* Key 1 appends the character `"a"` to the string on the screen.
* Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For example, `"c"` changes to `"d"` and `"z"` changes to `"a"`.

**Note** that initially there is an empty string `""` on the screen, so she can **only** press key 1.

Return a list of all strings that appear on the screen as Alice types `target`, in the order they appear, using the **minimum** key presses.

 

**Example 1:**
```
Input: target = "abc"

Output: ["a","aa","ab","aba","abb","abc"]

Explanation:

The sequence of key presses done by Alice are:

Press key 1, and the string on the screen becomes "a".
Press key 1, and the string on the screen becomes "aa".
Press key 2, and the string on the screen becomes "ab".
Press key 1, and the string on the screen becomes "aba".
Press key 2, and the string on the screen becomes "abb".
Press key 2, and the string on the screen becomes "abc".
```

**Example 2:**
```
Input: target = "he"

Output: ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]
```
 

**Constraints:**

* `1 <= target.length <= 400`
* `target` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 43 ms
Memory: 113.52 MB
```
```c++
class Solution {
public:
    vector<string> stringSequence(string target) {
        vector<string> ans;
        for (int i = 0; i < target.size(); i ++) {
            if (!ans.size()) {
                ans.push_back("a");
            }
            if (ans.back().size() < i+1) {
                ans.push_back(ans.back()+"a");
            }
            string cur = ans.back();
            while (cur != target.substr(0, i+1)) {
                cur.back() += 1;
                ans.push_back(cur);
            }
        }
        return ans;
    }
};
```
