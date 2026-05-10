3926. Count Valid Word Occurrences

You are given an array of strings `chunks`. The strings are concatenated in order to form a single string `s`.

You are also given an array of strings `queries`.

A **word** is defined as a **substring** of `s` that:

* consists of lowercase English letters (`'a'` to `'z'`),
* may include hyphens (`'-'`) only if each hyphen is surrounded by lowercase English letters, and
* is not part of a longer substring that also satisfies the above conditions.

Any character that is not a lowercase English letter or a valid hyphen acts as a separator.

Return an integer array `ans` such that `ans[i]` is the number of occurrences of `queries[i]` as a word in `s`.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

 

**Example 1:**
```
Input: chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]

Output: [2,1,0]

Explanation:

Concatenating all strings in chunks gives s = "hello world hello".
The valid words in s are "hello" which appears twice and "world" which appears once.
Thus, the ans = [2, 1, 0].
```

**Example 2:**
```
Input: chunks = ["a--b a-","-c"], queries = ["a","b","c"]

Output: [2,1,1]

Explanation:

Concatenating all strings in chunks gives s = "a--b a--c".
The valid words in s are "a" which appears twice, "b" which appears once, and "c" which appears once.
Thus, the ans = [2, 1, 1].
```

**Example 3:**
```
Input: chunks = ["hello"], queries = ["hello","ell"]

Output: [1,0]

Explanation:

The valid word in s is "hello" which appears once.
Thus, the ans = [1, 0].
```

**Constraints:**

* `1 <= chunks.length <= 10^5`
* `1 <= chunks[i].length <= 10^5`
* `chunks[i]` may consist of lowercase English letters, spaces, and hyphens.
* The total length of all strings in `chunks` does not exceed `10^5`
* `1 <= queries.length <= 10^5`
* `1 <= queries[i].length <= 10^5`
* `queries[i]` is a valid word
* The total length of all strings in `queries` does not exceed `10^5`

# Submissions
---
**Solution 1: (String, Hash Table, stringstream)**
```
Runtime: 208 ms, Beats 14.32%
Memory: 237.11 MB, Beats 40.26%
```
```c++
class Solution {
public:
    vector<int> countWordOccurrences(vector<string>& chunks, vector<string>& queries) {
        string s, cs, cs2, pre;
        for (auto &chunk: chunks) {
            s += chunk;
        }
        int m = s.length(), n = queries.size(), i, j, k;
        unordered_map<string, int> cnt;
        stringstream ss(s);
        while (getline(ss, cs, ' ')) {
            if (cs == "") {
                continue;
            }
            stringstream ss2(cs);
            pre = "";
            while (getline(ss2, cs2, '-')) {
                if (cs2 == "") {
                    if (pre != "") {
                        cnt[pre] += 1;
                    }
                    pre = "";
                } else {
                    if (pre == "") {
                        pre += cs2;
                    } else {
                        pre += "-" + cs2;
                    }
                }
            }
            if (pre != "") {
                cnt[pre] += 1;
            }
        }
        vector<int> ans(n);
        for (i = 0; i < n; i ++) {
            ans[i] = cnt[queries[i]];
        }
        return ans;
    }
};
```

**Solution 1: (String, Hash Table)**
```
Runtime: 119 ms, Beats 41.91%
Memory: 236.62 MB, Beats 59.56%
```
```c++
class Solution {
public:
    vector<int> countWordOccurrences(vector<string>& chunks, vector<string>& queries) {
        string s = "";
        for (auto &chunk : chunks) {
            s += chunk;
        }
        unordered_map<string, int> cnt;
        int n = s.size(), i = 0;
        while (i < n) {
            // separator
            if (!isalpha(s[i])) {
                i += 1;
                continue;
            }
            string word = "";
            while (i < n) {
                // normal letter
                if (isalpha(s[i])) {
                    word += s[i];
                    i += 1;
                }

                // valid hyphen
                else if(s[i] == '-') {
                    bool left = !word.empty();
                    bool right = i + 1 < n && isalpha(s[i + 1]);
                    if (left && right) {
                        word += '-';
                        i += 1;
                    } else {
                        break;
                    }
                }

                // separator
                else {
                    break;
                }
            }

            cnt[word] += 1;
        }
        vector<int> ans;
        for (auto &q : queries) {
            ans.push_back(cnt[q]);
        }
        return ans;
    }
};
```
