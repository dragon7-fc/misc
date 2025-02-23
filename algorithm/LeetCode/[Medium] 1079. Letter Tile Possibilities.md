1079. Letter Tile Possibilities

You have a set of `tiles`, where each tile has one letter `tiles[i]` printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

**Example 1:**
```
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
```

**Example 2:**
```
Input: "AAABBC"
Output: 188
```

**Note:**

* `1 <= tiles.length <= 7`
* `tiles` consists of uppercase English letters.

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 156 ms
Memory Usage: 22.2 MB
```
```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(seq, path):
            ans.add(path)
            for i in range(len(seq)):
                backtrack(seq[:i] + seq[i+1:], path + seq[i])
        ans = set()
        backtrack(tiles, "")
        
        return len(ans)-1
```

**Solution 2: (itertools)**
```
Runtime: 52 ms
Memory Usage: 14 MB
```
```python
import functools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return functools.reduce(operator.add , map(lambda x: len(set(itertools.permutations(tiles ,x))), range(1 , len(tiles)+1)))
```

**Solution 3: (Backtracking, Set, O(n * n!))**
```
Runtime: 8 ms
Memory: 6.3 MB
```
```c++
class Solution {
    void bt(int k, string &cur, unordered_set<string> &ans, int visited, string tiles) {
        if (k == 0) {
            ans.insert(cur);
            return;
        }
        for (int i = 0; i < tiles.size(); i ++) {
            if ((visited&(1<<i)) == 0) {
                cur += tiles[i];
                visited ^= (1<<i);
                bt(k-1, cur, ans, visited, tiles);
                cur.pop_back();
                visited ^= (1<<i);
            }
        }
    }
public:
    int numTilePossibilities(string tiles) {
        int n = tiles.size(), k, visited = 0;
        string cur;
        unordered_set<string> ans;
        for (k = 1; k <= n; k ++) {
            cur = "";
            bt(k, cur, ans, visited, tiles);
        }
        return ans.size();
    }
};
```

**Solution 4: (Backtracking, Counter, O(n!))**
```
Runtime: 3 ms, Beats 78.62%
Memory: 7.83 MB, Beats 92.23%
```
```c++
class Solution {
    void bt(vector<int> &cnt, int &ans) {
        for (int i = 0; i < 26; i ++) {
            if (cnt[i]) {
                ans += 1;
                cnt[i] -= 1;
                bt(cnt, ans);
                cnt[i] += 1;
            }
        }
    }
public:
    int numTilePossibilities(string tiles) {
        int n = tiles.size(), ans = 0;
        vector<int> cnt(26);
        for (auto t: tiles) {
            cnt[t-'A'] += 1;
        }
        bt(cnt, ans);
        return ans;
    }
};
```

**Solution 5: (Backtracking, Math, O(n * 2^n))**
```
Runtime: 1 ms, Beats 88.19%
Memory: 10.75 MB, Beats 52.62%
```
```c++
class Solution {
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        }

        int result = 1;
        for (int num = 2; num <= n; num++) {
            result *= num;
        }
        return result;
    }

    int countPermutations(string& seq) {
        // Count frequency of each character
        int charCount[26] = {0};
        for (char ch : seq) {
            charCount[ch - 'A']++;
        }

        // Calculate permutations using factorial formula
        int total = factorial(seq.length());
        for (int count : charCount) {
            if (count > 1) {
                total /= factorial(count);
            }
        }
        return total;
    }

    int generateSequences(string& tiles, string current, int pos,
                          unordered_set<string>& seen) {
        if (pos >= tiles.length()) {
            // If new sequence found, count its unique permutations
            if (seen.insert(current).second) {
                return countPermutations(current);
            }
            return 0;
        }

        // Try including and excluding current character
        return generateSequences(tiles, current, pos + 1, seen) +
               generateSequences(tiles, current + tiles[pos], pos + 1, seen);
    }
public:
    int numTilePossibilities(string tiles) {
        unordered_set<string> seen;

        // Sort characters to handle duplicates efficiently
        sort(tiles.begin(), tiles.end());

        // Find all unique sequences and their permutations
        return generateSequences(tiles, "", 0, seen) - 1;
    }
};
```
