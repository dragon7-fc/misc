3223. Minimum Length of String After Operations

You are given a string `s`.

You can perform the following process on `s` any number of times:

* Choose an index `i` in the string such that there is **at least** one character to the left of index `i` that is equal to `s[i],` and at least one character to the right that is also equal to `s[i]`.
* Delete the closest character to the left of index `i` that is equal to `s[i]`.
* Delete the closest character to the right of index `i` that is equal to `s[i]`.

Return the **minimum** length of the final string `s` that you can achieve.

 

**Example 1:**
```
Input: s = "abaacbcbb"

Output: 5

Explanation:
We do the following operations:

Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
```

**Example 2:**
```
Input: s = "aa"

Output: 2

Explanation:
We cannot perform any operations, so we return the length of the original string.
```
 

**Constraints:**

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of lowercase English letters.

# Submissions
---
**Solution 1: (Prefix sum)**
```
Runtime: 136 ms
Memory: 87.76 MB
```
```c++
class Solution {
public:
    int minimumLength(string s) {
        int n = s.size(), i;
        vector<vector<int>> right(26), left(26);
        vector<bool> visited(n);
        for (i = n-1; i >= 0; i --) {
            right[s[i]-'a'].push_back(i);
        }
        for (i = 0; i < n-1; i++) {
            if (right[s[i]-'a'].size() && right[s[i]-'a'].back() == i) {
                right[s[i]-'a'].pop_back();
            }
            if (!visited[i]) {
                if (left[s[i]-'a'].size() && right[s[i]-'a'].size()) {
                    visited[left[s[i]-'a'].back()] = true;
                    visited[right[s[i]-'a'].back()] = true;
                    left[s[i]-'a'].pop_back();
                    right[s[i]-'a'].pop_back();
                }
                left[s[i]-'a'].push_back(i);
            }
        }
        return count(visited.begin(), visited.end(), false);
    }
};
```

**Solution 2: (Counter, summary)**

min length -> remove max -> remove method

remove method:
1)    a .. a .. a                   -> .. a ..
2)    a .. a .. a .. a              -> .. a .. .. a
3)    a .. a .. a .. a .. a         -> .. .. a .. ..
4)    a .. a .. a .. a .. a .. a    -> .. .. .. a .. .. a 
    
```
Runtime: 90 ms
Memory: 30.42 MB
```
```c++
class Solution {
public:
    int minimumLength(string s) {
        int cnt[26] = {0};
        for (auto c: s) {
            cnt[c-'a'] += 1;
        }
        int ans = 0;
        for (int i = 0; i < 26; i ++) {
            if (cnt[i] >= 3) {
                cnt[i] = cnt[i]%2 ? 1 : 2;
            }
            ans += cnt[i];
        }
        return ans;
    }
};
```
