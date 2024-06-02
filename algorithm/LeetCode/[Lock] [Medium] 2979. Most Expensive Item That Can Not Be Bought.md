2979. Most Expensive Item That Can Not Be Bought

You are given two distinct prime numbers `primeOne` and `primeTwo`.

Alice and Bob are visiting a market. The market has an **infinite** number of items, for **any** positive integer x there exists an item whose price is `x`. Alice wants to buy some items from the market to gift to Bob. She has an infinite number of coins in the denomination `primeOne` and `primeTwo`. She wants to know the most expensive item she can not buy to gift to Bob.

Return the price of the **most expensive** item which Alice can not gift to Bob.

 

**Example 1:**
```
Input: primeOne = 2, primeTwo = 5
Output: 3
Explanation: The prices of items which cannot be bought are [1,3]. It can be shown that all items with a price greater than 3 can be bought using a combination of coins of denominations 2 and 5.
```

**Example 2:**
```
Input: primeOne = 5, primeTwo = 7
Output: 23
Explanation: The prices of items which cannot be bought are [1,2,3,4,6,8,9,11,13,16,18,23]. It can be shown that all items with a price greater than 23 can be bought.
```

**Constraints:**

* `1 < primeOne, primeTwo < 104`
* `primeOne, primeTwo are prime numbers.`
* `primeOne * primeTwo < 105`

# Submissions
---
**Soluti8on 1: (DP Bottom-Up)**
```
Runtime: 87 ms
Memory: 95.24 MB
```
```c++
class Solution {
public:
    int mostExpensiveItem(int primeOne, int primeTwo) {
        vector<int> dp;
        dp.push_back(1);
        int i = 1, last = 0;
        while (1) {
            dp.push_back(0);
            if (i >= primeOne) {
                dp[i] |= dp[i-primeOne];
            }
            if (i >= primeTwo) {
                dp[i] |= dp[i-primeTwo];
            }
            if (dp[i] == 0) {
                last = i;
            } else if (i >= last + primeOne || i >= last + primeTwo) {
                if (dp[i-primeOne] == 0) {
                    return i-primeOne;
                }
                return i - primeTwo;
            }
            i += 1;
        }
        return -1;
    }
};
```

**Solution 2: (Math)**
```
Runtime: 0 ms
Memory: 7.46 MB
```
```c++
class Solution {
public:
    int mostExpensiveItem(int primeOne, int primeTwo) {
        return primeOne * primeTwo - primeOne - primeTwo;
    }
};
```
