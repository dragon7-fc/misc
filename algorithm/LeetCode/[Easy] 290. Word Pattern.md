290. Word Pattern

Given a `pattern` and a string `str`, find if `str` follows the same `pattern`.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `str`.

**Example 1:**
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

**Example 2:**
```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

**Example 3:**
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

**Example 4:**
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

**Notes:**

* You may assume pattern contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.

# Submissions
---
**Solution 1: (Two Hash Maps)**
```
Runtime: 32 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True
```

**Solution 2: (Single Index Hash Map)**
```
Runtime: 32 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_index = {}
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True
```

**Solution 3: (Hash Table)**
```
Runtime: 16 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        word = str.split()
        if len(word) != len(pattern): return False
        for i in range(len(pattern)):
            if not d.get(pattern[i], None):
                if word[i] in d.values():
                    return False
                d[pattern[i]] = word[i]
            else:
                if d[pattern[i]] != word[i]:
                    return False
        return True
```

**Solution 4: (Hash Table)**
```
Runtime: 0 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, int> p2i;
        unordered_map<string, int> w2i;
        
        istringstream in(s); string word;
        int i = 0, n = pattern.size();

        
        for(word; in>>word; i++){
            if(i==n || p2i[pattern[i]] != w2i[word]) return false; //If it reaches end before all the words in string 's' are traversed || if values of keys : pattern[i] & word don't match return false
            
            p2i[pattern[i]] = w2i[word] = i+1; //Otherwise map to both to a value i+1
        }
        return i==n; //both the lengths should be equal
    }
};
```

**Solution 5: (Hash Table)**
```
Runtime: 3 ms
Memory Usage: 6.7 MB
```
```c++
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> dic; // the projection map, key is the char in pattern and the value is a word
        set<string> word_set;
        set<char> pattern_set;
        vector<string> words;
        istringstream iss(s);
        string word;
        while (iss >> word) {  words.push_back(word); word_set.insert(word); }
        for (int i = 0; i < pattern.length(); i ++) pattern_set.insert(pattern[i]);
		// 'aa' -> 'dog', 'ab' -> 'dog dog', 'abc'- > 'cat dog cat'
        if (words.size() != pattern.length() || word_set.size() != pattern_set.size()) return false;
        for (int i = 0; i < words.size(); i++) {
            if (dic.count(pattern[i]) > 0) { // pattern[i] has been projected to some word
                if (dic[pattern[i]] != words[i]) return false; // 'aba' -> 'cat dog dog'
            } else {
                dic[pattern[i]] = words[i];
            }
        }
        return true;  
    }
};
```
