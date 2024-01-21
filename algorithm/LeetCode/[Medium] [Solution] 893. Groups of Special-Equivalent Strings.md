893. Groups of Special-Equivalent Strings

You are given an array `A` of strings.

A move onto `S` consists of swapping any two even indexed characters of `S`, or any two odd indexed characters of `S`.

Two strings `S` and `T` are special-equivalent if after any number of moves onto `S`, `S == T`.

For example, `S = "zzxy"` and `T = "xyzz"` are special-equivalent because we may make the moves `"zzxy" -> "xzzy" -> "xyzz"` that swap `S[0]` and `S[2]`, then `S[1]` and `S[3]`.

Now, a group of special-equivalent strings from `A` is a non-empty subset of `A` such that:

1. Every pair of strings in the group are special equivalent, and;
1. The group is the largest size possible (ie., there isn't a string `S` not in the group such that `S` is special equivalent to every string in the group)

Return the number of groups of special-equivalent strings from `A`.

 
**Example 1:**
```
Input: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are ["xyzz", "zzxy"] and ["zzyx"].  Note that in particular, "zzxy" is not special equivalent to "zzyx".
```

**Example 2:**
```
Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
```

**Note:**

1. `1 <= A.length <= 1000`
1. `1 <= A[i].length <= 20`
1. All `A[i]` have the same length.
1. All `A[i]` consist of only lowercase letters.

# Solution
---
## Approach 1: Counting
**Intuition and Algorithm**

Let's try to characterize a special-equivalent string $S$, by finding a function $\mathcal{C}$ so that $S \equiv T \iff \mathcal{C}(S) = \mathcal{C}(T)$.

Through swapping, we can permute the even indexed letters, and the odd indexed letters. What characterizes these permutations is the count of the letters: all such permutations have the same count, and different counts have different permutations.

Thus, the function $\mathcal{C}(S)$ = (the count of the even indexed letters in `S`, followed by the count of the odd indexed letters in `S`) successfully characterizes the equivalence relation.

Afterwards, we count the number of unique $\mathcal{C}(S)$ for $S \in A$.

```python
class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
```

**Complexity Analysis**

* Time Complexity: $O(\sum\limits_{i} (A_i)\text{.length})$.

* Space Complexity: $O(N)$, where $N$ is the length of `A`.

# Submissions
---
**Solution: (Counting)**
```
Runtime: 44 ms
Memory Usage: 13.2 MB
```
```python
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})
```

**Solution 1: (Counter)**
```
Runtime: 17 ms
Memory Usage: 14.2 MB
```
```c++
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& words) {
        int n=words.size();
        
        // set is for grouping the strings.
        // The first element of pair is odd frequency
        // The second element of pair is even frequency
        set<pair<vector<int>,vector<int>>>dict;
        
        // odd vector stores the frequency at the odd positions of all the strings 
        vector<vector<int>>odd(n,vector<int>(26,0));
        
        // even vector stores the frequency at the even positions of all the strings 
        vector<vector<int>>even(n,vector<int>(26,0));
        for(int i=0;i<words.size();i++) {
            // calculate the frequency
            filler(words[i],odd[i],even[i]);
            
            // group the string 
            dict.insert({odd[i],even[i]});
        }
        
        // finally set size will the group size
        return dict.size();
    }
     // This function stores the character frequency of the odd and even positions of a string
    void filler(string &str,vector<int>&odd,vector<int>&even) {
        for(int i=0;i<str.length();i++) {
            if(i%2==0) {
                even[str[i]-'a']++;
            }
            else {
                odd[str[i]-'a']++;
            }
        }
    }
};
```

**Solution 2: (Set, String, Sort)**
```
Runtime: 8 ms
Memory Usage: 8.6 MB
```
```c++
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& words) {
        unordered_map<string,int>mp;
        for(int i=0;i<words.size();i++){
            string even="";
            string odd="";
            for(int j=0;j<words[i].size();j+=2)
            {
                even+=words[i][j];
            }
            for(int j=1;j<words[i].size();j+=2)
            {
                odd+=words[i][j];
            }
            sort(even.begin(),even.end());
            sort(odd.begin(),odd.end());
            mp[even+odd]++;//map size will return the ans;
            
        }
        return mp.size();
    }
};
```
