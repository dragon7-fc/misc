470. Implement Rand10() Using Rand7()

Given a function `rand7` which generates a uniform random integer in the range 1 to 7, write a function `rand10` which generates a uniform random integer in the range 1 to 10.

Do NOT use system's `Math.random()`.

 

**Example 1:**
```
Input: 1
Output: [7]
```

**Example 2:**
```
Input: 2
Output: [8,4]
```

**Example 3:**
```
Input: 3
Output: [8,1,10]
```

**Note:**

* `rand7` is predefined.
* Each testcase has one argument: n, the number of times that rand10 is called.

# Solution
---
## Approach 1: Rejection Sampling
**Intuition**

What if you could generate a random integer in the range 1 to 49? How would you generate a random integer in the range of 1 to 10? What would you do if the generated number is in the desired range? What if it is not?

**Algorithm**

This solution is based upon Rejection Sampling. The main idea is when you generate a number in the desired range, output that number immediately. If the number is out of the desired range, reject it and re-sample again. As each number in the desired range has the same probability of being chosen, a uniform distribution is produced.

Obviously, we have to run rand7() function at least twice, as there are not enough numbers in the range of 1 to 10. By running rand7() twice, we can get integers from 1 to 49 uniformly. Why?

![470_rejectionSamplingTable.png](img/470_rejectionSamplingTable.png)

A table is used to illustrate the concept of rejection sampling. Calling rand7() twice will get us row and column index that corresponds to a unique position in the table above. Imagine that you are choosing a number randomly from the table above. If you hit a number, you return that number immediately. If you hit a * , you repeat the process again until you hit a number.

Since 49 is not a multiple of 10, we have to use rejection sampling. Our desired range is integers from 1 to 40, which we can return the answer immediately. If not (the integer falls between 41 to 49), we reject it and repeat the whole process again.

**C++**
```c++
class Solution {
public:
    int rand10() {
        int row, col, idx;
        do {
            row = rand7();
            col = rand7();
            idx = col + (row - 1) * 7;
        } while (idx > 40);
        return 1 + (idx - 1) % 10;
    }
};
```

**Java**
```java
class Solution extends SolBase {
    public int rand10() {
        int row, col, idx;
        do {
            row = rand7();
            col = rand7();
            idx = col + (row - 1) * 7;
        } while (idx > 40);
        return 1 + (idx - 1) % 10;
    }
}
```

**Complexity Analysis**

* Time Complexity: $O(1)$ average, but $O(\infty)$ worst case.
The expected value for the number of calls to `rand7()` can be computed as follows:

