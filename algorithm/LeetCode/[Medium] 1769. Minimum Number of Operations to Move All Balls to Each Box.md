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

**Solution 2: (LTR + RTL)**
```
Runtime: 4 ms
Memory: 9.3 MB
```
```c++
class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> res(boxes.length()); 
        for (int i = 0, ops = 0, cnt = 0; i < boxes.length(); ++i) {
            res[i] += ops;
            cnt += boxes[i] == '1' ? 1 : 0;
            ops += cnt;
        }
        for (int i = boxes.length() - 1, ops = 0, cnt = 0; i >= 0; --i) {
            res[i] += ops;
            cnt += boxes[i] == '1' ? 1 : 0;
            ops += cnt;
        }
        return res;
    }
};
```
