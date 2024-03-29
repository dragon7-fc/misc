447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` (**the order of the tuple matters**).

Find the number of boomerangs. You may assume that `n` will be at most 500 and coordinates of points are all in the range **[-10000, 10000]** (inclusive).

**Example:**
```
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
```

# Submissions
---

**Solution 1: (Hash Table)**
```
Runtime: 1180 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # dist function
        def dist(p1,p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        
        res = 0
        for p1 in points:
            # fix p1 as i
            lookup = {}  # distance -> points
            for p2 in points:
                if p1==p2:
                    continue
                d = dist(p1,p2)
                if d in lookup:
                    lookup[d]+=1
                else:
                    lookup[d]=1

            #  Find j and k as two element permutation: A_n^2 = n*(n-1)    
            for v in lookup.values():
                if v>1:
                    res+= v*(v-1)
        return res
```

**Solution 2: (Hash Table, Brute Force)**
```
Runtime: 598 ms
Memory Usage: 85 MB
```
```c++
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        unordered_map<int, int> distances;
        
        int boomerangCount = 0;
        for(int i = 0; i < points.size(); i++){
            for(int j = 0; j < points.size(); j++){
                if(i == j) continue;
                
                int num_one  = pow(points[i][0] - points[j][0], 2);
                int num_two  = pow(points[i][1] - points[j][1], 2);
                int distance = num_one + num_two;
                
                distances[distance]++;
            }
            
            for(auto iter = distances.begin(); iter != distances.end(); iter++)
                boomerangCount += iter->second * (iter->second - 1);
            
            distances.clear();
        }
        
        return boomerangCount;
    }
};
```
