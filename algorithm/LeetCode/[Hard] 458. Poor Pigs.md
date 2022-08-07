458. Poor Pigs

There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.

 

**General case:**

If there are `n` buckets and a pig drinking poison will die within `m` minutes, how many pigs (`x`) you need to figure out the poisonous bucket within `p` minutes? There is exactly one bucket with poison.

 

**Note:**

* A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
* After a pig has instantly finished drinking buckets, there has to be a **cool down time** of m minutes. During this time, only observation is allowed and no feedings at all.
* Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).

**Hint 1:**

What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.

**Hint 2:**

How many states can we generate with x pigs and T tests?

**Hint 3:**

Find minimum `x` such that `(T+1)^x >= N`


# Submissions
---
**Solution 1: (Math, (rounds+1)\*\*x >= n)**

If there are only 2 rounds of tests,
Then for each bucket, a pig can have 3 choices:

* Drink it on 1st round
* Drink it on 2nd round
* Not drink it.

Every pig has the above 3 choices, for n pigs, the total number of combinations is 3^n
If we apply the first of such combinations to the first bucket, the second combination to the 2nd bucket, ..., the last combination to the last bucket, then when pig dies, the combination of dead pigs can only correspond to one bucket because each bucket has different pig combinations, therefore we can 100% find this poison bucket.
So the max number of testable bucket for "n" pigs should be:
(test rounds+1)^n

We keep increasing number of pigs from 0 ~ n and check what is the max testable bucket these pigs can make, until the max bucket numbe is biggers then the provided bucket.

```
Runtime: 32 ms
Memory Usage: 13.7 MB
```
```python
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs, rounds = 0, minutesToTest//minutesToDie
        while (rounds+1)**pigs < buckets:
            pigs += 1
            
        return pigs
```

**Solution 2: (Math, (rounds+1)\*\*x >= n)**
```
Runtime: 24 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest//minutesToDie
        return math.ceil(math.log(buckets, T+1))
```

**Solution 3: (Math)**
```
Runtime: 0 ms
Memory Usage: 6.1 MB
```
```c++
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        return ceil(log(buckets) / log(minutesToTest / minutesToDie + 1));
    }
};
```
