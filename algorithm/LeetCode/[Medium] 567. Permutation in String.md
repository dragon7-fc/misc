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
**Solution 1: (Sliding Window, Hash Table)**
```
Runtime: 23 ms
Memory Usage: 8.6 MB
```
```c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        map<char, int> m1, m2;
        int n1 = s1.size(), n2 = s2.size();
        if(n1>n2){
            return 0;
        }
        for(int i=0; i<n1; i++){
            m1[s1[i]]++;
            m2[s2[i]]++;
        }
        int i=0, j=n1;
        while(j<n2){
            if(m1==m2){
                return 1;
            }
            else{
                m2[s2[i]]--;
                if(m2[s2[i]] == 0){
                    m2.erase(s2[i]);
                }
                i++;
                m2[s2[j++]]++;
            }            
        }
        if(m1==m2){
            return 1;
        }
        return 0;
    }
};
```
