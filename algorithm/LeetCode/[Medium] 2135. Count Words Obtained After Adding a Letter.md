2135. Count Words Obtained After Adding a Letter

You are given two **0-indexed** arrays of strings `startWords` and `targetWords`. Each string consists of lowercase English letters only.

For each string in `targetWords`, check if it is possible to choose a string from `startWords` and perform a **conversion operation** on it to be equal to that from `targetWords`.

The **conversion operation** is described in the following two steps:

**Append** any lowercase letter that is **not present** in the string to its end.
* For example, if the string is `"abc"`, the letters `'d'`, `'e'`, or `'y'` can be added to it, but not `'a'`. If `'d'` is added, the resulting string will be `"abcd"`.

**Rearrange** the letters of the new string in any arbitrary order.
* For example, `"abcd"` can be rearranged to `"acbd"`, `"bacd"`, `"cbda"`, and so on. Note that it can also be rearranged to `"abcd"` itself.

Return the **number of strings** in `targetWords` that can be obtained by performing the operations on any string of `startWords`.

**Note** that you will only be verifying if the string in `targetWords` can be obtained from a string in `startWords` by performing the operations. The strings in `startWords` **do not** actually change during this process.

 

**Example 1:**
```
Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
Explanation:
- In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
  Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
- In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
```

**Example 2:**
```
Input: startWords = ["ab","a"], targetWords = ["abc","abcd"]
Output: 1
Explanation:
- In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
- There is no string in startWords that can be used to obtain targetWords[1] = "abcd".
```

**Constraints:**

* `1 <= startWords.length, targetWords.length <= 5 * 10^4`
* `1 <= startWords[i].length, targetWords[j].length <= 26`
* Each string of `startWords` and `targetWords` consists of lowercase English letters only.
* No letter occurs more than once in any string of `startWords` or `targetWords`.

# Submissions
---
**Solution 1: (Set)**
```
Runtime: 1101 ms
Memory: 33.9 MB
```
```python
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        src = collections.defaultdict(set)
        for word in startWords:
            src[len(word)].add(''.join(sorted(word)))
        ans = 0
        for word in targetWords:
            w = ''.join(sorted(word))
            for i in range(len(w)):
                cur = w[:i] + w[i+1:]
                if cur in src[len(w)-1]:
                    ans += 1
                    break
        return ans
```

**Solution 2: (Trie)**
```
Runtime: 2320 ms
emory: 39.2 MB
```
```
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        trie = {}
        for word in startWords:
            t = trie
            for c in sorted(word):
                t = t.setdefault(c, {})
            t['#'] = True
        ans = 0
        for word in targetWords:
            w = ''.join(sorted(word))
            n = len(word)
            for i in range(n):
                t = trie
                flag = True
                for j in range(n):
                    if j == i:
                        continue
                    t = t.get(w[j], None)
                    if t == None:
                        flag = False
                        break
                if t and not '#' in t:
                    flag = False
                if flag:
                    ans += 1
                    break
        return ans
```

**Solution 3: (Bitmask)**
```
Runtime: 226 ms
Memory: 99.1 MB
```
```c++
class Solution {
public:
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        auto get_mask = [](string &w){
            return accumulate(begin(w), end(w), 0, [](int mask, char ch){ return mask + (1 << (ch - 'a')); });  
        };
        unordered_set<int> s;
        for (auto &w : startWords)
            s.insert(get_mask(w));
        int res = 0;
        for (auto &w : targetWords) {
            int mask = get_mask(w);
            res += any_of(begin(w), end(w), [&](char ch){ return s.count(mask - (1 << (ch - 'a'))); });
        }
        return res;
    }
};
```
