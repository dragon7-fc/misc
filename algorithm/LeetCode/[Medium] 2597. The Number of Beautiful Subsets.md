2597. The Number of Beautiful Subsets

You are given an array `nums` of positive integers and a positive integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

Return the number of **non-empty beautiful** subsets of the array `nums`.

A **subset** of `nums` is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

**Example 1:**
```
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
```

**Constraints:**

* `1 <= nums.length <= 20`
* `1 <= nums[i], k <= 1000`

# Submissions
---
**Solution 1: (Hash Table, Backtracking)**
```
Runtime: 9112 ms
Memory: 14 MB
```
```python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        
        def bt(i, cnt):
            nonlocal ans
            if i == N:
                if cnt:
                    ans += 1
                return
            
            if nums[i] - k not in cnt and nums[i] + k not in cnt:
                cnt[nums[i]] += 1
                bt(i + 1, cnt)
                cnt[nums[i]] -= 1
                if not cnt[nums[i]]:
                    del cnt[nums[i]]
            bt(i + 1, cnt)
        
        bt(0, Counter())
        return ans
```

**Solution 2: (Binary Search, Backtracking)**
```
Runtime: 537 ms
Memory: 33.7 MB
```
```c++
class Solution {
    int solve(int i, int k, int n, vector<int> &nums, vector<int> &dp) {
        if (i == n) {
            return 0;
        }
        int o1 = 0, o2 = 0;
        o1 = solve(i + 1, k, n, nums, dp);
        if (binary_search(dp.begin(), dp.end(), nums[i] - k) == 0)
        {
            dp.push_back(nums[i]);
            o2 = 1 + solve(i + 1, k, n, nums, dp);
            dp.pop_back();
        }
        return o1 + o2;
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp;
        return solve(0, k, n, nums, dp);
    }
};
```

**Solution 3: (bitset, O(N * 2^N))**
```
Runtime: 1283 ms
Memory: 36.97 MB
```
```c++
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        sort(nums.begin(), nums.end());
        bool dp[1001];
        bool flag;
        for (int m = 1; m < (1<<n); m ++) {
            flag = true;
            memset(dp, 0, sizeof(dp));
            for (int i = 0; (1<<i) <= m; i++) {
                if (m & (1<<i)) {
                    if (nums[i] > k && dp[nums[i]-k]) {
                        flag = false;
                        break;
                    }
                    dp[nums[i]] = true;
                }
            }
            if (flag) {
                ans += 1;
            }
        }
        return ans;
    }
};
```

**Solution 4: (Using Bitset, O(N * 2^N))**
```
Runtime: 420 ms
Memory: 35.64 MB
```
```c++
class Solution {
    int countBeautifulSubsets(vector<int>& nums, int difference, int index, int mask) {
        // Base case: Return 1 if mask is greater than 0 (non-empty subset)
        if (index == nums.size())
            return mask > 0 ? 1 : 0;

        // Flag to check if the current subset is beautiful
        bool isBeautiful = true;

        // Check if the current number forms a beautiful pair with any previous
        // number in the subset
        for (int j = 0; j < index && isBeautiful; ++j){
            isBeautiful = ((1 << j) & mask) == 0 ||
                          abs(nums[j] - nums[index]) != difference;
            }

        // Recursively calculate beautiful subsets including and excluding the
        // current number
        int skip = countBeautifulSubsets(nums, difference, index + 1, mask);
        int take;
        if (isBeautiful) {
            take = countBeautifulSubsets(nums, difference, index + 1,
                                         mask + (1 << index));
        } else {
            take = 0;
        }

        return skip + take;
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        return countBeautifulSubsets(nums, k, 0, 0);
    }
};
```

**Solution 5: (Recursion with Backtracking, O(2^N))**
```
Runtime: 607 ms
Memory: 38.09 MB
```
```c++
class Solution {
    int countBeautifulSubsets(vector<int>& nums, int difference, unordered_map<int, int>& freqMap, int i) {
        // Base case: Return 1 for a subset of size 1
        if (i == nums.size()) {
            return 1;
        }
        // Count subsets where nums[i] is not taken
        int totalCount = countBeautifulSubsets(nums, difference, freqMap,
                                               i + 1); // nums[i] not taken

        // If nums[i] can be taken without violating the condition
        if (!freqMap[nums[i] - difference]) {
            freqMap[nums[i]]++;
            // Recursively count subsets where nums[i] is taken
            totalCount += countBeautifulSubsets(nums, difference, freqMap,
                                                i + 1); // nums[i] taken
            freqMap[nums[i]]--;
        }

        return totalCount;
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        // Frequency map to track elements
        unordered_map<int, int> freqMap;
        // Sort nums array
        sort(nums.begin(), nums.end());
        return countBeautifulSubsets(nums, k, freqMap, 0) - 1;
    }
};
```

