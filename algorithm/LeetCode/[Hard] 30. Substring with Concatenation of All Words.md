30. Substring with Concatenation of All Words

You are given a string, **s**, and a list of words, **words**, that are all of the same length. Find all starting indices of substring(s) in **s** that is a concatenation of each word in **words** exactly once and without any intervening characters.

 

**Example 1:**
```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

**Example 2:**
```
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
```

# Submissions
---
**Solution 1: (Sliding Window, Hash Table)**
```
Runtime: 460 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        lw, lws, ls = len(words[0]), len(words), len(s)
        totallen = lw * lws
        if ls < totallen: return []
        rst, ct = [], collections.Counter(words)
        for i in range(ls-totallen+1):
            ctt, j = {}, 0
            while j < lws:
                cur = s[i + j*lw:i + (j+1)*lw]
                ctt[cur] = ctt.get(cur, 0) + 1
                if ctt[cur] > ct[cur]: break
                j += 1
            if j == lws: rst.append(i)
        return rst
```

**Solution 2: (Sliding Window, DFS, Set)**
```
Runtime: 4188 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        N = len(words[0])
        if len(s) < N*len(words):
            return []
        i = 0
        location = []
        
        def recursion(firstWord, words, s, location, N):
            if not words:
                return location
            if firstWord in set(words):
                words.remove(firstWord)
                pos = recursion(s[location+N:location+2*N], words, s, location+N, N)
                if pos == -1:
                    return -1
                else:
                    return location
            else:
                return -1
            
        while i < len(s):
            firstWord = s[i:i+N]
            pos = recursion(firstWord, words[:], s, i, N)
            if pos != -1:
                location.append(pos)
            i += 1
        return location
```

**Solution 3: (DFS, Hash Table)**
```
Runtime: 855 ms
Memory Usage: 295.8 MB
```
```c++
class Solution {
    int M, N, L;
    int dfs(int i, unordered_map<string, int>& cnt, string& s, vector<string>& words) {
        if (!cnt[s.substr(i, M)]) {
            return i;
        }
        cnt[s.substr(i, M)] -= 1;
        return dfs(i+M, cnt, s, words);
    }
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        M = words[0].size();
        L = words.size();
        N = s.size();
        unordered_map<string, int> m;
        for (auto word: words)
            m[word] += 1;
        vector<int> ans;
        for (int i = 0; i <= N-M*L; i ++) {
            unordered_map<string, int> cur(m);
            if (dfs(i, cur, s, words) == i+M*L)
                ans.push_back(i);
        }
        return ans;
    }
};
```

**Solution 4: (String, Hash Table)**
```
Runtime: 247 ms
Memory Usage: 24.6 MB
```
```c++
class Solution {
    bool checkIt(string& s, unordered_map<string,int>& ogMap, int start, int size, int checkSize) {
        int i = start;
        int n = s.length();
        unordered_map<string, int> winMap;
        while(i < n) {
            string right = s.substr(i, size);
            if(ogMap.find(right) == ogMap.end()) return false;
            else {
                winMap[right]++;
                if(winMap[right] > ogMap[right]) return false;
                if(winMap == ogMap) return true;
                i += size;
            }
        }
        return false;
    }
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;
        int size = words[0].size();
        int checkSize = words.size();
        int superLen = size*checkSize;
        unordered_map<string, int> ogMap;
        for(auto& word : words) {
            ogMap[word]++;
        }
        
        int n = s.length();
        for(int i = 0; i < n - superLen + 1; i++) {
            if(checkIt(s, ogMap, i, size, checkSize)) {
                ans.push_back(i);
            }
        }
        
        return ans;
    }
};
```
