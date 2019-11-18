7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
```
Input: 123
Output: 321
```

**Example 2:**
```
Input: -123
Output: -321
```

**Example 3:**
```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: $[−2^{31},  2^{31} − 1]$. For the purpose of this problem, assume that your function returns `0` when the reversed integer overflows.

# Solution
---
## Approach 1: Pop and Push Digits & Check before Overflow
**Intuition**

We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.

**Algorithm**

Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of $x$ and "push" it to the back of the $\text{rev}$. In the end, $\text{rev}$ will be the reverse of the $x$.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.
```
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```
However, this approach is dangerous, because the statement $\text{temp} = \text{rev} \cdot 10 + \text{pop}$ can cause overflow.

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.

To explain, lets assume that $\text{rev}$ is positive.

If $temp = \text{rev} \cdot 10 + \text{pop}$ causes overflow, then it must be that $\text{rev} \geq \frac{INTMAX}{10}$
 
If $\text{rev} > \frac{INTMAX}{10}$, then $temp = \text{rev} \cdot 10 + \text{pop}$ is guaranteed to overflow.
If $\text{rev} == \frac{INTMAX}{10}$, then $temp = \text{rev} \cdot 10 + \text{pop}$ will overflow if and only if $\text{pop} > 7$
Similar logic can be applied when $\text{rev}$ is negative.

```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}
```

**Complexity Analysis**

* Time Complexity: $O(\log(x))$. There are roughly $\log_{10}(x)$ digits in $x$.
* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1:**
```
Runtime: 56 ms
Memory Usage: N/A
```
```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        x_abs = abs(x)
        while x_abs:
            y *= 10
            y = y + x_abs%10
            x_abs = int(x_abs/10)
        
        if y >= 2**31 - 1:
            return 0
        elif x < 0:
            return -y
        else:
            return y
```

**Solution 2:**
```
Runtime: 20 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
```