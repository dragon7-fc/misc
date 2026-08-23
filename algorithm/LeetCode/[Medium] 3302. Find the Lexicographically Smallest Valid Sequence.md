3302. Find the Lexicographically Smallest Valid Sequence

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it identical to `y`.

A sequence of indices seq is called **valid** if:

* The indices are sorted in **ascending** order.
* Concatenating the characters at these indices in `word1` in **the same** order results in a string that is almost equal to word2.

Return an array of size `word2.length` representing the **lexicographically smallest valid** sequence of indices. If no such sequence of indices exists, return an empty array.

**Note** that the answer must represent the lexicographically smallest array, **not** the corresponding string formed by those indices.

 

**Example 1:**
```
Input: word1 = "vbcca", word2 = "abc"

Output: [0,1,2]

Explanation:

The lexicographically smallest valid sequence of indices is [0, 1, 2]:

Change word1[0] to 'a'.
word1[1] is already 'b'.
word1[2] is already 'c'.
```

**Example 2:**
```
Input: word1 = "bacdc", word2 = "abc"

Output: [1,2,4]

Explanation:

The lexicographically smallest valid sequence of indices is [1, 2, 4]:

word1[1] is already 'a'.
Change word1[2] to 'b'.
word1[4] is already 'c'.
```

**Example 3:**
```
Input: word1 = "aaaaaa", word2 = "aaabc"

Output: []

Explanation:

There is no valid sequence of indices.
```

**Example 4:**
```
Input: word1 = "abc", word2 = "ab"

Output: [0,1]
```
 

**Constraints:**

* `1 <= word2.length < word1.length <= 3 * 10^5`
* `word1` and `word2` consist only of lowercase English letters.

# Submissions
---
**Solution 1: (Greeedy, find first match)**
```
Runtime: 171 ms
Memory: 104.54 MB
```
```c++
class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<int> last(n, -1), ans;
        int i, j;
        for (i = m - 1, j = n - 1; i >= 0; i--) {
            if (j >= 0 && word1[i] == word2[j]) {
                last[j] = i;
                j--;
            }
        }
        j = 0;
        bool skip = false;
        for (i = 0; i < m; i++) {
            if (j < n) {
                bool letterMatch = word1[i] == word2[j];
                if (letterMatch || (!skip && (j == n - 1 || (i + 1 <= last[j + 1])))) {
                    if (!letterMatch)
                        skip = true;
                    ans.push_back(i);
                    j++;
                }
            }
        }

        return j == n ? ans : vector<int>();
    }
};
```

**Solution 2: (Prefix and Suffix Decomposition + Greedy, precompute each character's last possible index to form target then try to replace smallest unmatched source without violate next target character's last possible index, can only replace one to form smallest = try to replace as samll as possible while check next character right possibility)**

             0 1 2 3 4
    word1 = "v b c c a", word2 = " a b c"
last                              -1 1 3
skip                               1
res                                0 1 2
-------------------------------------------
             0 1 2 3 4
    word1 = "b a c d c", word2 = " a b c"
last                              -1 0 4
skip                                 1
res                                1 2 4

```
Runtime: 31 ms, Beats 94.68%
Memory: 109.20 MB, Beats 55.32%
```
```c++
class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.length(), m = word2.length();

        // right possible bound
        vector<int> last(m, -1);
        int j = m - 1;
        for (int i = n - 1; i >= 0; --i) {
            if (j >= 0 && word1[i] == word2[j]) {
                // word2 length == 1 always valid

                last[j] = i;
                j -= 1;
            }
        }
        vector<int> res;
        int skip = 0;
        j = 0;
        for (int i = 0; i < n; ++i) {
            if (j == m) break;
            if (word1[i] == word2[j] ||

                // try to replace current index as smallest while check next character right possibility
                (skip == 0 && (j == m - 1 || i < last[j + 1]))) {
                    skip += (word1[i] != word2[j] ? 1 : 0);
                    res.push_back(i);
                    j += 1;
            }
        }
        return j == m ? res : vector<int>();
    }
};
```
