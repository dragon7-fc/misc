28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.

**Example 1:**
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2:**
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Clarification:**

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Submissions
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

**Solution 2: (String)**
```
Runtime: 260 ms
Memory Usage: 6.2 MB
```
```c


int strStr(char * haystack, char * needle){
    int hi, ni;
    int hlen = strlen(haystack);
    int nlen = strlen(needle);
    
    if (nlen > hlen)
        return -1;
    
    if (nlen == 0)
        return 0;
    
    for (hi = 0; hi < (hlen - nlen + 1); hi++) {
        if (strncmp(&haystack[hi], needle, nlen) == 0)
            return hi;
    }

    return -1;
}
```

**Solution 3: (String)**
```
Runtime: 0 ms
Memory: 6.3 MB
```
```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        return haystack.find(needle);
    }
};
```

**Solution 4: (KMP)**
```
Runtime: 0 ms
Memory: 6.3 MB
```
```c++
class Solution {
    vector<int> constructLsp(string pattern) {
        vector<int> lps(pattern.length() , 0);
        if(pattern == "") return lps;
        for (int i = 1 , prevPtr = 0; i < pattern.length();) {
            if(pattern[i] == pattern[prevPtr]) {
                lps[i] = prevPtr + 1;     
                prevPtr++;
                i++;
            }
            else {
                if (prevPtr == 0) {
                    lps[i] = 0;
                    i++;
                }
                else {
                    prevPtr = lps[prevPtr - 1];
                }
            }
        }
        return lps;
    }

    int kmp(string str , string pattern , vector<int>& lps) {
        int i = 0 , j = 0;
        while (i < str.length()) {
            if(str[i] == pattern[j]) {
                i++;
                j++;
            }
            else {
                if (j == 0){
                    i++;
                }
                else {
                    j = lps[j - 1];
                }
            }
            
            if(j == pattern.length()) return i - pattern.length();
        }
        return -1;
    }
public:
    int strStr(string haystack, string needle) {
        vector<int> lps = constructLsp(needle);
        return kmp(haystack , needle , lps);
    }
};
```
