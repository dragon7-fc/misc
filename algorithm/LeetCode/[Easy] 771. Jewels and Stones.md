771. Jewels and Stones

You're given strings `J` representing the types of stones that are jewels, and `S` representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in `J` are guaranteed distinct, and all characters in `J` and `S` are letters. Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

**Example 1:**
```
Input: J = "aA", S = "aAAbbbb"
Output: 3
```

**Example 2:**
```
Input: J = "z", S = "ZZ"
Output: 0
```

**Note:**

* S and J will consist of letters and have length at most 50.
* The characters in J are distinct.

# Submissions
---
**Solution 1:**
```
Runtime: 40 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set()
        for j in J:
            j_set.add(j)
        
        ans = 0
        for j in j_set:
            ans += S.count(j)
            
        return ans
```

**Solution 2:**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([x for x in J for y in S if x == y])
```