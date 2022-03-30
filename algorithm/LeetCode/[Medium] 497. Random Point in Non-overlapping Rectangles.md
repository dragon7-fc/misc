497. Random Point in Non-overlapping Rectangles

Given a list of **non-overlapping** axis-aligned rectangles `rects`, write a function `pick` which randomly and uniformily picks an **integer point** in the space covered by the rectangles.

**Note:**

* An integer point is a point that has integer coordinates. 
* A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
* ith rectangle = `rects[i] = [x1,y1,x2,y2]`, where `[x1, y1]` are the integer coordinates of the bottom-left corner, and `[x2, y2]` are the integer coordinates of the top-right corner.
* length and width of each rectangle does not exceed `2000`.
* `1 <= rects.length <= 100`
* `pick` return a point as an array of integer coordinates `[p_x, p_y]`
* `pick` is called at most `10000` times.\

**Example 1:**
```
Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
```

**Example 2:**
```
Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
```

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments. `Solution`'s constructor has one argument, the array of rectangles `rects`. `pick` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

# Submissions
---
**Solution 1: (Random, Binary Search)**
```
Runtime: 172 ms
Memory Usage: 16.5 MB
```
```python
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # number of points in each rectangle
        self.counts = [(x2 - x1 + 1) * (y2 - y1 + 1) 
                       for x1, y1, x2, y2 in rects]
        
        # accumulated (prefix) count of points
        self.accumulate_counts = []
        accumulated = 0
        for count in self.counts:
            accumulated += count
            self.accumulate_counts.append(accumulated)
            
        self.total = self.accumulate_counts[-1]

    def pick(self) -> List[int]:
        # rand is in [1, n], including both ends
        rand = random.randint(1, self.total)
        
        # find rightmost index with value <= rand
        # e.g., for accumulate_count of [2, 5, 8], with rand inputs range [1, 8]
        # there are 3 groups {1,2 | 3,4,5 | 6,7,8}, corresponding to index [0, 1, 2] respectively
        rect_index = bisect.bisect_left(self.accumulate_counts, rand)
        
        # use rand to find point_index, too
        point_index = rand - self.accumulate_counts[rect_index] + self.counts[rect_index] - 1
        x1, y1, x2, y2 = self.rects[rect_index]
        i, j = divmod(point_index, y2 - y1 + 1)
        return [x1 + i, y1 + j]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```

**Solution 2: (Random, Binary Search)**
```
Runtime: 76 ms
Memory Usage: 68.7 MB
```
```c++
class Solution {
    vector<int> v;
    vector<vector<int>> rects;
    // I add the +1 here because in some inputs they contain lines also like 
	// [ 1,2,1,3 ] ( rectangle with height 0 or width 0 but this also contains 2 points )
	// to also add these points I add +1.
    int area(vector<int>& r) {
        return (r[2] - r[0] + 1) * (r[3] - r[1] + 1);
    }
public:
    Solution(vector<vector<int>>& rects) {
        this->rects = rects;
        int totalArea=0;
        for (auto r: rects) {
            totalArea+=area(r);
            v.push_back(totalArea);
        }
    }
    
    vector<int> pick() {
        // pick a random reactangle in rects
        int rnd = rand() % v.back();
        int idx = upper_bound(v.begin(), v.end(), rnd) - v.begin();
        
        // pick a random point in rects[idx]
        auto r = rects[idx];
        int x = rand() % (r[2] - r[0] + 1) + r[0];
        int y = rand() % (r[3] - r[1] + 1) + r[1];
        return { x, y };
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(rects);
 * vector<int> param_1 = obj->pick();
 */
```
