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

**Solution 3: (Sliding Window, counter)**
```
Runtime: 3 ms
Memory: 8.75 MB
```
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size(), cnt[26] = {0}, cur[26] = {0}, i = 0, j, ii;
        bool flag;
        for (auto c: s1) {
            cnt[c-'a'] += 1;
        }
        for (j = 0; j < n; j ++) {
            cur[s2[j]-'a'] += 1;
            if (j < m-1) {
                continue;
            }
            flag = true;
            for (ii = 0; ii < 26; ii ++) {
                if (cnt[ii] != cur[ii]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                return true;
            }
            cur[s2[i]-'a'] -= 1;
            i += 1;
        }
        return false;
    }
};
```

**Solution 4: (Sliding Window, counter, optimized)**
```
Runtime: 8 ms
Memory: 8.62 MB
```
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size(), n = s2.size(), cnt[26] = {0}, cnt2[26] = {0}, i = 0, j, k = 0, l, r;
        if (m > n) {
            return false;
        }
        for (j = 0; j < m; j ++) {
            cnt[s1[j]-'a'] += 1;
            cnt2[s2[j]-'a'] += 1;
        }
        for (j = 0; j < 26; j ++) {
            k += cnt[j] == cnt2[j];
        }
        for (j = 0; j < n-m; j ++) {
            l = s2[j]-'a';
            r = s2[j+m]-'a';
            if (k == 26) {
                return true;
            }
            cnt2[r] += 1;
            if (cnt[r] == cnt2[r]) {
                k += 1;
            } else if (cnt2[r] == cnt[r] + 1) {
                k -= 1;
            }
            cnt2[l] -= 1;
            if (cnt[l] == cnt2[l]) {
                k += 1;
            } else if (cnt2[l] == cnt[l] - 1) {
                k -= 1;
            }
        }
        return k == 26;
    }
};
```
