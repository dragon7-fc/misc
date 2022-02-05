438. Find All Anagrams in a String

Given a string **s** and a **non-empty** string **p**, find all the start indices of **p**'s anagrams in **s**.

Strings consists of lowercase English letters only and the length of both strings **s** and **p** will not be larger than `20,100`.

The order of output does not matter.

**Example 1:**
```
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

# Submissions
---
**Solution 1: (Sliding Window, Counter)**
```
Runtime: 172 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_counter = collections.Counter(p)
        running_counter = collections.Counter()
        len_p = len(p)
        result = []

        for i in range(len(s)):
            
            # If index  >= length of the pattern.
            # then decrement the count of the (i - len_p)th character to remove it from 
            # the current (sliding) window.
            if i >= len_p:
                if running_counter[s[i - len_p]] == 1:
                    del running_counter[s[i  - len_p]]
                else:
                    running_counter[s[i - len_p]] -= 1
            
            # Default: just increment the count of the current character.
            running_counter[s[i]] += 1
            
            # At any time, if running_counter == pattern_counter then append the result.
            if running_counter == pattern_counter:
                result.append(i - len_p + 1)

        return result
```

**Solution 2: (Sliding Window)**
```
Runtime: 41 ms
Memory Usage: 12.8 MB
```
```c
int isEquals(int sHash[],int pHash[]){
    for(int i=0;i<26;i++){
        if(sHash[i]!=pHash[i]){return 0;}
    }
    return 1;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAnagrams(char * s, char * p, int* returnSize){
    int *ret=(int*)malloc(sizeof(int)*100000);
    *returnSize=0;
    int sLen=strlen(s);
    int pLen=strlen(p);
    if(sLen<pLen){return NULL;}
    int pHash[26]={0};
    int sHash[26]={0};
    for(int i=0;i<sLen;i++){sHash[s[i]-'a']++;}
    for(int i=0;i<pLen;i++){
        if(sHash[p[i]-'a']==0){
            *returnSize=0;
            return NULL; 
        }
        pHash[p[i]-'a']++;
    }
    memset(sHash,0,26*sizeof(int));
    for(int i=0;i<pLen;i++){sHash[s[i]-'a']++;}
    if(isEquals(sHash,pHash)){ret[(*returnSize)++]=0;}
    for(int i=1;i<sLen-pLen+1;i++){
         sHash[s[i-1]-'a']--;
         sHash[s[i+pLen-1]-'a']++;
         if(isEquals(sHash,pHash)){ret[(*returnSize)++]=i;}
    }
    return ret;
}
```

**Solution 3: (Sliding Window)**
```
Runtime: 12 ms
Memory Usage: 8.7 MB
```
```c++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = s.length();
        int l = p.length();
        vector<int> ans;
        vector<int> vp(26, 0);
        vector<int> vs(26, 0);
        for (char c : p) ++vp[c - 'a'];    // fixed
        for (int i = 0; i < n; ++i) {
            if (i >= l) --vs[s[i - l] - 'a'];        
            ++vs[s[i] - 'a'];
            if (i >= l - 1 && vs == vp) ans.push_back(i + 1 - l);
        }
        return ans;
    }
};
```

**Solution 4: (Sliding Window, Counter)**
```
Runtime: 77 ms
Memory Usage: 12.7 MB
```
```c++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int M = s.size(), N = p.size();
        unordered_map<char, int> t, cnt;
        vector<int> ans;
        for (int i = 0; i < N; i ++) {
            t[p[i]] += 1;
        }
        for (int i = 0; i < M; i ++) {
            cnt[s[i]] += 1;
            if (cnt == t)
                ans.push_back(i-N+1);
            if (i >= N-1)
                if (cnt[s[i-N+1]] > 1)
                    cnt[s[i-N+1]] -= 1;
                else
                    cnt.erase(s[i-N+1]);
            
        }
        return ans;
    }
};
```