**Solution 6: (Optimised Recursion (Deriving Recurrence Relation), groupby remainder, O(N * LogN + 2^N) = O(2^N))**
```
Runtime: 12 ms
Memory: 37.96 MB
```
```c++
class Solution {
    int countBeautifulSubsets(vector<pair<int, int>>& subsets, int numSubsets,
                              int difference, int i) {
        // Base case: Return 1 for a subset of size 1
        if (i == numSubsets) {
            return 1;
        }

        // Calculate subsets where the current subset is not taken
        int skip = countBeautifulSubsets(subsets, numSubsets, difference, i + 1);
        // Calculate subsets where the current subset is taken
        int take = (1 << subsets[i].second) - 1;

        // If next number has a 'difference', calculate subsets; otherwise, move
        // to next
        if (i + 1 < numSubsets &&
            subsets[i + 1].first - subsets[i].first == difference) {
            take *= countBeautifulSubsets(subsets, numSubsets, difference, i + 2);
        } else {
            take *= countBeautifulSubsets(subsets, numSubsets, difference, i + 1);
        }

        return skip + take; // Return total count of subsets
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int totalCount = 1;
        map<int, map<int, int>> freqMap;

        // Calculate frequencies based on remainder
        for (int& num : nums) {
            freqMap[num % k][num]++;
        }

        // Calculate subsets for each remainder group
        for (auto& fr : freqMap) {
            vector<pair<int, int>> subsets(fr.second.begin(), fr.second.end());
            totalCount *= countBeautifulSubsets(subsets, subsets.size(), k, 0);
        }

        return totalCount - 1;
    }
};
```

**Solution 7: (Dynamic Programming - Memoization, O(N * logN + 2^N) = O(2^N))**
```
Runtime: 12 ms
Memory: 38.74 MB
```
```c++
class Solution {
    int countBeautifulSubsets(vector<pair<int, int>>& subsets, int numSubsets,
                              int difference, int i, vector<int>& counts) {
        // Base case: Return 1 for a subset of size 1
        if (i == numSubsets) {
            return 1;
        }

        // If the count is already calculated, return it
        if (counts[i] != -1) {
            return counts[i];
        }

        // Calculate subsets where the current subset is not taken
        int skip = countBeautifulSubsets(subsets, numSubsets, difference, i + 1,
                                         counts);

        // Calculate subsets where the current subset is taken
        int take = (1 << subsets[i].second) - 1; // take the current subset

        // If the next number has a difference of 'difference', calculate
        // subsets accordingly
        if (i + 1 < numSubsets &&
            subsets[i + 1].first - subsets[i].first == difference) {
            take *= countBeautifulSubsets(subsets, numSubsets, difference,
                                          i + 2, counts);
        } else {
            take *= countBeautifulSubsets(subsets, numSubsets, difference,
                                          i + 1, counts);
        }

        return counts[i] = skip + take; // Store and return total count of subsets
    }
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int totalCount = 1;
        map<int, map<int, int>> freqMap;

        // Calculate frequencies based on remainder
        for (int& num : nums) {
            freqMap[num % k][num]++;
        }

        // Calculate subsets for each remainder group
        for (auto& fr : freqMap) {
            vector<pair<int, int>> subsets(fr.second.begin(), fr.second.end());
            // Store counts of subsets for memoization
            vector<int> counts(subsets.size(), -1); 
            totalCount *= countBeautifulSubsets(subsets, subsets.size(), k, 0, counts);
        }
        return totalCount - 1;
    }
};
```

**Solution 9: (Dynamic Programming - Iterative, O(N * logN))**
```
Runtime: 7 ms
Memory: 38.20 MB
```
```c++
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int totalCount = 1;

        map<int, map<int, int>> freqMap;

        // Calculate frequencies based on remainder
        for (int& num : nums) {
            freqMap[num % k][num]++;
        }

        // Iterate through each remainder group
        for (auto& fr : freqMap) {
            int n = fr.second.size(); // Number of elements in the current group

            vector<pair<int, int>> subsets(fr.second.begin(), fr.second.end());
            vector<int> counts(n + 1); // Array to store counts of subsets
            counts[n] = 1;             // Initialize count for the last subset

            // Calculate counts for each subset starting from the second last
            for (int i = n - 1; i >= 0; i--) {

                // Count of subsets skipping the current subset
                int skip = counts[i + 1];

                // Count of subsets including the current subset
                int take = (1 << subsets[i].second) - 1;

                // If next number has a 'difference', calculate subsets;
                // otherwise, move to next
                if (i + 1 < n && subsets[i + 1].first - subsets[i].first == k) {
                    take *= counts[i + 2];
                } else {
                    take *= counts[i + 1];
                }

                // Store the total count for the current subset
                counts[i] = skip + take; 
            }

            totalCount *= counts[0];
        }

        return totalCount - 1;
    }
};
```

**Solution 10: (Dynamic Programming - Optimized Iterative, O(N * logN))**
```
Runtime: 8 ms
Memory: 37.38 MB
```
```c++
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int totalCount = 1;
        map<int, map<int, int>> freqMap;

        // Calculate frequencies based on remainder
        for (int& num : nums) {
            freqMap[num % k][num]++;
        }

        // Iterate through each remainder group
        for (auto& fr : freqMap) {
            int prevNum = -k, prev2, prev1 = 1, curr;

            // Iterate through each number in the current remainder group
            for (auto& [num, freq] : fr.second) {
                // Count of subsets skipping the current number
                int skip = prev1; 

                // Count of subsets including the current number
                // Check if the current number and the previous number 
                // form a beautiful pair
                int take;
                if (num - prevNum == k) {
                    take = ((1 << freq) - 1) * prev2;
                } else {
                    take = ((1 << freq) - 1) * prev1;
                }

                // Store the total count for the current number
                curr = skip + take; 
                prev2 = prev1;
                prev1 = curr;
                prevNum = num;
            }
            totalCount *= curr;
        }
        return totalCount - 1;
    }
};
```
