461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, calculate the Hamming distance.

**Note:**

* `0 ≤ x, y < 231`.

**Example:**
```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")
```

**Solution 2: (Bit Manipulation)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int res = x ^ y;  // res contains all set bits for each bit different in X and Y
        int ans = 0;  // Total ans
        while(res > 0){
            ans += res & 1;  // if the bit is set increment ans
            res = res>>1; // right shift bits of res so that the bit to consider is at one's place
        }
        return ans; // return total count
    }
};
```