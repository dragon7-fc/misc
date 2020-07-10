793. Preimage Size of Factorial Zeroes Function

Let `f(x)` be the number of zeroes at the end of `x!`. (Recall that `x! = 1 * 2 * 3 * ... * x`, and by convention, `0! = 1`.)

For example, `f(3) = 0` because 3! = 6 has no zeroes at the end, while `f(11) = 2` because 11! = 39916800 has 2 zeroes at the end. Given `K`, find how many non-negative integers `x` have the property that `f(x) = K`.

**Example 1:**
```
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
```

**Example 2:**
```
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
```

**Note:**

* `K` will be an integer in the range `[0, 10^9]`.

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 0 ms
Memory Usage: 5.9 MB
```
```c++
class Solution {
public:
    long int counter(long long int n) // function to count trailing zeroes in n!
    {
        long int c=0;
        while(n)
        {
            c+=(n/5);
            n/=5;
        }
        return c;
    }
    int preimageSizeFZF(int K) {
        // the output is either 5 or 0
        // i.e. the count of trailing zeroes changes per 5 numbers
        long long int low,high,mid,c;
        low=0;
        high=1000000000;
        
        if(K==low || K==high) // two base cases
            return 5;
        
        while(low<=high)
        {
            mid=low+(high-low)/2;
            c = counter(mid);
            if(K==c)   // a number with same no of trailing zeroes is found
                return 5;
            else if(K < c)
                high=mid-1;
            else
                low=mid+1;
        }
        
        return 0;    
    }
};
```

**Solution 2: (Binary Search)**
```
Runtime: 40 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        
        def count(num):
            cnt = 0
            while num:
                cnt += num // 5
                num //= 5
            return cnt
        
        l, r = 0, 2 ** 63 - 1
        while l < r:
            mid = (l + r) // 2
            if count(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - l % 5 if count(l) == K else 0
```