$\begin{align} E\left( \text{# calls to rand7} \right) = \ & 2 \cdot \frac{40}{49} + \\ & 4 \cdot \frac{9}{49} \cdot \frac{40}{49} + \\ & 6 \cdot \left(\frac{9}{49}\right)^2 \cdot \frac{40}{49} + \\ \ \\ & ...\\ \ \\ =\ & \sum_{k=1}^{\infty} \left(\frac{9}{49}\right)^{k-1} \cdot \frac{40}{49} \\ =\ & \frac{80}{49 \cdot \left(1 - \dfrac{9}{49}\right)^2} \\ \ \\ =\ & 2.45 \end{align}$

* Space Complexity: $O(1)$.

## Approach 2: Utilizing out-of-range samples
**Intuition**

There are a total of 2.45 calls to rand7() on average when using approach 1. Can we do better? Glad that you asked. In fact, we are able to improve average number of calls to rand7() by about 10%.

The idea is that we should not throw away the out-of-range samples, but instead use them to increase our chances of finding an in-range sample on the successive call to rand7.

**Algorithm**

Start by generating a random integer in the range 1 to 49 using the aforementioned method. In the event that we could not generate a number in the desired range (1 to 40), it is equally likely that each number of 41 to 49 would be chosen. In other words, we are able to obtain integers in the range of 1 to 9 uniformly. Now, run rand7() again to obtain integers in the range of 1 to 63 uniformly. Apply rejection sampling where the desired range is 1 to 60. If the generated number is in the desired range (1 to 60), we return the number. If it is not (61 to 63), we at least obtain integers of 1 to 3 uniformly. Run rand7() again to obtain integers in the range of 1 to 21 uniformly. The desired range is 1 to 20, and in the unlikely event we get a 21, we reject it and repeat the entire process again.

**C++**
```c++
class Solution {
public:
    int rand10() {
        int a, b, idx;
        while (true) {
            a = rand7();
            b = rand7();
            idx = b + (a - 1) * 7;
            if (idx <= 40)
                return 1 + (idx - 1) % 10;
            a = idx - 40;
            b = rand7();
            // get uniform dist from 1 - 63
            idx = b + (a - 1) * 7;
            if (idx <= 60)
                return 1 + (idx - 1) % 10;
            a = idx - 60;
            b = rand7();
            // get uniform dist from 1 - 21
            idx = b + (a - 1) * 7;
            if (idx <= 20)
                return 1 + (idx - 1) % 10;
        }
    }
};
```

**Java**
```java
class Solution extends SolBase {
    public int rand10() {
        int a, b, idx;
        while (true) {
            a = rand7();
            b = rand7();
            idx = b + (a - 1) * 7;
            if (idx <= 40)
                return 1 + (idx - 1) % 10;
            a = idx - 40;
            b = rand7();
            // get uniform dist from 1 - 63
            idx = b + (a - 1) * 7;
            if (idx <= 60)
                return 1 + (idx - 1) % 10;
            a = idx - 60;
            b = rand7();
            // get uniform dist from 1 - 21
            idx = b + (a - 1) * 7;
            if (idx <= 20)
                return 1 + (idx - 1) % 10;
        }
    }
}
```

**Complexity Analysis**

* Time Complexity: $O(1)$ average, but $O(\infty)$ worst case.
The expected value for the number of calls to `rand7()` can be computed as follows (with some steps omitted due to tediousness):

$\begin{align} E\left( \text{# calls to rand7} \right) =\,& 2 \cdot \frac{40}{49} + \\ &3 \cdot \frac{9}{49} \cdot \frac{60}{63} + \\ &4 \cdot \frac{9}{49} \cdot \frac{3}{63} \cdot \frac{20}{21} + \\ \\ &\left(\frac{9}{49} \cdot \frac{3}{63} \cdot \frac{1}{21}\right) \times \\ & \left( 6 \cdot \frac{40}{49} + \right. \\ & \ \ \ 7 \cdot \frac{9}{49} \cdot \frac{60}{63} + \\ & \left. \ \ \ 8 \cdot \frac{9}{49} \cdot \frac{3}{63} \cdot \frac{20}{21} \right) + \\ \\ &\left(\frac{9}{49} \cdot \frac{3}{63} \cdot \frac{1}{21}\right)^2 \times \\ &\left( 10 \cdot \frac{40}{49} + \right. \\ & \ \ \ 11 \cdot \frac{9}{49} \cdot \frac{60}{63} + \\ & \left. \ \ \ 12 \cdot \frac{9}{49} \cdot \frac{3}{63} \cdot \frac{20}{21} \right) + \\ \\ &\ldots \\ \\ =\,& 2.2123 \end{align}$

* Space Complexity: $O(1)$.

# Submissions
---
**Solution 1: (Rejection Sampling, round7() as row / column index)**
```
Runtime: 356 ms
Memory Usage: 15.6 MB
```
```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col, idx = 0, 0, 0
        while True:
            row = rand7();
            col = rand7();
            idx = col + (row - 1) * 7;
            if idx <= 40: 
                break
                
        return 1 + (idx - 1) % 10
```

**Solution 2: (Utilizing out-of-range samples)**
```
Runtime: 336 ms
Memory Usage: 15.5 MB
```
```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a, b, idx = 0, 0, 0
        while True:
            a = rand7()
            b = rand7()
            idx = b + (a - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10
            a = idx - 40
            b = rand7()
            # get uniform dist from 1 - 63
            idx = b + (a - 1) * 7
            if idx <= 60:
                return 1 + (idx - 1) % 10
            a = idx - 60
            b = rand7()
            # get uniform dist from 1 - 21
            idx = b + (a - 1) * 7
            if idx <= 20:
                return 1 + (idx - 1) % 10
```