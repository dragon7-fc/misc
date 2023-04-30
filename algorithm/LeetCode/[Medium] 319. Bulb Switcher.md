319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

**Example:**
```
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
```
# Submissions
---
**Solution 1: (Brainteaser)**

There is a pattern for it  
for 1th bulb : 1  
2nd : 1 0  
3rd : 1 0 0  
4th : 1 0 0 1  
5th : 1 0 0 1 0  
6th : 1 0 0 1 0 0  
7th : 1 0 0 1 0 0 0  
8th : 1 0 0 1 0 0 0 0  
9th : 1 0 0 1 0 0 0 0 1  

Meaning the I-th bulb that is on only on when its on __I**2__ turn, for example if you want 2 bulb on then you will have to go to 4th round, 3 bulb on -> 9th round.
so for (n-th round) you can get at most floor(square_root(n)) bulb.

```
Runtime: 24 ms
Memory Usage: 12.4 MB
```
```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**.5)
```

**Solution 2: (Brainteaser)**

bulb is on at end
-> the number of this bulb must have odd factors
-> only square number has odd fctors
-> find the number of square number less than n

```
Runtime: 3 ms
Memory: 6.1 MB
```
```c++
class Solution {
public:
    int bulbSwitch(int n) {
        return sqrt(n);
    }
};
```
