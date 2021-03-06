1419. Minimum Number of Frogs Croaking

Given the string `croakOfFrogs`, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ **sequentially**. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

 

**Example 1:**
```
Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
```

**Example 2:**
```
Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
```

**Example 3:**
```
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
```

**Example 4:**
```
Input: croakOfFrogs = "croakcroa"
Output: -1
```

**Constraints:**

* `1 <= croakOfFrogs.length <= 10^5`
* All characters in the string are: `'c'`, `'r'`, `'o'`, `'a'` or `'k'`.

# Submissions
---
**Solution 1: (Greedy)**

Whenever a 'c' is encountered, you know that a frog has started to croak. This frog can be a new frog or one of the existing one. Whenever 'k' is encountered, you know that one of the frogs have stopped croaking, so whenever a new 'c' is encountered, we can reuse the same frog.

This is the basic idea.
* For 'c', increment in use frogs by one.
* For 'k' decrement the in use count by one.
* The maximum value reached by the in use count is the answer.

```
Runtime: 308 ms
Memory Usage: 14.6 MB
```
```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k, in_use, answer = 0, 0, 0, 0, 0, 0, 0
        for d in croakOfFrogs:
            if d == 'c':
                c, in_use = c+1, in_use+1
            elif d == 'r':
                r += 1
            elif d == 'o':
                o += 1
            elif d == 'a':
                a += 1
            else:
                k, in_use = k+1, in_use-1
                
            answer = max(answer, in_use)
            
            if c < r or r < o or o < a or a < k:
                return -1
            
        if in_use == 0 and c == r and r == o and o == a and a == k:
            return answer
        
        return -1
```