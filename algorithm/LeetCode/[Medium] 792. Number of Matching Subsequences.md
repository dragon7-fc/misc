792. Number of Matching Subsequences

Given a string `s` and an array of strings `words`, return the number of `words[i]` that is a subsequence of `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.
 

**Example 1:**
```
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
```

**Example 2:**
```
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
```

**Constraints:**

* `1 <= s.length <= 5 * 10^4`
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 50`
* `s` and `words[i]` consist of only lowercase English letters.

# Submissions
---
**Solution 1: (Rolling Hash)**
```
Runtime: 504 ms
Memory Usage: 15.2 MB
```
```python
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
```

**Solution 2: (Brute Force)**
```
Runtime: 292 ms
Memory Usage: 15.6 MB
```
```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            i = -1
            for c in word:
                i = s.find(c, i+1)
                if i < 0:
                    break
            if i >= 0:
                ans += 1
        return ans
```

**Solution 3: (Brute Force)**
```
Runtime: 218 ms
Memory Usage: 29.7 MB
```
```c++
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int ans=0;
        for(int i=0; i<words.size(); i++) {
            int wsize = words[i].size(); 
            int pos=0, j=0; 
            for(; j<wsize; j++) {
                auto ix = s.find(words[i][j], pos);
                if(ix == string::npos) break;
                pos=ix+1;
            }
            if(j==wsize) ans++;
        }
        return ans;
    }
};
```

**Solution 4: (Brute Force)**
```
Runtime: 202 ms
Memory Usage: 31.5 MB
```
```c++
class Solution {
    bool hasMatches(string &curr, string &s) {
        int pos = 1;
        int i = s.find(curr[0]);
        if (i == -1)
            return false;
        while (pos < curr.length()) {
            i = s.find(curr[pos], i + 1);
            if (i == -1)
                return false;
            pos++;
        }
        return true;
    }
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int count = 0;
        for (string str : words)
            if (hasMatches(str, s))
                count++;
        
        return count;
    }
};
```

**Solution 5: (Hash Table, Binary Search)**
```
untime: 135 ms
Memory: 54.85 MB
```
```c++
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int n = s.length();
        int m = words.size();
        vector<vector<int>> char_map(26);
        for(int i=0;i<n;i++){
            int ch=s[i]-'a';
            char_map[ch].push_back(i);
        }
        int count=0;
        for(int i=0;i<m;i++){
            int last=-1;
            int flag=1;
            for(int j=0;j<words[i].length();j++){
                int ch=words[i][j]-'a';
                //go for upper bound
                if(char_map[ch].size()==0){
                    flag=0;
                    break;
                }
                auto it=upper_bound(char_map[ch].begin(),char_map[ch].end(),last);
                if (it==char_map[ch].end()) {
                    flag=0;
                    break;
                } else {
                    last=*it;
                }
            }
            if (flag) {
                count+=1;
            }
        }
        return count;
    }
};
```

**Solution 6: (Hash Table, Binary Search)**

                           0   0 1   0 1 2   0 1 2
    s = "abcde", words = ["a","b b","a c d","a c e"]
g                                            
a: 0                       0         0       0
b: 1                           1 2x
c: 2                                   2       2
d: 3                                     3
e: 4                                             4

ans                         1            2       3

```
Runtime: 51 ms, Beats 88.93%
Memory: 55.44 MB, Beats 63.91%
```
```c++
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int m = s.length(), n = words.size(), i, j, j0, ans = 0;
        bool flag;
        vector<vector<int>> pre(26);
        for (i = 0; i < m; i ++) {
            pre[s[i] - 'a'].push_back(i);
        }
        for (i = 0; i < n; i ++) {
            j0 = -1;
            flag = true;
            for (j = 0; j < words[i].length(); j ++) {
                auto a = words[i][j] - 'a';
                auto it = upper_bound(pre[a].begin(), pre[a].end(), j0);
                if (it == pre[a].end()) {
                    flag = false;
                    break;
                } else {
                    j0 = *it;
                }
            }
            if (flag) {
                ans += 1;
            }
        }
        return ans;
    }
};
```
