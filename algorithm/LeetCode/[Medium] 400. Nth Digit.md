400. Nth Digit

Find the $n^{th}$ digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

**Note:**

n is positive and will fit within the range of a 32-bit signed integer (n < $2^{31}$).

**Example 1:**
```
Input:
3

Output:
3
```

**Example 2:**
```
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
```

# Submissions
---
**Solution 1: (Math)**
```
Runtime: 28 ms
Memory Usage: 12.7 MB
```
```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        s, d = 0, 0
        while s < n:
            s += (d+1)*9*10**d
            d += 1
        n -= s-d*9*10**(d-1)
        r, q = n % d, 10**(d-1) + n//d
        return str(q)[r-1] if r > 0 else str(q-1)[-1]
```

**Solution 2: (Binary Search)**
```
Runtime: 0 ms
Memory: 6.6 MB
```
```c++
class Solution {
    int noOfDigits(int x)
    {
        int count = 0;
        while(x)
        {
            count += 1;
            x /= 10;
        }
        return max(1, count);
    }
    long long int totalDigits(int n)
    {
        if(n == 0)
            return 0;
        int digNum = noOfDigits(n);
        long long int i = 1, count = 0;
        
        while(i < digNum)
        {
            count += i * (pow(10, i) - pow(10, i - 1));
            i += 1;
        }
        count += (n - pow(10, i-1) + 1) * i;
        return count;
    }
public:
    int findNthDigit(int n) {
        long long int i, r, d, x, low = 0, mid, high = n;
        while(low <= high)
        {
            mid = low + (high-low)/2;
            d = noOfDigits(mid);
            x = totalDigits(mid-1);
            
            if(x >= n)
                high = mid - 1;
            else if(n > x && n <= x + d)
            {
                n = n - x;
                break;
            }
            else
                low = mid + 1;
        }
        for(i=0;i<=d-n;i++)
        {
            r = mid % 10;
            mid /= 10;
        }
        return r;
    }
};
```
