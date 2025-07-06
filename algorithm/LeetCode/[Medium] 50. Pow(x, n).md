50. Pow(x, n)

Implement `pow(x, n)`, which calculates x raised to the power `n` ($x^{n}$).

**Example 1:**
```
Input: 2.00000, 10
Output: 1024.00000
```

**Example 2:**
```
Input: 2.10000, 3
Output: 9.26100
```

**Example 3:**
```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Note:**

* `-100.0 < x < 100.0`
* n is a 32-bit signed integer, within the range $[−2^{31}, 2^{31} − 1]$

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        
        ans = 1
        while n > 0:
            if n % 2 == 1: # current exponent is odd
                ans = ans * x
                x = x * x
                n = (n-1) / 2
            else: # current exponent is even
                x = x * x
                n = n / 2

        return ans
```

**Solution 2: (Math, DFS)**
```
Runtime: 28 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        if n%2 == 1:
            ans = x * self.myPow(x*x, (n-1)/2)
        else:
            ans = self.myPow(x*x, n/2)

        return ans
```

**Solution 3: (Math, DFS)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0)
             return 1;
        double t = myPow(x, n/2);
        if (n%2)
            return n < 0 ? 1/x*t*t: x*t*t; 
        else
            return t*t;
    }
};
```

**Solution 4: (Math, DFS)**
```
Runtime: 5 ms
Memory Usage: 5.6 MB
```
```c
double myPow(double x, int n){
    // divide and conquer
    long N = n;
    if (N == 0)
    {
        return 1.0;
    }
    if (N == 1)
    {
        return x;
    }
    if (N < 0)
    {
        N = -N;
        x = 1 / x;
    }
    
    if (N % 2 == 0)
    {
        double power = myPow(x, N / 2);
        return power * power;
    }
    else
    {
        return myPow(x, N / 2) * myPow(x, N - N / 2);
    }
}
```

**Solution 5: (Math, DFS)**
```
Runtime: 0 ms
Memory: 6 MB
```
```c++
class Solution {
public:
    double myPow(double x, int n) {
        if (n==0) return 1;
        if (n<0) {
            n = abs(n);
            x = 1/x;
        }
        if(n%2 == 0){
            return myPow(x*x, n/2);
        }
        else{
            return x*myPow(x, n-1);
        }
    }
};
```

**Solution 6: (Math, shift right)**
```
Runtime: 0 ms
Memory: 5.9 MB
```
```c++
class Solution {
public:
    double myPow(double x, int n) {
        double ans = 1;
        long long m = n;
        if(n < 0){
            m = (-1) * m;
        }
        while(m > 0){
            if(m % 2 == 1){
                ans = ans * x;
                m = m -1;
            }
            else{
                x = x*x;
                m = m/2;
            }
        }
        if(n < 0){
            ans = 1/ans;
        }
        return ans;
    }
};
```

**Solution 7: (Math)**

1010    = 10
  2^2
2^8
2^8 * 2^4

b   0 1  2    3
a   2 4 16  256
ans 1 4    1024

```
Runtime: 0 ms, Beats 100.00%
Memory: 8.73 MB, Beats 13.04%
```
```c++
class Solution {
public:
    double myPow(double x, int n) {
        if (x == 1 || n == 0) {
            return 1;
        }
        double a = x, ans = 1;
        long long b = 0, cn = n;
        if (cn < 0) {
            a = 1/x;
            cn *= -1;
        }
        while ((1LL<<b) <= cn) {
            if ((1<<b) & cn) {
                ans *= a;
            }
            b += 1;
            a *= a;
        }
        return ans;
    }
};
```
