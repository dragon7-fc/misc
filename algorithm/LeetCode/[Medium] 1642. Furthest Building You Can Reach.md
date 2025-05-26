1642. Furthest Building You Can Reach

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by possibly using `bricks` or `ladders`.

While moving from building `i` to building `i+1` (`0`-indexed),

* If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.
* If the current building's height is **less than** the next building's height, you can either use **one ladder** or (`h[i+1] - h[i]`) **bricks**.

    Return the furthest building index (`0`-indexed) you can reach if you use the given `ladders` and `bricks` optimally.

 

**Example 1:**

![1642_q4.gif](img/1642_q4.gif)
```
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
```

**Example 2:**
```
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
```

**Example 3:**
```
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
```

**Constraints:**

* `1 <= heights.length <= 105`
* `1 <= heights[i] <= 106`
* `0 <= bricks <= 109`
* `0 <= ladders <= heights.length`

# Submissions
---
**Solution 1: (Heap, Greedy, greedy add to ladder then pick the smallest as brick)**
```
Runtime: 488 ms
Memory Usage: 28 MB
```
```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1
```

**Solution 2: (Heap, Greedy, greedy add to brick then pick the largest as ladder)**

    heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
                8  - 5 - 15 2  - 16
                     b      b
*/

```
Runtime: 209 ms
Memory Usage: 54 MB
```
```c++
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // Priority Queue for storing the bricks used in each step in decreasing order (Max at top)
        priority_queue<int> maxB;
    
        int i=0, diff =0; // i is used for storing the position and diff for storing difference.
        for(i=0; i<heights.size()-1; i++){ // go till before the last building.
            
            //difference of the height of corresponding buildings
            diff = heights[i+1]-heights[i];
            
            //If next building is equal or samaller than current then go to next building.
            if(diff <= 0){
                continue;
            }

            bricks -= diff; //taking the bricks needed for going to next building.
            maxB.push(diff); //adding the number of bricks used in priority queue.
            
            // if bricks become negetive then there were not enough bricks. So add a ladder in place of the step where most bricks were used.
            if(bricks < 0){
                bricks += maxB.top(); //taking back bricks from that step
                maxB.pop(); //As max bricks were removed so pop
                ladders--; //1 ladder used
            }

            //if ladder is negetive then the ladder was not provided to go to next building. So we can't proceed.
            if(ladders < 0) break;
        }
        
        // return the present position.
        return i;
    }
};
```
