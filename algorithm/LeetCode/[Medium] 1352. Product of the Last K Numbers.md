1352. Product of the Last K Numbers

Implement the class `ProductOfNumbers` that supports two methods:

1. `add(int num)`

Adds the number `num` to the back of the current list of numbers.

2. `getProduct(int k)`

Returns the product of the last `k` numbers in the current list.
You can assume that always the current list has at least `k` numbers.
At any time, the product of any contiguous sequence of numbers will fit into a single `32`-bit integer without overflowing.

 

**Example:**
```
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
```

**Constraints:**

* There will be at most `40000` operations considering both `add` and `getProduct`.
* `0 <= num <= 100`
* `1 <= k <= 40000`

# Submissions
---
**Solution 1: (Prefix Sum)**
```
Runtime: 284 ms
Memory Usage: 28 MB
```
```python
import functools
class ProductOfNumbers:

    def __init__(self):
        # Store preProduct of all numbers
        self.products = [1]

    def add(self, num: int) -> None:
        # Calculate product if the current number is not 0
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If 0 is present in the last k numbers, return 0, else return product
        if len(self.products) - 1 >= k:
            return self.products[-1] // self.products[len(self.products) - 1 - k]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

**Solution 2: (Prefix Sum)**
```
Runtime: 11 ms, Beats 94.59%
Memory: 77.94 MB, Beats 77.84%
```
```c++
class ProductOfNumbers {
    int sz = 0;
    vector<int> dp;
public:
    ProductOfNumbers() {
        dp.push_back(1);
    }
    
    void add(int num) {
        if (num) {
            dp.push_back(dp.back()*num);
            sz += 1;
        } else {
            dp = {1};
            sz = 0;
        }
    }
    
    int getProduct(int k) {
        if (sz < k) {
            return 0;
        }
        return dp.back()/dp[sz - k];
    }
};
```
