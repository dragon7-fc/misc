567. Permutation in String

Given two strings **s1** and **s2**, write a function to return `true` if **s2** contains the permutation of **s1**. In other words, one of the first string's permutations is the substring of the second string.

 

**Example 1:**
```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

**Note:**

* The input strings only contain lower case letters.
* The length of both given strings is in range `[1, 10,000]`.

# Submissions
---
**Solution 1: (Two Pointers, Sliding Window)**
```
Runtime: 68 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        t = collections.Counter(s1)
        w = collections.Counter(s2[:M - 1])
        for i in range(M-1, N):
            w[s2[i]] += 1
            if w == t: 
                return True
            w[s2[i - M + 1]] -= 1
            if w[s2[i - M + 1]] == 0 : 
                del w[s2[i - M + 1]]

        return False
```
**Solution 2: (Sliding Window)**
```
Runtime: 10 ms
Memory: 7.3 MB
```
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> cur(26), goal(26);
        for(char c : s1) goal[c - 'a']++;
        for(int i = 0; i < s2.size(); i++) {
            cur[s2[i] - 'a']++;
            if(i >= s1.size()) cur[s2[i - s1.size()] - 'a']--;
            if(goal == cur) return true;
        }
        return false;
    }
};
```

**Solution 3: (Sliding Window, Hash Table)**
```
Runtime: 17 ms
Memory: 8.1 MB
```
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> cur(26), goal(26);
        for(char c : s1) goal[c]++;
        for(int i = 0; i < s2.size(); i++) {
            cur[s2[i]] ++;
            if(i >= s1.size()) {
                cur[s2[i - s1.size()]] --;
                if (cur[s2[i - s1.size()]] == 0) {
                    cur.erase(s2[i - s1.size()]);
                }
            }
            if(goal == cur) return true;
        }
        return false;
    }
};
```
