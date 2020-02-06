191. Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

**Example 1:**
```
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

**Example 2:**
```
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

**Example 3:**
```
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

**Note:**

* Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

**Follow up:**

* If this function is called many times, how would you optimize it?

# Solution
---
## Approach #1 (Loop and Flip) [Accepted]
**Algorithm**

The solution is straight-forward. We check each of the 3232 bits of the number. If the bit is 11, we add one to the number of $1$-bits.

We can check the $i^{th}$ bit of a number using a bit mask. We start with a mask m=1m=1, because the binary representation of $1$ is,

$00000000000000000000000000000001$ Clearly, a logical AND between any number and the mask 11 gives us the least significant bit of this number. To check the next bit, we shift the mask to the left by one.

$00000000000000000000000000000010$

And so on.

**Java**
```java
public int hammingWeight(int n) {
    int bits = 0;
    int mask = 1;
    for (int i = 0; i < 32; i++) {
        if ((n & mask) != 0) {
            bits++;
        }
        mask <<= 1;
    }
    return bits;
```

**Complexity Analysis**

* The run time depends on the number of bits in nn. Because $n$ in this piece of code is a 32-bit integer, the time complexity is $O(1)$.

* The space complexity is $O(1)$, since no additional space is allocated.

## Approach #2 (Bit Manipulation Trick) [Accepted]
**Algorithm**

We can make the previous algorithm simpler and a little faster. Instead of checking every bit of the number, we repeatedly flip the least-significant $1$-bit of the number to $0$, and add $1$ to the sum. As soon as the number becomes $0$, we know that it does not have any more $1$-bits, and we return the sum.

The key idea here is to realize that for any number $n$, doing a bit-wise AND of $n$ and $n - 1$ flips the least-significant $1$-bit in $n$ to $0$. Why? Consider the binary representations of $n$ and $n - 1$.

![191_Number_Of_Bits.png](img/191_Number_Of_Bits.png)

Figure 1. AND-ing $n$ and $n-1$ flips the least-significant $1$-bit to 0.

In the binary representation, the least significant $1$-bit in $n$ always corresponds to a $0$-bit in $n - 1$. Therefore, anding the two numbers $n$ and $n - 1$ always flips the least significant $1$-bit in $n$ to $0$, and keeps all other bits the same.

Using this trick, the code becomes very simple.

**Java**
```java
public int hammingWeight(int n) {
    int sum = 0;
    while (n != 0) {
        sum++;
        n &= (n - 1);
    }
    return sum;
}
```

**mplexity Analysis**

* The run time depends on the number of $1$-its in $n$. In the worst case, all bits in $n$ are $1$-bits. In case of a 32-bit integer, the run time is $O(1)$.

* The space complexity is $(1)$ since no additional space is allocated.

# Submissions
---
**Solution 1: (Bit Manipulation)**
```
Runtime: 4 ms
Memory Usage: 11.7 MB
```
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n != 0:
            ans += 1
            n &= (n - 1)

        return ans
```

**Solution 2: (String)**
```
Runtime: 24 ms
Memory Usage: N/A
```
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (sum([int(bit) for bit in bin(n)[2:]]))
```