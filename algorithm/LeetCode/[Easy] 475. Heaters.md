475. Heaters

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of `houses` and `heaters` on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

**Note:**

* Numbers of `houses` and `heaters` you are given are non-negative and will not exceed `25000`.
* Positions of `houses` and `heaters` you are given are non-negative and will not exceed `10^9`.
* As long as a house is in the `heaters`' warm radius range, it can be warmed.
* All the `heaters` follow your radius standard and the warm radius will the same.
 

**Example 1:**
```
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
```

**Example 2:**
```
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
```

# Submissions
---
**Solution 1: (Binary Search)**

Compute all distance between hourses and heaters, then get the max one.

```
Runtime: 296 ms
Memory Usage: 15.8 MB
```
```python
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        N = len(heaters)
        dist = []
        for h in houses:
            ind = bisect.bisect(heaters, h)  # search nearest heater index
            if ind == N: diff = h - heaters[-1]
            elif ind == 0: diff = heaters[0] - h
            else: diff = min(heaters[ind] - h, h - heaters[ind - 1])
            dist.append(diff)
        return max(dist)
```

**Solution 2: (Greedy)**
```
Runtime: 49 ms
Memory: 26 MB
```
```c++
class Solution {

public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        vector<int> res(houses.size(), INT_MAX); 
        
        // For each house, calculate distance to nearest RHS heater
        for (int i = 0, h = 0; i < houses.size() && h < heaters.size(); ) {
            if (houses[i] <= heaters[h]) {
                res[i] = heaters[h] - houses[i]; 
                i++;
            } else { 
                h++; 
            }
        }
        
        // For each house, calculate distance to nearest LHS heater
        for (int i = houses.size() - 1, h = heaters.size()-1; i >= 0 && h >= 0; ) {
            if (houses[i] >= heaters[h]) { 
                res[i] = min(res[i], houses[i] - heaters[h]); 
                i--; 
            } else { 
                h--; 
            }
        }
       
        return *max_element(res.begin(), res.end());
    }
};
```
