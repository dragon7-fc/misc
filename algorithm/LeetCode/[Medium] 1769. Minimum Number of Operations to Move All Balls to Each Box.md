1769. Minimum Number of Operations to Move All Balls to Each Box

You have `n` boxes. You are given a binary string boxes of length `n`, where `boxes[i]` is `'0'` if the `i`th box is empty, and `'1'` if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size `n`, where `answer[i]` is the minimum number of operations needed to move all the balls to the ith box.

Each `answer[i]` is calculated considering the initial state of the boxes.

 

**Example 1:**
```
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
```

**Example 2:**
```
Input: boxes = "001011"
Output: [11,8,5,4,3,4]
```

**Constraints:**

* `n == boxes.length`
* `1 <= n <= 2000`
* `boxes[i]` is either `'0'` or `'1'`.

# Submissions
---
**Solution 1: (Current and accumulate)**
```
Runtime: 72 ms
Memory Usage: 14.7 MB
```
```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        curr, steps = 0, 0
        for i in range(n):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        curr, steps = 0, 0
        for i in reversed(range(n)):
            answer[i] += steps
            if boxes[i] == '1': curr += 1
            steps += curr
        return answer
```

**Solution 2: (Sum of Left and Right Moves)**

        0   0   1   0   1   1
      -----------------------
       11,  8,  5,  4,  3,  4
cur    11   8   5 1+2   1   0  cur+right
right   3   3   3   2   2   1   right += '1'
           <-
cur     0   0   0 0+1   2   4  cur+left
left    0   0   1   1   2   3
           ->

```
Runtime: 0 ms
Memory: 12.14 MB
```
```c++
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size(), i, cur = 0, left = 0, right = 0;
        vector<int> ans(n);
        for (i = n-1; i >= 0; i --) {
            cur += right;
            ans[i] = cur;
            right += boxes[i] == '1';
        }
        left = 0;
        cur = 0;
        for (i = 0; i < n; i ++) {
            cur += left;
            ans[i] += cur;
            left += boxes[i] == '1';
        }
        return ans;
    }
};
```
