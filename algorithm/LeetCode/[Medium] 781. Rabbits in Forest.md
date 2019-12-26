781. Rabbits in Forest

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those `answers` are placed in an array.

Return the minimum number of rabbits that could be in the forest.

**Examples:**
```
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
```

```
Input: answers = [10, 10, 10]
Output: 11
```

```
Input: answers = []
Output: 0
```

**Note:**

* `answers` will have length at most `1000`.
* Each `answers[i]` will be an integer in the range `[0, 999]`.

# Submissions
---
**Solution 1:**
```
Runtime: 44 ms
Memory Usage: 12.6 MB
```
```python
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        d = {}  # similar rabit -> current rabit
        count = 0
        for num in answers:
            # If there's no other rabit that has the same color,
            # the rabbit is one kind of its own
            if num == 0:
                count += 1
            else:
                # For a rabbit that has n rabbits similar to it, 
                # the minimum of rabbit there are is n + 1
                if num not in d:
                    d[num] = 1
                    count += (num + 1)
                else:
                    d[num] += 1
                    # If the number of similar rabbits is canceled out,
                    # we remove it from the hash table
                    if d[num] > num:
                        del d[num]
        return count
```