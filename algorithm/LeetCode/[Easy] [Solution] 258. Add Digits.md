258. Add Digits

Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit.

**Example:**
```
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
```

**Follow up:**

Could you do it without any loop/recursion in O(1) runtime?

# Solution
--
## Overview
The value we're asked to compute is the so-called Digital Root. Logarithmic time solution is easy to write, although the main question here is how to fit into a constant time.

```python
class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
                
        return digital_root
```

## Approach 1: Mathematical: Digital Root
Formula for the Digital Root

There is a known formula to compute a digital root in a decimal numeral system

$dr_{10}(n) = 0, \qquad \text{if } n = 0$

$dr_{10}(n) = 9, \qquad \text{if } n = 9 k$

$dr_{10}(n) = n \mod 9, \qquad \text{if } n \ne 9 k$

How to derive it? Probably, you already know the following proof from school, where it was used for a divisibility by 9: "The original number is divisible by 9 if and only if the sum of its digits is divisible by 9". Let's revise it briefly.

The input number could be presented in a standard way, where $d_0, d_1, .. d_k$ are digits of n:

$n = d_0 + d_1 \cdot 10^1 + d_2 \cdot 10^2 + ... + d_k \cdot 10^k$
 

One could expand each power of ten, using the following:

$10 = 9 \cdot 1 + 1 \\ 100 = 99 + 1 = 9 \cdot 11 + 1 \\ 1000 = 999 + 1 = 9 \cdot 111 + 1 \\ ... \\ 10^k = 1\underbrace{00..0}_\text{k times} = \underbrace{99..9}_\text{k times} + 1 = 9 \cdot \underbrace{11..1}_\text{k times} + 1$

That results in

$n = d_0 + d_1 \cdot (9 \cdot 1 + 1) + d_2 \cdot(9 \cdot 11 + 1) + ... + d_k \cdot (9 \cdot \underbrace{11..1}_\text{k times} + 1)$

and could be simplified as

$n = (d_0 + d_1 + d_2 + ... + d_k) + 9 \cdot (d_1 \cdot 1 + d_2 \cdot 11 + ... + d_k \cdot \underbrace{11..1}_\text{k times})$

The last step is to take the modulo from both sides:

$n \mod 9 = (d_0 + d_1 + d_2 + ... + d_k) \mod 9$

and to consider separately three cases: the sum of digits is 0, the sum of digits is divisible by 9, and the sum of digits is not divisible by nine:

$dr_{10}(n) = 0, \qquad \text{if } n = 0$

$dr_{10}(n) = 9, \qquad \text{if } n = 9 k$

$dr_{10}(n) = n \mod 9, \qquad \text{if } n \ne 9 k$

Implementation

The straightforward implementation is

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
```

though two last cases could be merged into one

$dr_{10}(n) = 0, \qquad \text{if } n = 0$

$dr_{10}(n) = 1 + (n - 1) \mod 9, \qquad \text{if } n \ne 0$

```python
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(1)$.

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Mathematical: Digital Root)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
```

**Solution 2: (Math, DFS)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def addDigits(self, num: int) -> int:
        def dfs(num):
            digits = [int(d) for d in str(num)]
            if len(digits) == 1:
                return digits[0]
            return dfs(str(sum(digits)))
        Runtime: 0 ms
Memory Usage: 5.8 MB
        return dfs(num)
```

**Solution 3: (DFS)**
```
Runtime: 0 ms
Memory Usage: 5.8 MB
```
```c++
class Solution {
public:
    int addDigits(int num) {
        int sum=0;
        while(num)
        {
            sum+=(num%10);
            num/=10;
        }
        if(sum<10)
            return sum;
        else
            return addDigits(sum);
    }
};
```

**Solution 3: (Math)**
```
Runtime: 0 ms
Memory: 5.9 MB
```
```c++
class Solution {
public:
    int addDigits(int num) {
        int cur;
        while (num >= 10) {
            cur = 0;
            while (num > 0) {
                cur += num%10;
                num /= 10;
            }
            num = cur;
        }
        return num;
    }
};
```
