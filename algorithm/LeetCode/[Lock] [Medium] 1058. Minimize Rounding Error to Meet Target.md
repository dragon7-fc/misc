1058. Minimize Rounding Error to Meet Target

Given an array of `prices [p1,p2...,pn]` and a `target`, round each price `pi` to `Roundi(pi)` so that the rounded array `[Round1(p1),Round2(p2)...,Roundn(pn)]` sums to the given target. Each operation `Roundi(pi)` could be either `Floor(pi)` or `Ceil(pi)`.

Return the string `"-1"` if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as Σ `|Roundi(pi) - (pi)|` for `i` from `1` to `n`, as a string with three places after the decimal.

 

**Example 1:**
```
Input: prices = ["0.700","2.800","4.900"], target = 8
Output: "1.000"
Explanation: 
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .
```

**Example 2:**
```
Input: prices = ["1.500","2.500","3.500"], target = 10
Output: "-1"
Explanation: 
It is impossible to meet the target.
```

**Note:**

* `1 <= prices.length <= 500`.
* Each string of prices `prices[i]` represents a real number which is between `0` and `1000` and has exactly 3 decimal places.
* `target` is between `0` and `1000000`.

# Submissions
---
**Solution 1: (DP Top-Down)**
```
Runtime: 488 ms
Memory Usage: 86.4 MB
```
```python
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        N = len(prices)

        @functools.lru_cache(None)
        def dp(i, t):
            if t < 0:
                return float('inf')
            if i == N:
                if t == 0:
                    return 0
                return float('inf')
            
            cur = float(prices[i])
            c = math.ceil(cur)
            f = math.floor(cur)
            res = min(
                cur - f + dp(i+1, t-f),
                c - cur + dp(i+1, t-c)
            )
            return res

        res = dp(0, target)
        if res == 0:
            return "0.000"
        return "{0:.3f}".format(res) if res != float('inf') else "-1"
```

**Solution 2: (Greedy)**
```
Runtime: 40 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        float_prices = [float(price) for price in prices]
        
        # 1. Compute the min rounded sum:
        rounded_sum = 0
        rounding_error = 0
        for price in float_prices:
            rounded_price = floor(price)
            
            rounded_sum += rounded_price
            rounding_error += price - rounded_price
        if rounded_sum >= target: # STOP
            return '%.3f' % rounding_error if rounded_sum == target else '-1'
        
        elif rounded_sum + len(prices) < target:
            return '-1'
        
        # 2. Replace 1 floor by ceil at a time until we reach target: choose the price with the min rounding error
        float_prices.sort(key=lambda price: ceil(price) - price) # ... Sort prices by ceil error to get the min rounding error
        for price in float_prices:
            rounded_sum += ceil(price) - floor(price) # +1 or +0
            rounding_error += (ceil(price) - price) - (price - floor(price)) # Replace the floor rounding by the ceil rounding
            
            if rounded_sum >= target:
                break
        
        return '%.3f' % rounding_error if rounded_sum == target else '-1'
```

**Solution 3: (Sort)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        if not prices:
            return "-1"
        prices = [float(p) for p in prices]
        n = len(prices)
        lower = sum([math.floor(p) for p in prices])
        upper = sum([math.ceil(p) for p in prices])
        if target < lower or target > upper:
            return "-1"
        
        numCeil = int(target - lower)
        # for int prices like 2.000 or 17.000, the ceiling op cannot + 1 on the result
        # so these entries should not be put at the beginning of sorted list
        prices = sorted(prices, key=lambda p: math.ceil(p) - p if math.ceil(p) != math.floor(p) else sys.maxsize)
        return "{0:.3f}".format(sum([math.ceil(p) - p for p in prices[:numCeil]]) +
               sum([p - math.floor(p) for p in prices[numCeil:]]))
```