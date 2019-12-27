638. Shopping Offers

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for **exactly** certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

**Example 1:**
```
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
```

**Example 2:**
```
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
```

**Note:**

* There are at most 6 kinds of items, 100 special offers.
* For each item, you need to buy at most 6 of them.
* You are **not** allowed to buy more items than you want, even if that would lower the overall price.

# Solution
---
## Approach #1 Using Recursion [Accepted]
**Algorithm**

Before discussing the steps involved in the process, we need to note a few points. Firstly, whenever an offer is used from amongst the ones available in the $special$ list, we need to update the $needs$ appropriately, such that the number of items in the current offer of each type are deducted from the ones in the corresponding entry in $needs$.

Further, an offer can be used only if the number of items, of each type, required for using the offer, is lesser than or equal to the ones available in the current $needs$.

Now, let's discuss the algorithm. We make use of a `shopping(price,special,needs)` function, which takes the $price$ and $special$ list along with the current(updated) $needs$ as the input and returns the minimum cost of buying these items as required by this $needs$ list.

In every call of the function `shopping(price,special,needs)`, we do as follows:

1. Determine the cost of buying items as per the $needs$ array, without applying any offer. Store the result in resres.

2. Iterate over every offer in the $special$ list. For every offer chosen, repeat steps 3 to 5.

3. Create a copy of the current $needs$ in a $clone$ list(so that the original needs can be used again, while selecting the next offer).

4. Try to apply the current offer. If possible, update the required number of items in $clone$.

5. If the current offer could be applied, find the minimum cost out of $res$ and `offer_current + shopping(price,special,clone)`. Here, `offer_current` refers to the price that needs to be paid for the current offer. Update the $res$ with the minimum value.

6. Return the $res$ corresponding to the minimum cost.

We need to note that the $clone$ needs to be updated afresh from needsneeds(coming to the current function call) when we choose a new offer. This needs to be done, because solely applying the next offer could result in a lesser cost than the one resulting by using the previous offer first.

```java
public class Solution {
    public int shoppingOffers(List < Integer > price, List < List < Integer >> special, List < Integer > needs) {
        return shopping(price, special, needs);
    }
    public int shopping(List < Integer > price, List < List < Integer >> special, List < Integer > needs) {
        int j = 0, res = dot(needs, price);
        for (List < Integer > s: special) {
            ArrayList < Integer > clone = new ArrayList < > (needs);
            for (j = 0; j < needs.size(); j++) {
                int diff = clone.get(j) - s.get(j);
                if (diff < 0)
                    break;
                clone.set(j, diff);
            }
            if (j == needs.size())
                res = Math.min(res, s.get(j) + shopping(price, special, clone));
        }
        return res;
    }
    public int dot(List < Integer > a, List < Integer > b) {
        int sum = 0;
        for (int i = 0; i < a.size(); i++) {
            sum += a.get(i) * b.get(i);
        }
        return sum;
    }

}
```

## Approach #2 Using Recursion with memoization [Accepted]
**Algorithm**

In the last approach, we can observe that the same $needs$ can be reached by applying the offers in various orders. e.g. We can choose the first offer followed by the second offer or vice-versa. But, both lead to the same requirement of updated $needs$ and the cost as well. Thus, instead of repeating the whole process for the same $needs$ state through various recursive paths, we can create an entry corresponding to the current set of $needs$ in a HashMap, $map$, which stores the minimum cost corresponding to this set of $needs$. Thus, whenever the same call is made again in the future through a different path, we need not repeat the whole process over, and we can directly return the result stored in the $map$.

```java
public class Solution {
    public int shoppingOffers(List < Integer > price, List < List < Integer >> special, List < Integer > needs) {
        Map < List < Integer > , Integer > map = new HashMap();
        return shopping(price, special, needs, map);
    }
    public int shopping(List < Integer > price, List < List < Integer >> special, List < Integer > needs, Map < List < Integer > , Integer > map) {
        if (map.containsKey(needs))
            return map.get(needs);
        int j = 0, res = dot(needs, price);
        for (List < Integer > s: special) {
            ArrayList < Integer > clone = new ArrayList < > (needs);
            for (j = 0; j < needs.size(); j++) {
                int diff = clone.get(j) - s.get(j);
                if (diff < 0)
                    break;
                clone.set(j, diff);
            }
            if (j == needs.size())
                res = Math.min(res, s.get(j) + shopping(price, special, clone, map));
        }
        map.put(needs, res);
        return res;
    }
    public int dot(List < Integer > a, List < Integer > b) {
        int sum = 0;
        for (int i = 0; i < a.size(); i++) {
            sum += a.get(i) * b.get(i);
        }
        return sum;
    }

}
```

# Submissions
---
**Solution 1:**
```
Runtime: 104 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(price, special, needs, memo):
            if memo[tuple(needs)]:
                return memo[tuple(needs)]
            j = 0
            res = dot(needs, price)
            for s in special:
                clone = needs.copy()
                for j in range(len(needs)):
                    diff = clone[j] - s[j]
                    if diff < 0:
                        break
                    clone[j] = diff
                    if j == len(needs)-1:
                        res = min(res, s[j+1] + shopping(price, special, clone, memo))
            memo[tuple(needs)] = res
            return res

        def dot(a, b):
            sum_ = 0;
            for i in range(len(a)):
                sum_ += a[i] * b[i]
            return sum_
        
        memo = collections.defaultdict(int)
        return shopping(price, special, needs, memo)
```