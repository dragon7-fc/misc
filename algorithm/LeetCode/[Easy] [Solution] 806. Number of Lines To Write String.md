806. Number of Lines To Write String

We are to write the letters of a given string `S`, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array `widths`, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.

 

**Example :**
```
Input: 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation: 
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.
```

**Example :**
```
Input: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]
Explanation: 
All letters except 'a' have the same length of 10, and 
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.
```

**Note:**

* The length of S will be in the range `[1, 1000]`.
* `S` will only contain lowercase letters.
* `widths` is an array of length `26`.
* `widths[i]` will be in the range of `[2, 10]`.

# Solution
---
## Approach #1: Insert Each Character [Accepted]
**Intuition**

We can write out each character in the string `S` one by one.

As we write characters, we can update `(lines, width)` that keeps track of how many lines we have used, and what is the length of the used space in the last line.

**Algorithm**

If the space w of the next character in `S` fits our current line, we will add it. Otherwise, we will start a new line, and use `w` space to put that character on the next line.

```python
class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width
```

**Complexity Analysis**

* Time Complexity: $O(S\text{.length})$, as we iterate through S.

* Space Complexity: $O(1)$ additional space, as we only use lines and width. (In Java, our `toCharArray` method makes this $O(S\text{.length})$, but we could use `.charAt` instead).

# Submissions
---
**Solution 1: (Insert Each Character, Greedy)**
```
Runtime: 56 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width
```

**Solution 2: (Greedy)**
```
Runtime: 4 ms
Memory Usage: 7 MB
```
```c++
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int lines = 1, current_sum = 0;
        
        for(char ch : S){
            current_sum += widths[ch - 'a'];
            
            if(current_sum > 100){
                current_sum = widths[ch - 'a'];
                lines++;
            }
        }
        
        return {lines, current_sum};
    }
};
```