15. 3Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

**Example 2:**
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints:**

* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

# Submissions
---
**Solution : (Hash Table)**
```
Runtime: 668 ms
Memory Usage: 24.2 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(int)
        soln = []

        #creates a dictionary and counts the array
        for x in nums:
            dic[x] += 1
        
        #gets a list of keys and the length
        keys = list(dic.keys())
        length_k = len(keys)
        
        #for each key
        for i in range(length_k):
            x = keys[i]
            
            # case: [x, x, -2*x]
            #if the negative sum exists, add it to the solution
            if dic[x]>1:
                if -2*x in dic:
                    soln.append([x, x,-2*x])
                    
            # case: [x, y, -(x+y)
            for j in range(i+1,length_k):
                y = keys[j]
                #ensures we dont double count
                if -(x+y) in dic and -(x+y) not in [x,y]:
                    soln.append([x, y, -(x+y)])
        
        #special case of 0
        if 0 in dic:
            if dic[0] == 2:
                soln.remove([0,0,0])
        
        #returns unique solution sets
        soln=[list(x) for x in set(tuple(sorted(x)) for x in soln)]
        
        return soln
```

**Solution 2: (Two Pointers)**
```
Runtime: 728 ms
Memory Usage: 17.3 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:                
                cur = nums[i] + nums[j] + nums[k] 
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
```

**Solution 3: (Binary Search)**
```
Runtime: 216 ms
Memory Usage: 17.9 MB
```
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret
```

**Solution 4: (qsort)**
```
Runtime: 124 ms
Memory Usage: 20.2 MB
```
```c
int cmp(int *a, int *b)
{
    return *a - *b;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int **rst;
    int rstSize = 0;
    int basicSize = 8;
    int i, j, k, sum;

    rst = (int **)malloc(sizeof(int *) * basicSize);
    *returnColumnSizes = (int **)malloc(sizeof(int) * basicSize);

    qsort(nums, numsSize, sizeof(int), cmp);

    for (i = 0; i < numsSize - 1; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        j = i + 1;
        k = numsSize - 1;
        while (j < k) {
            sum = nums[i] + nums[j] + nums[k];
            if (sum == 0) {
                rst[rstSize] = (int *)malloc(sizeof(int) * 3);
                (*returnColumnSizes)[rstSize] = 3;
                rst[rstSize][0] = nums[i];
                rst[rstSize][1] = nums[j];
                rst[rstSize][2] = nums[k];

                rstSize++;

                while (j < k && nums[j] == nums[j + 1]) {
                    j++;
                }
                j++;
                k--;

                if (rstSize == basicSize) {
                    basicSize *= 2;
                    rst = (int **)realloc(rst, sizeof(int *) * basicSize);
                    (*returnColumnSizes) = (int **)realloc((*returnColumnSizes),sizeof(int) * basicSize);
				}

            } else if (sum > 0) {
                k--;
            } else {
                j++;
            }
        }
    }

    *returnSize = rstSize;

    return rst;
}
```

**Solution 5: (Sort, Two Pointers)**

    nums = [-1, 0, 1, 2, -1, -4]    
            -4 -1 -1  0   1   2
                ^  ^          ^
                ^     ^   ^


```
Runtime: 47 ms, Beats 71.50%
Memory: 29.02 MB, Beats 73.89%
```
```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size(), i, j, k;
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (i = 0; i < n - 2; i ++) {
            if (i && nums[i] == nums[i-1]) {
                continue;
            }
            j = i+1, k = n-1;
            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    ans.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j+1]) {
                        j += 1;
                    }
                    j += 1;
                    k -= 1;
                } else if (nums[i] + nums[j] + nums[k] > 0) {
                    k -= 1;
                } else {
                    j += 1;
                }
            }
        }
        return ans;
    }
};
```
