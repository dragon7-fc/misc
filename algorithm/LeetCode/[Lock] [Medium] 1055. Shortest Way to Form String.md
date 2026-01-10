1055. Shortest Way to Form String

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings `source` and `target`, return the minimum number of subsequences of `source` such that their concatenation equals target. If the task is impossible, return `-1`.

 

**Example 1:**
```
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
```

**Example 2:**
```
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
```

**Example 3:**
```
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
```

**Constraints:**

* Both the `source` and `target` strings consist of only lowercase English letters from `"a"-"z"`.
* The lengths of `source` and `target` string are between `1` and `1000`.

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, j = 0, 0
        count = 1
        while j < len(target):
            i = source.find(target[j], i)
            if i == -1:
                i = source.find(target[j])
                if i == -1:
                    return -1
                count += 1
            i += 1
            j += 1
        return count
```

**Solution 2: (Greedy. Binary Search, Hash Table)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        h = collections.defaultdict(list)
        for i, ch in enumerate(source):
            h[ch].append(i)        
        i, j = -1, 0
        count = 1
        while j < len(target):
            if target[j] not in h:
                return -1
            idx = bisect.bisect(h[target[j]], i) 
            if idx == len(h[target[j]]):
                i = -1
                count += 1
                continue
            i = h[target[j]][idx]
            j += 1
        return count
```

**Solution 1: (Two Pointers)**
```
Runtime: 0 ms
Memory: 6.7 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Boolean array to mark all characters of source
        bool sourceChars[26] = {false};
        for (char c : source) {
            sourceChars[c - 'a'] = true;
        }

        // Check if all characters of target are present in source
        // If any character is not present, return -1
        for (char c : target) {
            if (!sourceChars[c - 'a']) {
                return -1;
            }
        }

        // Length of source to loop back to start of source using mod
        int m = source.length();

        // Pointer for source
        int sourceIterator = 0;

        // Number of times source is traversed. It will be incremented when
        // while finding occurrence of a character in target, sourceIterator
        // reaches the start of source again.
        int count = 0;

        // Find all characters of target in source
        for (char c : target) {

            // If while finding, iterator reaches start of source again,
            // increment count
            if (sourceIterator == 0) {
                count++;
            }

            // Find the first occurrence of c in source
            while (source[sourceIterator] != c) {

                // Formula for incrementing while looping back to start.
                sourceIterator = (sourceIterator + 1) % m;

                // If while finding, iterator reaches start of source again,
                // increment count
                if (sourceIterator == 0) {
                    count++;
                }
            }

            // Loop will break when c is found in source. Thus, increment.
            // Don't increment count until it is not clear that target has
            // remaining characters.
            sourceIterator = (sourceIterator + 1) % m;
        }

        // Return count
        return count;
    }
};
```

**Solution 2: (Inverted Index and Binary Search)**
```
Runtime: 8 ms
Memory: 9.1 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Array to store the vector of charToIndices of each character in source
        vector < int > charToIndices[26];
        for (int i = 0; i < source.size(); i++) {
            charToIndices[source[i] - 'a'].push_back(i);
        }

        // The current index in source
        int sourceIterator = 0;

        // Number of times we have to iterate through source to get target
        int count = 1;

        // Find all characters of target in source
        for (int i = 0; i < target.size(); i++) {

            // If the character is not present in source, return -1
            if (charToIndices[target[i] - 'a'].size() == 0) {
                return -1;
            }

            // Binary search to find the index of the character in source next to the source iterator
            vector < int > indices = charToIndices[target[i] - 'a'];
            int index = lower_bound(indices.begin(), indices.end(), sourceIterator) - indices.begin();

            // If we have reached the end of the list, we need to iterate
            // through source again, hence first index of character in source.
            if (index == indices.size()) {
                count++;
                sourceIterator = indices[0] + 1;
            } else {
                sourceIterator = indices[index] + 1;
            }
        }

        return count;
    }
};
```

**Solution 2: (2D Array)**
```
Runtime: 0 ms
Memory: 6.9 MB
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        // Next Occurrence of Character after Index
        int nextOccurrence[source.length()][26];

        // Base Case
        for (int c = 0; c < 26; c++) {
            nextOccurrence[source.length() - 1][c] = -1;
        }
        nextOccurrence[source.length() - 1][source[source.length() - 1] - 'a'] = source.length() - 1;

        // Fill using recurrence relation
        for (int idx = source.length() - 2; idx >= 0; idx--) {
            for (int c = 0; c < 26; c++) {
                nextOccurrence[idx][c] = nextOccurrence[idx + 1][c];
            }
            nextOccurrence[idx][source[idx] - 'a'] = idx;
        }

        // Pointer to the current index in source
        int sourceIterator = 0;

        // Number of times we need to iterate through source
        int count = 1;

        // Find all characters of target in source
        for (char c : target) {

            // If the character is not present in source
            if (nextOccurrence[0][c - 'a'] == -1) {
                return -1;
            }

            // If we have reached the end of source, or character is not in
            // source after source_iterator, loop back to beginning
            if (sourceIterator == source.length() || nextOccurrence[sourceIterator][c - 'a'] == -1) {
                count++;
                sourceIterator = 0;
            }

            // Next occurrence of character in source after source_iterator
            sourceIterator = nextOccurrence[sourceIterator][c - 'a'] + 1;
        }

        // Return the number of times we need to iterate through source
        return count;
    }
};
```

**Solution 3: (Greedy, Hash Table, Binary Search)**

    source = "x y z",
    target = "x z y x z"
j       0     1 3 2 1 3
mp
x: 0          
y: 1
z: 2
ans     1         2 3

```
Runtime: 0 ms, Beats 100.00%
Memory: 9.24 MB, Beats 36.56%
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        int n = source.size(), i, j, ans;
        vector<vector<int>> mp(26);
        for (i = 0; i < n; i ++) {
            mp[source[i] - 'a'].push_back(i);
        }
        j = 0;
        ans = 1;
        for (auto &c: target) {
            if (mp[c - 'a'].size() == 0) {
                return -1;
            }
            auto it = lower_bound(begin(mp[c - 'a']), end(mp[c - 'a']), j);
            if (it == end(mp[c - 'a'])) {
                ans += 1;
                j = mp[c - 'a'][0] + 1;
            } else {
                j = *it + 1;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Greedy, Hash Table, Prefix Sum)**

    source = "  x   y   z", target = "x z y x z"
dp              0   1   2
x               0      -1
y                   1  -1
z                       2

j                                  0  1 3 2 1 3
ans                                1      2 3
```
Runtime: 0 ms, Beats 100.00%
Memory: 8.94 MB, Beats 76.34%
```
```c++
class Solution {
public:
    int shortestWay(string source, string target) {
        int n = source.length(), i, j, dp[n][26], ans;
        for (j = 0; j < 26; j++) {
            dp[n - 1][j] = -1;
        }
        dp[n - 1][source[n - 1] - 'a'] = n - 1;
        for (i = n - 2; i >= 0; i--) {
            for (j = 0; j < 26; j++) {
                dp[i][j] = dp[i + 1][j];
            }
            dp[i][source[i] - 'a'] = i;
        }
        j = 0;
        ans = 1;
        for (auto &c: target) {
            if (dp[0][c - 'a'] == -1) {
                return -1;
            }
            if (j == n || dp[j][c - 'a'] == -1) {
                ans += 1;
                j = 0;
            }
            j = dp[j][c - 'a'] + 1;
        }
        return ans;
    }
};
````
