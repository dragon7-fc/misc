605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

**Example 1:**
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```

**Example 2:**
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

**Note:**
1. The input array won't violate no-adjacent-flowers rule.
1. The input array size is in the range of [1, 20000].
1. **n** is a non-negative integer which won't exceed the input array size.

# Solution
---
## Approach #1 Single Scan [Accepted]
The solution is very simple. We can find out the extra maximum number of flowers, $count$, that can be planted for the given $flowerbed$ arrangement. To do so, we can traverse over all the elements of the $flowerbed$ and find out those elements which are 0(implying an empty position). For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next adjacent positions respectively.

If the $count$ obtained is greater than or equal to $n$, the required number of flowers to be planted, we can plant $n$ flowers in the empty spaces, otherwise not.

```java
public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0, count = 0;
        while (i < flowerbed.length) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                count++;
            }
            i++;
        }
        return count >= n;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. A single scan of the $flowerbed$ array of size $n$ is done.

* Space complexity : $O(1)$. Constant extra space is used.

## Approach #2 Optimized [Accepted]
**Algorithm**

Instead of finding the maximum value of $count$ that can be obtained, as done in the last approach, we can stop the process of checking the positions for planting the flowers as soon as $count$ becomes equal to $n$. Doing this leads to an optimization of the first approach. If $count$ never becomes equal to $n$, $n$ flowers can't be planted at the empty positions.

```java

public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0, count = 0;
        while (i < flowerbed.length) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i++] = 1;
                count++;
            }
             if(count>=n)
                return true;
            i++;
        }
        return false;
    }
}
```

**Complexity Analysis**

* Time complexity : $O(n)$. A single scan of the $flowerbed$ array of size $n$ is done.

* Space complexity : $O(1)$. Constant extra space is used.

# Submissions
---
**Solution 1: (Optimized)**
```
Runtime: 200 ms
Memory Usage: 14.1 MB
```
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                i += 1
                count += 1
            
            if count >=n:
                return True
            i += 1
        
        return False
```


**Solution 2: (Greedy, Mask)**
```
Runtime: 188 ms
Memory Usage: 12.8 MB
```
```python
Runtime: 188 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp =[0] + flowerbed +[0]
    
        index = 1 

        while index< len(tmp)-1:
            if tmp[index-1]== 0 and tmp[index]==0 and tmp[index+1]==0:
                n -= 1
                index += 1 
            index += 1
        return n <= 0
```

**Solution 3: (Greedy, Mask)**
```
Runtime: 12 ms
Memory: 20.2 MB
```
```c++
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) {
            return true;
        }
        for (int i = 0; i < flowerbed.size(); i ++) {
            if (!flowerbed[i] && (i == 0 || !flowerbed[i-1]) && (i == flowerbed.size()-1 || !flowerbed[i+1])) {
                flowerbed[i] = 1;
                n -= 1;
                if (!n) {
                    break;
                }
            }
        }
        return n == 0;
    }
};
```
