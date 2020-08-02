1536. Minimum Swaps to Arrange a Binary Grid

Given an `n x n` binary `grid`, in one step you can choose two **adjacent rows** of the `grid` and swap them.

A `grid` is **said** to be **valid** if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the `grid` valid, or **-1** if the `grid` cannot be valid.

The main diagonal of a `grid` is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.

 

**Example 1:**

![1536_fw.jpg](img/1536_fw.jpg)
```
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
```

**Example 2:**

![1536_e2.jpg](img/1536_e2.jpg)
```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
```

**Example 3:**

![1536_e3.jpg](img/1536_e3.jpg)
```
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
```

**Constraints:**

* `n == grid.length`
* `n == grid[i].length`
* `1 <= n <= 200`
* `grid[i][j] is 0 or 1`

# Submissions
---
**Solution 1: (Greedy)**

**Explaination**

First we count the number of trailing zeroes in each row and store the numbers in arr.

For `grid = [[0,0,1],[1,1,0],[1,0,0]]`, we have `arr = [0,1,2]`.

We are hoping to rearrange arr so that `arr[i] >= n - i - 1`. In this case, `arr` will become `[2,1,0]` after rearrangement.

We can use greedy approach to do the rearrangement:

* find the smallest `j` such that `j >= i` and `arr[j] >= n - i - 1`
* do `j - i` swaps to bring `arr[j]` to index `i`

The reason why greedy approach works is that `arr` will be in "descending" order after rearragement, so it's fine to push smaller numbers downwards.

Here the "descending" order is not strict. `arr` is good as long as `arr[i] >= n - i - 1`. For example, `arr = [4,3,4,4]` is valid.


**Complexity**

* Time complexity: `O(N^2)`
* Space complexity: `O(N)`

```
Runtime: 544 ms
Memory Usage: 14.4 MB
```
```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def count(arr):
            ans = 0
            for i in range(n-1, -1, -1):
                if arr[i] == 0:
                    ans += 1
                else:
                    break
            return ans
            
        arr = [count(row) for row in grid]
        ans = 0
        for i in range(n):
            target = n - i - 1
            if arr[i] >= target:
                continue
            flag = False
            for j in range(i+1, n):
                if arr[j] >= target:
                    flag = True
                    ans += (j - i)
                    arr[i+1:j+1] = arr[i:j]
                    break
            if not flag:
                return -1
        
        return ans
```

**Solution 3: (Greedy)**
```
Runtime: 144 ms
Memory Usage: 25.8 MB
```
```c++
class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        vector<int>t; //t[i]: tailing zero count for i-th row
        const int n = grid.size();
        for(int i=0;i<n;i++){
            int count = 0;
            for(int j = n;--j>=0 && !grid[i][j]; )  count++;                
            t.push_back(count);
        }
        int ans = 0;        
        for(int i=0;i<t.size();i++){
            int k = i;
            int req = n-1 - i; // desired tailing zero count
            while(k<n && t[k]<req) k++; // greedily find first swaping candidate
            if(k==n) return -1;
            ans += k-i;
            
            while(k>i){ // simulate swaping operation of two adjacent rows
                t[k] = t[k-1];
                k--;
            }
        }    
        
        return ans;
    }
};
```