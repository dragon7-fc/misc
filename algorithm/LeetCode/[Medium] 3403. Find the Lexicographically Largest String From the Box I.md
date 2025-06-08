3403. Find the Lexicographically Largest String From the Box I

You are given a string `word`, and an integer `numFriends`.

Alice is organizing a game for her `numFriends` friends. There are multiple rounds in the game, where in each round:

* `word` is split into numFriends **non-empty** strings, such that no previous round has had the **exact** same split.
* All the split words are put into a box.

Find the **lexicographically largest** string from the box after all the rounds are finished.

A string `a` is **lexicographically smaller** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`.
If the first `min(a.length, b.length)` characters do not differ, then the shorter string is the lexicographically smaller one.

 

**Example 1:**
```
Input: word = "dbca", numFriends = 2

Output: "dbc"

Explanation: 

All possible splits are:

"d" and "bca".
"db" and "ca".
"dbc" and "a".
```

**Example 2:**
```
Input: word = "gggg", numFriends = 4

Output: "g"

Explanation: 

The only possible split is: "g", "g", "g", and "g".
```
 

**Constraints:**

* `1 <= word.length <= 5 * 10^3`
* `word` consists only of lowercase English letters.
* `1 <= numFriends <= word.length`

# Submissions
---
**Solution 1: (Brute Force)**

n = 7
numFriends = 5

    0 1 2 3 4 5 6
    x x x x x x x
    x x x
      x x x
        x x x
          x x x
            x x x
              x x
                x
    -----
    n-numFriens+1

```
Runtime: 72 ms
Memory: 169.24 MB
```
```c++
class Solution {
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) {
            return word;
        }
        int n = word.size(), m = n - numFriends + 1;
        string res = "";
        for (int i = 0; i < n; ++i) {
            res = max(res, word.substr(i, m));
        }
        return res;
    }
};
```

**Solution 2: (Two Pointers)**
```
Runtime: 4 ms, Beats 95.52%
Memory: 11.03 MB, Beats 86.57%
```
```c++
class Solution {
    string lastSubstring(string s) {
        int i = 0, j = 1, n = s.size();
        while (j < n) {
            int k = 0;
            while (j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            if (j + k < n && s[i + k] < s[j + k]) {
                int t = i;
                i = j;
                j = max(j + 1, t + k + 1);
            } else {
                j = j + k + 1;
            }
        }
        return s.substr(i, n - i);
    }
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) {
            return word;
        }
        string last = lastSubstring(word);
        int n = word.size(), m = last.size();
        return last.substr(0, min(m, n - numFriends + 1));
    }
};
```
