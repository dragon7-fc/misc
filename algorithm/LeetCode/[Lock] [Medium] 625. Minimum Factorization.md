625. Minimum Factorization

Given a positive integer `num`, return the smallest positive integer `x` whose multiplication of each digit equals `num`. If there is no answer or the answer is not fit in 32-bit signed integer, return `0`.

 

**Example 1:**
```
Input: num = 48
Output: 68
```

**Example 2:**
```
Input: num = 15
Output: 35
```

**Constraints:**

* `1 <= num <= 2^31 - 1`

# Submissions
---
**Solution 1: (Greedy)**
```
Runtime: 53 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1: return 1 # edge case 
        ans, mult = 0, 1
        for x in range(9, 1, -1): 
            while num % x == 0: 
                num //= x
                ans = ans + mult * x
                mult *= 10
        return ans if num == 1 and ans < (1 << 31) else 0
```

**Solution 2: (Bucket)**
```
Runtime: 2 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int smallestFactorization(int num) {
        if(num == 1)
            return 1;
        
        vector<int> buckets(10, 0);
        for(int mod = 9; mod >= 2; mod--) {
            while(num != 1 && num%mod == 0) {
                buckets[mod]++;
                num /= mod;
            }
        }
        
        if(num != 1)
            return 0;
        
        int ans = 0;
        for(int i = 2; i < 10; i++) {
            for(int j = 0; j < buckets[i]; j++) {
                if((ans > INT_MAX/10) || (ans == INT_MAX/10 && i > 7))
                    return 0;
                ans = ans * 10 + i;
            }
        }
        return ans;
    }
};
```

**Solution 3: (Using Factorizatio)**
```
Runtime: 0 ms
Memory Usage: 37.7 MB
```
```java
class Solution {
    public int smallestFactorization(int num) {
        if (num < 2)
            return num;
        long res = 0, mul = 1;
        for (int i = 9; i >= 2; i--) {
            while (num % i == 0) {
                num /= i;
                res = mul * i + res;
                mul *= 10;
            }
        }
        return num < 2 && res <= Integer.MAX_VALUE ? (int)res : 0;
    }
}
```
