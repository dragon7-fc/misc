68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

**Note:**

* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
* The input array words contains at least one word.

**Example 1:**
```
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:**
```
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
```

**Example 3:**
```
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

# Submissions
---
**Solution 1: (String, Greedy)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst, arr, curlen = [], [], 0
        for word in words:
            if curlen + len(word) <= maxWidth:
                arr.append(word)
                curlen += len(word) + 1
            else:
                if len(arr) == 1: line = arr[0] + ' ' * (maxWidth-curlen+1)
                else:
                    div, mod = divmod(maxWidth - curlen + len(arr), len(arr)-1)
                    line = ''
                    for i in range(len(arr)-1):
                        line += arr[i]
                        line += ' ' * div
                        if i < mod: line += ' '
                    line += arr[-1]
                rst.append(line)
                arr, curlen = [word], len(word) + 1
        if arr: rst.append(' '.join(arr) + ' ' * (maxWidth-curlen+1))
        return rst
```