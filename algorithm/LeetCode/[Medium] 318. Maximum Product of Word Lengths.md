318. Maximum Product of Word Lengths

Given a string array `words`, find the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return `0`.

**Example 1:**
```
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
```

**Example 2:**
```
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
```

**Example 3:**
```
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 428 ms
Memory Usage: 13.1 MB
```
```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words: return 0
        N = len(words)
        ans, hashword = 0, [0] * N 
        for i in range(N):
            for j in words[i]:
                hashword[i] |= 1 << (ord(j) - ord('a'))
        for i in range(N):
            for j in range(i+1, N):
                if not (hashword[i] & hashword[j]): 
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 40 ms
Memory Usage: 15.6 MB
```
```c++
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size();
         
        vector<int> state(n);
         
        auto getState = [](string &s){
            int state = 0;

            for(char ch: s){
                state |=  1 << (ch - 'a');
            }
            return state;
        };
        
        for(int i=0; i<n; i++){
            state[i] = getState(words[i]);
        }
        int ans = 0;
        
        for(int i=0; i<n; i++){
            for(int j = i+1; j<n ; j++){
                if( (state[i] & state[j]) == 0)  {
                    ans = max(ans, (int)words[i].size() * (int)words[j].size());
                }
            }
        }
        
        return ans;
    }
};
```
