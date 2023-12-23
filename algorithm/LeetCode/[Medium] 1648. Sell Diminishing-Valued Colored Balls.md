1648. Sell Diminishing-Valued Colored Balls

You have an inventory of different colored balls, and there is a customer that wants orders balls of **any** color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls **of that color** you currently have in your `inventory`. For example, if you own `6` yellow balls, the customer would pay `6` for the first yellow ball. After the transaction, there are only `5` yellow balls left, so the next yellow ball is then valued at `5` (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, `inventory`, where `inventory[i]` represents the number of balls of the `i`th color that you initially own. You are also given an integer `orders`, which represents the total number of balls that the customer wants. You can sell the balls **in any order**.

Return the **maximum** total value that you can attain after selling orders colored balls. As the answer may be too large, return it **modulo** `109 + 7`.

 

**Example 1:**

![j1648_j.gif](img/j1648_j.gif)
```
Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
```

**Example 2:**
```
Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
```

**Example 3:**
```
Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
```

**Example 4:**
```
Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
```

**Constraints:**

* `1 <= inventory.length <= 105`
* `1 <= inventory[i] <= 109`
* `1 <= orders <= min(sum(inventory[i]), 109)`

# Submissions
---
**Solution 1; (Greedy, Sort then greedy add rectangle area arithmetic sum)**
```
Runtime: 648 ms
Memory Usage: 25 MB
```
```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % 1_000_000_007
            k += 1
```

**Solution 2: (Binary Search)**
```
Runtime: 221 ms
Memory: 87.5 MB
```
```c++
class Solution {
    map<int, int, greater<>> m;
    bool valid(int M, int T) {
        for (auto &[n , cnt] : m) {
            if (n <= M) break;
            T -= (long)cnt * (n - M);
            if (T <= 0) return true;
        }
        return T <= 0;
    }
public:
    int maxProfit(vector<int>& inventory, int orders) {
        long ans = 0, mod = 1e9+7, L = 0, R = *max_element(begin(inventory), end(inventory));
        for (int n : inventory)
            m[n]++;
        while (L < R) {
            long M = (L + R) / 2;
            if (valid(M, orders)) L = M + 1;
            else R = M;
        }
        for (auto &[n , cnt] : m) {
            if (n <= L) break;
            orders -= cnt * (n - L);
            ans = (ans + (n + L + 1) * (n - L) / 2 % mod * cnt % mod) % mod;
        }
        if (orders) ans = (ans + L * orders % mod) % mod;
        return ans;
    }
};
```
