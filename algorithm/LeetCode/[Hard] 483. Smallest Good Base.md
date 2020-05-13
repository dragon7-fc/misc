483. Smallest Good Base

For an integer n, we call k>=2 a **good base** of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

**Example 1:**
```
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
```

**Example 2:**
```
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
```

**Example 3:**
```
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
```

**Note:**

* The range of n is `[3, 10^18]`.
* The string representing n is always valid and will not have leading zeros.

# Submissions
---
**Solution 1: (Math)**

Well, this is the standard solution, so you'll see it in many places ... It's short and fast, but how does it work?

Let's do baby steps.

What is 111 in base 2?

that is 1x2^0 + 1x2^1 + 1x2^2 = 1x1 + 1x2 + 1x4 = 1 + 2 + 4 = 7

what is 111 in base 5?

that is 1x5^0 + 1x5^1 + 1x5^2 = 1x1 + 1x5 + 1x25 = 1 + 5 + 25 = 31

Guess what ... this is a classic geometric sequence. Check out Wikipedia under Geometric progression.

Good news - there is a very simple formula to calculate the total:

if our base is r and the starting element is 1, the sum (in our case it's n):

n = (1 - k^m)/(1 - k)

Here n is our number n, k is the base and m is the number of digits in the string representing n in base k

This is the key part, once you get comfortable with that, the rest is more or less easy.

Ok, so if you look at that formula, we only know n, we need to find k, but we also don't know m. Since we have 2 variables and one equasion, we can't calculate k analytically, but since the number of digits can't be too long, we can simply try a range of possible bases.

So how can we determine the range? Let's see ... the smaller the base, the longer the number representation - that is obvious if you remember how numbers look in hex (base 16, shorter than in decimal) vs in binary format (base 2, much longer!). That means if we got number n, the longest possible string to represent it would be with base 2. And the way to calculate the number of digits is log(n,2). (so if k=log(n,2), that means n = 2 ^ k, so that tells us the highest number we can represent with that many digits)

We can quickly calculate that number using:

        m_max = int(math.log(n, 2))
Ok, so far so good. Now we can go back to the formula:

n = (1 - k^m)/(1 - k)

we know the number n and that m is in the range from 1 to m_max.

How can we find k? Now we are going to do the following trick.

Since k is the base, it's going to be an integer. So the idea is we get an estimate using non-exact calculation and then we verify if that k works or not using a percise verification formula.

If you look at

n = (1 - k^m)/(1 - k)

Once k and m become large numbers, we can ignore them and then n ~ k^m/k, so we can use k = int(n**(1/m)) as an approximate value for k. Now, this is important. Remember, we said "once k and m become large numbers"? This estmate works better for the large numbers than for the small ones. So when we'll run our loop, we'll go from the large values of m down.

Ok, so once we have an estimated k, we simply plug it into the formula above and verify. Here is another tip. That formula has division in it. Division makes things complicated. First, now we are going to be using floats in addition to ints. Second, comparing int and float is hard. So we can simply stay with int numbers only by changing that formula to:

`if (k**m - 1 ) == n*(k - 1)`

Ok, now we got the final catch. Remember k = int(n**(1/m)) ? There is another problem with division. We can't divide by zero. So we need to exclude that.

Finally, if nothing else works, any number can be presented as 11 using base n-1. For example, 3 is 11 base 2, 11 is 11 base 10, 17 is 11 base 16 etc. ( more formally n = 1x(n-1)^1+1x(n-1)^0 = 1x(n-1) + 1x1 = n -1 + 1 = n)

Great, now we just need to put all pieces together:
```python
    def smallestGoodBase(self, n: 'str') -> 'str':
        n = int(n) # <- thanks to Python's unlmited int size, we can simply convert the input string into int.
        m_max = int(math.log(n, 2)) # <- here we estimate the max number of digits we would need.
        
        for m in range(m_max, 1, -1): # <- we are going to check if we can form the number n with that many digits ...
            k = int(n**(1/m)) # <- estimating the base by rounding the float to an int
            if (k**(m+1) - 1)  == n*(k-1): # <- and here we are verifying accurately if that base would work
                return str(k) # <- return if yes
        return str(n-1)  # <- if nothing else worked, we can always represent as 11 in base (n-1)
```
Yes! It works really well with performance above 97%.

```
Runtime: 32 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))
        
        for m in range(m_max, 1, -1):
            k = int(n**(1/m))
            if (k**(m+1) - 1)  == n*(k-1):
                return str(k)
        return str(n-1)   
```