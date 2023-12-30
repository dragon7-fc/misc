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

**Solution 3: (Backtracking)**
```
Runtime: 8 ms
Memory: 6.3 MB
```
```c++
class Solution {
    void backtrack(vector<int>& count, int& res){
        for (int i = 0; i < count.size(); i++) {
            if (count[i] > 0) {
                res++;
                count[i]--;
                backtrack(count, res);
                count[i]++;
            }
        }
    }
public:
    int numTilePossibilities(string tiles) {
        unordered_map<char, int> m;
        for (const auto& it: tiles) {
            m[it]++;
        }
        vector<int> count;
        for (const auto& it: m) {
            count.emplace_back(it.second);
        }
        int res = 0;
        backtrack(count, res);
        return res;
    }
};
```
