418. Sentence Screen Fitting

Given a `rows x cols` screen and a `sentence` represented by a list of non-empty words, find how many times the given `sentence` can be fitted on the screen.

**Note:**

1. A word cannot be split into two lines.
1. The order of words in the `sentence` must remain unchanged.
1. Two consecutive words **in a line** must be separated by a single space.
1. Total words in the sentence won't exceed `100`.
1. Length of each word is greater than `0` and won't exceed `10`.
1. `1 ≤ rows, cols ≤ 20,000`.

**Example 1:**
```
Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
```

**Example 2:**
```
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
```

**Example 3:**
```
Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
```

# Submissions
---
**Solution 1: (String, Hash Table)**
```
Runtime: 236 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        N = len(sentence)
        nums = 0
        d = {}
        for _ in range(rows):
            cur = nums % N
            if sentence[cur] in d:
                nums += d[sentence[cur]]
            else:
                if len(sentence[cur]) > cols:
                    return 0
                count = 0
                idx = cur
                words = 0
                while count+len(sentence[idx]) <= cols:
                    words += 1
                    count += len(sentence[idx])+1
                    idx = (idx+1) % N
                d[sentence[cur]] = words
                nums += words
        return nums//N

```