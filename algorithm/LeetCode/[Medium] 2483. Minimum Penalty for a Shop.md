2483. Minimum Penalty for a Shop

You are given the customer visit log of a shop represented by a `0-indexed` string customers consisting only of characters `'N'` and `'Y'`:

* if the `i`th character is `'Y'`, it means that customers come at the `i`th hour
* whereas `'N'` indicates that no customers come at the `i`th hour.

If the shop closes at the `j`th hour `(0 <= j <= n)`, the penalty is calculated as follows:

* For every hour when the shop is open and no customers come, the penalty increases by `1`.
* For every hour when the shop is closed and customers come, the penalty increases by `1`.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the `j`th hour, it means the shop is closed at the hour `j`.

 

**Example 1:**
```
Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
```

**Example 2:**
```
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
```

**Example 3:**
```
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
```

**Constraints:**

* `1 <= customers.length <= 10^5`
* `customers` consists only of characters `'Y'` and `'N'`.

# Submissions
---
**Solution 1: (Two Pass)**
```
Runtime: 109 ms
Memory: 14.9 MB
```
```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = customers.count('Y')
        if penalty == n: 
            return n
        min_, ans = n, 0
        for index, value in enumerate(customers):
            if min_ > penalty:
                min_ = penalty
                ans = index
            if value == 'Y':
                penalty -= 1
            else:
                penalty += 1
        if min_ > penalty: return n
        return ans
```

**Solution 2: (Two Pass)**
```
Runtime: 26 ms
Memory: 10.7 MB
```
```c++
class Solution {
public:
    int bestClosingTime(string customers) {
        int cur = count(begin(customers), end(customers), 'Y'), mn = cur, ans = 0;
        for (int i = 0; i < customers.size(); ++i) {
            cur += customers[i] == 'Y' ? -1 : 1;
            if (cur < mn) {
                mn = cur;
                ans = i + 1;
            }
        }
        return ans;
    }
};
```

