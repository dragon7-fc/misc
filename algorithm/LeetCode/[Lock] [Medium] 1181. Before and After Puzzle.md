1181. Before and After Puzzle

Given a list of `phrases`, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the **last word of the first phrase** is the same as the **first word of the second phrase**.

Return the Before and After puzzles that can be formed by every two phrases `phrases[i]` and `phrases[j]` where `i != j`. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of **distinct** strings **sorted lexicographically**.

 

**Example 1:**
```
Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]
```

**Example 2:**
```
Input: phrases = ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
Output: ["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"]
```

**Example 3:**
```
Input: phrases = ["a","b","a"]
Output: ["a"]
```

**Constraints:**

* `1 <= phrases.length <= 100`
* `1 <= phrases[i].length <= 100`

# Submissions
---
**Solution 1: (Haash Table)**
```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        
        # use two dictionary to remember each phrase's first and last word
        # key: first/last, val is the index
        first_dict, last_dict = defaultdict(list),defaultdict(list)
        for i in range(len(phrases)):
            p = phrases[i].split()
            first_dict[p[0]].append(i)
            last_dict[p[-1]].append(i)
        
        res = []
        for last in last_dict:
            if last in first_dict:
                for begin in last_dict[last]:
                    for end in first_dict[last]:
                        if begin != end:
                            res.append(phrases[begin] + phrases[end][len(last):])
        res = list(set(res))
        res.sort()
        return res
```