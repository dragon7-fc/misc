2531. Make Number of Distinct Characters Equal

You are given two **0-indexed** strings `word1` and `word2`.

A move consists of choosing two indices `i` and `j` such that `0 <= i < word1.length` and `0 <= j < word2.length` and swapping `word1[i]` with `word2[j]`.

Return `true` if it is possible to get the number of distinct characters in `word1` and `word2` to be equal with **exactly one** move. Return `false` otherwise.

 

**Example 1:**
```
Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
```

**Example 2:**
```
Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
```

**Example 3:**
```
Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
```

**Constraints:**

* `1 <= word1.length, word2.length <= 10^5`
* `word1` and `word2` consist of only lowercase English letters.

# Submissions
---
**Solution 1: (Brute Force on all character)**
```
Runtime: 125 ms
Memory: 15.2 MB
```
```python
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
            
        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:
                if c1 not in cnt1 or c2 not in cnt2:
                    continue
				# remove c1 from word1 and put c2 in word1
                cnt1[c1] -= 1
                if cnt1[c1] == 0:
                    del cnt1[c1]
                cnt1[c2]+=1
                
				# remove c2 from word2 and put c1 in word2
                cnt2[c2] -= 1
                if cnt2[c2] == 0:
                    del cnt2[c2]
                cnt2[c1]+=1
                
                if len(cnt1)== len(cnt2):  # if size of both dicts are equal then possible return true
                    return True
                
				
				# reset back the dicts
                cnt1[c1] += 1
                cnt1[c2] -= 1
                if cnt1[c2] == 0:
                    del cnt1[c2]
                
                cnt2[c2] += 1
                cnt2[c1] -= 1
                if cnt2[c1] == 0:
                    del cnt2[c1]
                
        return False
```
