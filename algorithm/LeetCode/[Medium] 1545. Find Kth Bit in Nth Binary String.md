1545. Find Kth Bit in Nth Binary String

Given two positive integers `n` and `k`, the binary string  `Sn` is formed as follows:

* `S1 = "0"`
* `Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

* `S1 = "0"`
* `S2 = "011"`
* `S3 = "0111001"`
* `S4 = "011100110110001"`

Return the `k`th bit in `Sn`. It is guaranteed that `k` is valid for the given `n`.

 

**Example 1:**
```
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".
```

**Example 2:**
```
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001". The 11th bit is "1".
```

**Example 3:**
```
Input: n = 1, k = 1
Output: "0"
```

**Example 4:**
```
Input: n = 2, k = 3
Output: "1"
```

**Constraints:**

* `1 <= n <= 20`
* `1 <= k <= 2n - 1`

# Submissions
---
**Solution 1: ()**

**Explanation**

* If k is on the left part of the string, we do nothing.
* If K is right in the middle, we return flip directly.
* If k is on the right part of the string,

    * find it's symeric postion k = l + 1 - k.
    * Also we toggle flip ^= 1


**Complexity**

* Time O(n)
* Space O(1)


```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    char findKthBit(int n, int k) {
        int flip = 0, l = (1 << n) - 1;
        while (k > 1) {
            if (k == l / 2 + 1)
                return '0' + (flip ^ 1);
            if (k > l / 2) {
                k = l + 1 - k;
                flip ^= 1;
            }
            l /= 2;
        }
        return '0' + flip;
    }
};
```

**Solution 2: (DFS)**
```
Runtime: 28 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # base case
        if n == 1:
            return "0"
        
        # calculate length of S_n
        l = 2 ** n - 1
        
        # recursion
        mid = l // 2 + 1
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            return str(1 - int(self.findKthBit(n - 1, l - k + 1)))
```

**Solution 3: (DFS)**
```
Runtime: 28 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1: return "0"
        if k == 2**(n-1): return "1"
        if k < 2**(n-1): return self.findKthBit(n-1, k)
        return "0" if self.findKthBit(n-1, 2**n-k) == "1" else "1"
```

**Solution 3: (Bit Manipulation)**

S4 = "011100110110001"
             |  ^
S3 = "0111001"
         |^
S2 = "011"
       |^
S1 = "0"
      ^

```
Runtime: 0 ms
Memory: 7.34 MB
```
```c++
class Solution {
public:
    char findKthBit(int n, int k) {
        int ans = 0;
        while (k > 1) {
            if (k >= (1<<(n-1))) {
                ans ^= 1;
                if (k == 1<<(n-1)) {
                    break;
                }
                k = (1<<(n-1)) - (k - (1<<(n-1)));
            }
            n -= 1;
        }
        return ans + '0';
    }
};
```

**Solution 4: (Bit Manipulation)**

k  =  6 = 0b    1100
-k = -6 = 0b1...0100 


n = 4, k = 11
k  =  11 =     1011
-k = -11 = 1...0101
positionInSection = 1
isInInvertedPart = ((11/1)>>1)&1 == 1 -> true
originalBitIsOne = (11&1) == 0 -> false


```
Runtime: 0 ms
Memory: 7.35 MB
```
```c++
class Solution {
public:
    char findKthBit(int n, int k) {
        // Find the position of the rightmost set bit in k
        // This helps determine which "section" of the string we're in
        int positionInSection = k & -k;

        // Determine if k is in the inverted part of the string
        // This checks if the bit to the left of the rightmost set bit is 1
        bool isInInvertedPart = (((k / positionInSection) >> 1) & 1) == 1;

        // Determine if the original bit (before any inversion) would be 1
        // This is true if k is even (i.e., its least significant bit is 0)
        bool originalBitIsOne = (k & 1) == 0;

        if (isInInvertedPart) {
            // If we're in the inverted part, we need to flip the bit
            return originalBitIsOne ? '0' : '1';
        } else {
            // If we're not in the inverted part, return the original bit
            return originalBitIsOne ? '1' : '0';
        }
    }
};
```
