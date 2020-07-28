390. Elimination Game

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

**Example:**
```
Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
```

# Submissions
---
**Solution 1: (Two Pointers)**
```
Runtime: 36 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def lastRemaining(self, n: int) -> int:
        delta = 1
        left = 1
        right = n
        size = n
        leftToRight = True
        while size > 1:
            if leftToRight:
                left += delta;
                if size%2 == 1:
                    right -= delta
            else:
                right -= delta
                if size % 2 == 1:
                    left += delta
            size //= 2
            delta *= 2
            leftToRight = not leftToRight
            
        return left
```

**Solution 2: (Two Pointers)**
```
Runtime: 8 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int lastRemaining(int n) {
        int delta = 1;
        int left = 1;
        //int right = n % 2 == 1 ? --n : n;
        int right = n;
        int size = n;
        bool leftToRight = true;
        while(size > 1) {
            if(leftToRight) {
                left += delta;
                if(size % 2 == 1) right -= delta;
            } else {
                right -= delta;
                if(size % 2 == 1) left += delta;
            }
            size /= 2;
            delta *= 2;
            leftToRight = !leftToRight;
        }
        return left;
    }
};
```