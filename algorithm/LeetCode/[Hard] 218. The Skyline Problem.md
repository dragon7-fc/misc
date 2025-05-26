218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are **given the locations and height of all the buildings** as shown on a cityscape photo (Figure A), write a program to **output the skyline** formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers `[Li, Ri, Hi]`, where `Li` and `Ri` are the `x` coordinates of the left and right edge of the ith building, respectively, and `Hi` is its height. It is guaranteed that `0 ≤ Li, Ri ≤ INT_MAX`, `0 < Hi ≤ INT_MAX`, and `Ri - Li > 0`. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`.

![718_skyline1.png](img/718_skyline1.png)

For instance, the dimensions of all buildings in Figure A are recorded as: `[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]` .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:`[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]`.

**Notes:**

* The number of buildings in any input list is guaranteed to be in the range `[0, 10000]`.
* The input list is already sorted in ascending order by the left x position `Li`.
* The output list must be sorted by the x position.
* There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` is not acceptable; the three lines of height `5` should be merged into one in the final output as such: `[...[2 3], [4 5], [12 7], ...]`

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 144 ms
Memory Usage: 17.7 MB
```
```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """ https://leetcode.com/problems/the-skyline-problem/
        General approach: scan the X positions where anything happened, maintaining a heap
        of active buildings and noting when the max height changes.
        """
        if not buildings:
            return []

        # left and right edges are where all the action happens, so collect these.
        # These will look like {x position: [height of each building starting or ending here]}
        building_left_edges = collections.defaultdict(list)
        building_right_edges = collections.defaultdict(list)
        for building in buildings:
            left_index, right_index, height = building
            building_left_edges[left_index].append(height)
            building_right_edges[right_index].append(height)

        x_positions_of_interest = sorted(
            set(building_left_edges.keys()).union(building_right_edges.keys())
        )

        # Heap will contain heights of all buildings present at the current x value.
        # Heights will be stored as negative values since heapq only supports min heaps,
        # and at any point we want the maximum height.
        active_buildings_heap = []
        last_skyline_height = 0
        skyline = []
        for x in x_positions_of_interest:
            for height in building_left_edges[x]:
                heapq.heappush(active_buildings_heap, -height)
            if building_right_edges[x]:
                for height in building_right_edges[x]:
                    active_buildings_heap.remove(-height)
                heapq.heapify(active_buildings_heap)

            skyline_here = -active_buildings_heap[0] if active_buildings_heap else 0

            if skyline_here != last_skyline_height:
                last_skyline_height = skyline_here
                skyline.append((x, skyline_here))

        return skyline
```

**Solution 2: (Divide and Conquer)**
```
Runtime: 176 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        def merge(sk1, sk2):
            res = [[0,-1]]
            i, j , c = 0, 0, min(sk1[0][0], sk2[0][0])
            if sk1[0][0] < sk2[0][0]:
                sk2 = [[sk1[0][0], 0]] + sk2
            elif sk1[0][0] > sk2[0][0]:
                sk1 = [[sk2[0][0], 0]] + sk1
            while i < len(sk1) or j < len(sk2):
                if sk1[i][1] > sk2[j][1]:
                    if sk1[i][1] != res[-1][1]:
                        res.append([c, sk1[i][1]])
                else:
                    if sk2[j][1] != res[-1][1]:
                        res.append([c, sk2[j][1]])
                if i + 1 < len(sk1) and (j + 1 >= len(sk2) or sk1[i+1][0] < sk2[j+1][0] ): 
                        c = sk1[i+1][0]
                        i +=1
                elif j + 1 < len(sk2) and (i + 1 >= len(sk1) or sk1[i+1][0] > sk2[j+1][0]):
                        c = sk2[j+1][0]
                        j +=1
                elif i+1 < len(sk1) and j + 1 < len(sk2) and sk1[i+1][0] == sk2[j+1][0]:
                    c = sk1[i+1][0]
                    i += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            res.pop(0)
            return res
        
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        if len(buildings) == 0:
            return []
        n = len(buildings) // 2
        a = buildings[:n]
        b = buildings[n:]

        return merge(self.getSkyline(a), self.getSkyline(b))
```

**Solution 3: (Sort, line sweeping, start-end event, sorted set)**
```
Runtime: 37 ms
Memory: 14.8 MB
```
```c++
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        // create event points
        // each event point has an coordinate and height associated with it
        vector<pair<int, int> > events;
        vector<vector<int>> contour;
        // tracks the max height 
        multiset<int> heights;
        // to track the height of each building, we create
        // two kinds of events for each building
        // left pt: We make the height -ve(so that sorting puts it in front)
        // right pt: We make the height +ve, this is just to help us know 
        // we have reached the end of building
        for(const vector<int>& building: buildings) {
            // left point
            events.emplace_back(make_pair(building[0], -1 * building[2]));
            // right point
            events.emplace_back(make_pair(building[1], building[2]));
        }
        
        // sort the event points by coordinate
        sort(events.begin(), events.end());
        int max_height_so_far = 0, curr_height = 0;
        
        // height of lst contour point
        heights.emplace(0);
        for(const pair<int, int>& event: events) {
            // add the event point if it is left, remove the event point if right
            if(event.second < 0)
                heights.emplace(-1 * event.second);
            else
                heights.erase(heights.find(event.second));
            
            // get the max height of the building seen so far
            // that still hasn't reached its end
            curr_height = *heights.rbegin();
            // if we get a height greater than the height seen so far,
            // that means that building will create a contour point
            if(curr_height != max_height_so_far) {
                contour.emplace_back(vector<int>{event.first, curr_height});
                max_height_so_far = curr_height;
            }
        }
        
        return contour;
    }
};
```

**Solution 4: (Sort, multiset)**
```
Runtime: 37 ms, Beats 20.28%
Memory: 34.20 MB, Beats 15.81%
```
```c++
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        map<int,vector<pair<int,int>>> m;
        for (int i = 0; i < buildings.size(); i ++) {
            m[buildings[i][0]].push_back({buildings[i][2], 0});
            m[buildings[i][1]].push_back({buildings[i][2], 1});
        }
        multiset<int> st;
        int cur = 0, ncur;
        vector<vector<int>> ans;
        for (auto [x, v]: m) {
            sort(v.begin(), v.end(), [](auto &pa, auto &pb){
                return pa.second < pb.second;
            });
            for (auto [y, t]: v) {
                if (t == 0) {
                    st.insert(y);
                } else {
                    auto it = st.find(y);
                    st.erase(it);
                }
            }
            ncur = cur;
            if (st.size() && ncur != *st.rbegin()) {
                ncur = *st.rbegin(); 
            } else if (st.size() == 0 && ncur != 0) {
                ncur = 0;
            }
            if (ncur != cur) {
                ans.push_back({x, ncur});
                cur = ncur;
            }
        }
        return ans;
    }
};
```
