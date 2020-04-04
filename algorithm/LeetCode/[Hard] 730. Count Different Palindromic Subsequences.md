730. Count Different Palindromic Subsequences

Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo `10^9 + 7`.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `A_1, A_2, ...` and `B_1, B_2, ...` are different if there is some i for which A_i != B_i.

**Example 1:**
```
Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
```

**Example 2:**
```
Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
```

**Note:**

* The length of S will be in the range `[1, 1000]`.
* Each character S[i] will be in the set `{'a', 'b', 'c', 'd'}`.

### Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 1064 ms
Memory Usage: 82 MB
```
```python
'''
DP
One key observation is S[i] can only be 'a', 'b', 'c' or 'd'
So for any Palindrom subsequence, it must be 'a*a', 'b*b', 'c*c', 'd*d', 'a', 'b', 'c', 'd'. * means 0 or more letters.
For a given string, the total of different Palindrom subsequence is the total count of each type of Palindrom subsequence: 
count of 'a*a' + count of 'b*b' + count of 'c*c' + count of 'd*d' + count of 'a' + count of 'b' + count of 'c' + count of 'd'
Take calculating count of 'a*a' as an example, we need find the index of beginning 'a' and the index of ending 'a'.
If the beining index is euqal to ending index, the count is 1.
Else plus 2 to the total different Palindrom subsequence of the subsequence * between the beining 'a' and the ending 'a'.
Here plus 2 means 'a' and 'aa' are two new Palindrom subsequences.
'cacc': a->1; b->0; d->0; c-> diff Palindrom of 'ac' + 2 = 4, so total is 5.
Use bottom up DP to calculate short substring and then longer substring.
DP[i][j] is the number of different non-empty palindromic subsequences for S[i:j+1]
If j-i <= 1, then DP[i][j] is always j-i+1
Time: O(n^2)
Space: O(n^2)
'''
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        
        @functools.lru_cache(None)
        def dfs(start, end):
            if end <= start + 1:
                return end - start + 1
            count = 0
            segment = S[start:end+1]
            for x in 'abcd':
                i = segment.find(x)
                j = segment.rfind(x)
                if i == j == -1:
                    continue
                i += start
                j += start
                count += dfs(i+1, j-1) + 2 if i != j else 1
            return count % (10**9 + 7)

        return dfs(0, len(S)-1)
```