1257. Smallest Common Region

You are given some lists of `regions` where the first region of each list includes all other regions in that list.

Naturally, if a region `X` contains another region Y then X is bigger than `Y`.

Given two regions `region1`, `region2`, find out the smallest region that contains both of them.

If you are given regions `r1`, `r2` and `r3` such that `r1` includes `r3`, it is guaranteed there is no `r2` such that `r2` includes `r3`.

It's guaranteed the smallest region exists.

 

**Example 1:**

```
Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
```

**Constraints:**

* `2 <= regions.length <= 10^4`
* `region1 != region2`
* All strings consist of English letters and spaces with at most 20 letters.

# Submissions
---
**Solution 1:**

1. Build family tree from offsprings to their parents;
1. Use a HashSet to construct ancestry history of region1;
1. Retrieve ancestry of region2 by family tree till find the first common ancestry in ancestry history of region1.

```
Runtime: 268 ms
Memory Usage: 17.4 MB
```
```python
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {region[i] : region[0] for region in regions for i in range(1, len(region))}
        ancestry_history = {region1}
        while region1 in parents:
            region1 = parents[region1]
            ancestry_history.add(region1)
        while region2 not in ancestry_history:
            region2 = parents[region2]
        return region2
```