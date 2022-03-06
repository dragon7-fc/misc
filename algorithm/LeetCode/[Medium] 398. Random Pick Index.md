398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

**Note:**

The array size can be very large. Solution that uses too much extra space will not pass the judge.

**Example:**
```
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
```

# Submissions
---
**Solution: (Caching results using a hashmap)**
```
Runtime: 295 ms
Memory Usage: 51.8 MB
```
```c++
class Solution {
    unordered_map<int, vector<int>> indices;
public:
    Solution(vector<int>& nums) {
        int l = nums.size();
        for (int i = 0; i < l; ++i) {
            this->indices[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        int l = indices[target].size();
        // pick an index at random
        int randomIndex = indices[target][rand() % l];
        return randomIndex;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```

**Solution: (Reservoir sampling)**
```
Runtime: 130 ms
Memory Usage: 34.7 MB
```
```c++
class Solution {
    vector<int> nums;
public:
    Solution(vector<int>& nums) {
        this->nums.swap(nums);
    }
    
    int pick(int target) {
        int n = nums.size();
        int count = 0;
        int idx = 0;
        for (int i = 0; i < n; ++i) {
            // if nums[i] is equal to target, i is a potential candidate
            // which needs to be chosen uniformly at random
            if (nums[i] == target) {
                // increment the count of total candidates
                // available to be chosen uniformly at random
                count++;
                // we pick the current number with probability 1 / count (reservoir sampling)
                if (rand() % count == 0) {
                    idx = i;
                }
            }
        }
        return idx;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```

**Solution 1: (Reservoir Sampling)**
```
Runtime: 316 ms
Memory Usage: 16.8 MB
```
```python
class Solution:

    def __init__(self, nums: List[int]):
        self.num = nums

    def pick(self, target: int) -> int:
        rst, count = None, 0
        for i in range(len(self.num)):
            if self.num[i] != target: continue
            count += 1
            if random.randint(1, count) == count: rst = i
        return rst

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
