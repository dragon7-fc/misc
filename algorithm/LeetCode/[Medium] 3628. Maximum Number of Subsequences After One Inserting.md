3628. Maximum Number of Subsequences After One Inserting

You are given a string `s` consisting of uppercase English letters.

You are allowed to insert at most one uppercase English letter at **any** position (including the beginning or end) of the string.

Return the **maximum** number of `"LCT"` subsequences that can be formed in the resulting string after at most one insertion.

 

**Example 1:**
```
Input: s = "LMCT"

Output: 2

Explanation:

We can insert a "L" at the beginning of the string s to make "LLMCT", which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].
```

**Example 2:**
```
Input: s = "LCCT"

Output: 4

Explanation:

We can insert a "L" at the beginning of the string s to make "LLCCT", which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].
```

**Example 3:**
```
Input: s = "L"

Output: 0

Explanation:

Since it is not possible to obtain the subsequence "LCT" by inserting a single letter, the result is 0.
```
 

**Constraints:**

* `1 <= s.length <= 10^5`
* `s` consists of uppercase English letters.

# Submissions
---
**Solution 1: (Prefix Sum, Brute Force, try all solution)**
```
Runtime: 50 ms, Beats 52.08%
Memory: 45.14 MB, Beats 59.30%
```
```c++
class Solution {
    typedef long long ll;
public:
    long long numOfSubsequences(string s) {
        int n=s.size();
        vector<ll> prefix(n+1, 0); // lcount 1 based
        vector<ll> suffix(n+1, 0); // tcount 0 based
        for(int i=0; i<n; i++){
            if(s[i]=='L'){
                prefix[i+1]=1;
            }
            prefix[i+1]+=prefix[i];
        }
        for(int i=n-1; i>=0; i--){
            if(s[i]=='T'){
                suffix[i]=1;
            }
            suffix[i]+=suffix[i+1];
        }
        ll resWithC=0;
        ll bestPosForC=0;
        ll resWithL=0;
        ll resWithT=0;
        for(int i=0; i<n; i++){
            // if we place l or t to the left ot right
            // if place c has no effect
            if(s[i]=='C'){
                resWithC+=prefix[i]*suffix[i+1];
                resWithL+=(prefix[i]+1)*suffix[i+1];
                resWithT+=prefix[i]*(suffix[i+1]+1);
            }
            else{
                // if we place C
                bestPosForC = max(prefix[i]*suffix[i], bestPosForC);
            }
            
        }
        resWithC+=bestPosForC;
        return max({resWithL, resWithT, resWithC});
    }
};
```
