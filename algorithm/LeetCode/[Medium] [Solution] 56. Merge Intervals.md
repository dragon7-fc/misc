56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**
```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Solution
---
## Approach 1: Connected Components
**Intuition**

If we draw a graph (with intervals as nodes) that contains undirected edges between all pairs of intervals that overlap, then all intervals in each connected component of the graph can be merged into a single interval.

**Algorithm**

With the above intuition in mind, we can represent the graph as an adjacency list, inserting directed edges in both directions to simulate undirected edges. Then, to determine which connected component each node is it, we perform graph traversals from arbitrary unvisited nodes until all nodes have been visited. To do this efficiently, we store visited nodes in a `Set`, allowing for constant time containment checks and insertion. Finally, we consider each connected component, merging all of its intervals by constructing a new Interval with `start` equal to the minimum start among them and `end` equal to the maximum end.

This algorithm is correct simply because it is basically the brute force solution. We compare every interval to every other interval, so we know exactly which intervals overlap. The reason for the connected component search is that two intervals may not directly overlap, but might overlap indirectly via a third interval. See the example below to see this more clearly.

![component](img/56_component.png)

Although (1, 5) and (6, 10) do not directly overlap, either would overlap with the other if first merged with (4, 7). There are two connected components, so if we merge their nodes, we expect to get the following two merged intervals:

```python
class Solution:
    def overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[interval_i].append(intervals[j])
                    graph[intervals[j]].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals):
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
```

**Complexity Analysis**

* Time complexity : $O(n^2)$

Building the graph costs $O(V + E) = O(V) + O(E) = O(n) + O(n^2) = O(n^2)$ time, as in the worst case all intervals are mutually overlapping. Traversing the graph has the same cost (although it might appear higher at first) because our visited set guarantees that each node will be visited exactly once. Finally, because each node is part of exactly one component, the merge step costs $O(V) = O(n)$ time. This all adds up as follows:

$O(n^2) + O(n^2) + O(n) = O(n^2)$

* Space complexity : $O(n^2)$

As previously mentioned, in the worst case, all intervals are mutually overlapping, so there will be an edge for every pair of intervals. Therefore, the memory footprint is quadratic in the input size.

## Approach 2: Sorting
**Intuition**

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

**Algorithm**

First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each interval in turn as follows: If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged. Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

A simple proof by contradiction shows that this algorithm always produces the correct answer. First, suppose that the algorithm at some point fails to merge two intervals that should be merged. This would imply that there exists some triple of indices $i$, $j$, and $k$ in a list of intervals $ints$ such that $i < j < k$ and ($ints[i]$, $ints[k]$) can be merged, but neither ($ints[i]$, $ints[j]$) nor ($ints[j]$, $ints[k]$) can be merged. From this scenario follow several inequalities:

\begin{aligned} ints[i].end < ints[j].start \\ ints[j].end < ints[k].start \\ ints[i].end \geq ints[k].start \\ \end{aligned} 

We can chain these inequalities (along with the following inequality, implied by the well-formedness of the intervals: $ints[j].start \leq ints[j].end$) to demonstrate a contradiction:

\begin{aligned} ints[i].end < ints[j].start \leq ints[j].end < ints[k].start \\ ints[i].end \geq ints[k].start \end{aligned} 

Therefore, all mergeable intervals must occur in a contiguous run of the sorted list.

![sort](img/56_sort.png)

Consider the example above, where the intervals are sorted, and then all mergeable intervals form contiguous blocks.

```python
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```

**Complexity Analysis**

* Time complexity : $O(n\log{}n)$

Other than the `sort` invocation, we do a simple linear scan of the list, so the runtime is dominated by the $O(nlgn)$ complexity of sorting.

* Space complexity : $O(1)$ (or $O(n)$)

If we can sort `intervals` in place, we do not need more than constant additional space. Otherwise, we must allocate linear space to store a copy of `intervals` and sort that.

# Submissions
---
**Solution 1: (Sorting)**
```
Runtime: 64 ms
Memory Usage: N/A
```
```python
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```

**Solution 2: (Sorting)**
```
Runtime: 16 ms
Memory Usage: 14.8 MB
```
```c++
class Solution {
public:
    
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> merged;
        for (auto interval : intervals) {
            // if the list of merged intervals is empty or if the current
            // interval does not overlap with the previous, simply append it.
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            }
            // otherwise, there is overlap, so we merge the current and previous
            // intervals.
            else {
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        return merged;
    }
};
```

**Solution 3: (Sorting)**
```
Runtime: 16 ms
Memory Usage: 7.8 MB
```
```c
int cmp(void* a,void* b){
    if((*(int**)a)[0]==(*(int**)b)[0]){
        return (*(int**)a)[1]-(*(int**)b)[1];
    }
    return (*(int**)a)[0]-(*(int**)b)[0];
}

// int cmp(void* a,void* b){
//     if(((int**)a)[0][0]==((int**)b)[0][0]){
//         return ((int**)a)[0][1]-((int**)b)[0][1];
//     }
//     return ((int**)a)[0][0]-((int**)b)[0][0];
// }


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes){
    *returnSize=0;
    if(intervalsSize==0){
        return NULL;
    }
    qsort(intervals,intervalsSize,sizeof(intervals[0]),cmp);
    int** ret=(int**)malloc(intervalsSize*sizeof(int*));
    int* tmp=NULL;
    int flag=0;
    for(int i=0;i<intervalsSize;i++){
        if(flag==0){
            tmp=intervals[i];
            flag=1;
            continue;
        }
        if(tmp[1]>=intervals[i][0]){
            tmp[1]=tmp[1]>intervals[i][1]?tmp[1]:intervals[i][1];
        }else{
            ret[(*returnSize)++]=tmp;
            flag=0;
            i--;
        }
    }
    ret[(*returnSize)++]=tmp;
    returnColumnSizes[0]=(int*)malloc((*returnSize)*sizeof(int));
    for(int i=0;i<(*returnSize);i++){
        returnColumnSizes[0][i]=2;
    }
    return ret;
}
```

**Solution 4: (Sort)**
```
Runtime: 4 ms, Beats 69.65%
Memory: 23.88 MB, Beats 58.94%
```
```c++
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size(), i, pre = -1;
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;
        for (i = 0; i < n; i ++) {
            if (intervals[i][0] > pre) {
                ans.push_back(intervals[i]);
                pre = intervals[i][1];
            } else {
                pre = max(pre, intervals[i][1]);
                ans.back()[1] = pre;
                
            }
        }
        return ans;
    }
};
```
