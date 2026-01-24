233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

**Example:**
```
Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
```

# Solution
---
## Approach #1 Brute force [Time Limit Exceeded]
**Intuition**

Do as directed in question.

**Algorithm**

* Iterate over $i$ from $1$ to $n$:
    * Convert $i$ to string and count $\text{'1'}$ in each integer string
    * Add count of $\text{'1'}$ in each string to the sum, say $count$
    
```c++
int countDigitOne(int n)
{
    int countr = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        countr += count(str.begin(), str.end(), '1');
    }
    return countr;
}
```

**Complexity Analysis**

* Time complexity: $O(n*log_{10}(n))$.

    * We iterate from $1$ to $n$
    * In each iteration, we convert integer to string and count '1' in string which takes linear time in number of digits in $i$, which is $log_{10}(n)$.
* Space complexity: $O(log_{10}(n))$ Extra space for the `countr` and the converted string $\text{str}$.

## Approach #2 Solve it mathematically [Accepted]
**Intuition**

In Approach #1, we manually calculated the number of all the $'1'$s in the digits, but this is very slow. Hence, we need a way to find a pattern in the way $'1'$s (or for that matter any digit) appears in the numbers. We could then use the pattern to formulate the answer.

Consider the $1$s in $\text{ones}$ place , $\text{tens}$ place, $\text{hundreds}$ place and so on... An analysis has been performed in the following figure.

![233_number_of_digit_one.png](img/233_number_of_digit_one.png)

From the figure, we can see that from digit '1' at $\text{ones}$ place repeat in group of 1 after interval of $10$. Similarly, '1' at $\text{tens}$ place repeat in group of 10 after interval of $100$. This can be formulated as $(n/(i*10))*i$.

Also, notice that if the digit at $\text{tens}$ place is $\text{'1'}$, then the number of terms with $\text{'1's}$ is increased by $x+1$, if the number is say $\text{"ab1x"}$. As if digits at $\text{tens}$ place is greater than $1$, then all the $10$ occurances of numbers with $'1'$ at $\text{tens}$ place have taken place, hence, we add $10$. This is formluated as ${\min(\max((\text{n mod (i*10)} )-i+1,0),i)}$.

Lets take an example, say $n = 1234$.

No of $\text{'1'}$ in $\text{ones}$ place = $1234/10$ (corresponding to 1,11,21,...1221) + $\min(4,1)$(corresponding to 1231) = $124$

No of $\text{'1'}$ in $\text{tens}$ place = $(1234/100)*10$ (corresponding to 10,11,12,...,110,111,...1919) + $\min(21,10)$ (corresponding to 1210,1211,...1219) = $130$

No of $\text{'1'}$ in $\text{hundreds}$ place = $(1234/1000)*100$ (corresponding to 100,101,12,...,199) +$\min(135,100)$ (corresponding to 1100,1101...1199) = $200$

No of $\text{'1'}$ in $\text{thousands}$ place = $(1234/10000)*10000$ + $\min(235,1000)$(corresponding to 1000,1001,...1234)=$235$

Therefore, Total = 124+130+200+235 = 689124+130+200+235=689.

Herein, one formula has been devised, but many other formulae can be devised for faster implementations, but the essence and complexity remains the same. The users are encouraged to try to devise their own version of solution using the mathematical concepts.

**Algorithm**

* Iterate over $i$ from $1$ to $n$ incrementing by $10$ each time:

* Add $(n/(i*10))*i$ to $\text{countr}$ representing the repetition of groups of $i$ sizes after each $(i*10)$ interval.

* Add ${\min(\max((\text{n mod (i*10)} )-i+1,0),i)}$ to $\text{countr}$ representing the additional digits dependant on the digit in iith place as described in intuition.

```c++
int countDigitOne(int n)
{
    int countr = 0;
    for (long long i = 1; i <= n; i *= 10) {
        long long divider = i * 10;
        countr += (n / divider) * i + min(max(n % divider - i + 1, 0LL), i);
    }
    return countr;
}
```

**Complexity analysis**

* Time complexity: $O(log_{10}(n))$.

    * No of iterations equal to the number of digits in n which is $log_{10}(n)$

* Space complexity: $O(1)$ space required.

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        i = 1
        while i <= n:
            divider = i*10
            countr += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return countr
```

**Solution 2: (Math)**

    n =  1   3
i        1  10
divider 10 100
countr  +2  +4
```
Runtime: 0 ms Beats, 100.00%
Memory: 7.68 MB, Beats 97.02%
```
```c++
class Solution {
public:
    int countDigitOne(int n) {
        int countr = 0;
        for (long long i = 1; i <= n; i *= 10) {
            long long divider = i * 10;
            countr += (n / divider) * i + min(max(n % divider - i + 1, 0LL), i);
        }
        return countr;
    }
};
```
