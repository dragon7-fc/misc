3388. Count Beautiful Splits in an Array

You are given an array `nums`.

A split of an array `nums` is **beautiful** if:

* The array `nums` is split into three **non-empty subarrays**: `nums1`, `nums2`, and `nums3`, such that `nums` can be formed by concatenating `nums1`, `nums2`, and `nums3` in that order.
* The subarray `nums1` is a prefix of `nums2` **OR** `nums2` is a prefix of `nums3`.

Return the **number of ways** you can make this split.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

A **prefix** of an array is a subarray that starts from the beginning of the array and extends to any point within it.

 

**Example 1:**
```
Input: nums = [1,1,2,1]

Output: 2

Explanation:

The beautiful splits are:

A split with nums1 = [1], nums2 = [1,2], nums3 = [1].
A split with nums1 = [1], nums2 = [1], nums3 = [2,1].
```

**Example 2:**
```
Input: nums = [1,2,3,4]

Output: 0

Explanation:

There are 0 beautiful splits.
```
 

**Constraints:**

* `1 <= nums.length <= 5000`
* `0 <= nums[i] <= 50`

# Submissions
---
**Solution 1: (Rolling Hash)**
```
Runtime: 386 ms
Memory: 27.08 MB
```
```c++
class Solution {
    // Helper function to compare hashes of two subarrays
    bool isPrefix(const vector<long>& hash, int start1, int end1, int start2, int end2, long mod, const vector<long>& pow) 
    {
        int len1 = end1 - start1;
        int len2 = end2 - start2;

        if (len1 > len2)
        {
            return false;
        }

        long hash1 = (hash[end1] - (hash[start1] * pow[len1]) % mod + mod) % mod;
        long hash2 = (hash[start2 + len1] - (hash[start2] * pow[len1]) % mod + mod) % mod;

        return hash1 == hash2;
    }
public:
    int beautifulSplits(vector<int>& nums) {
        int n = nums.size();
        if (n < 3)
        {
            return 0;  // We need at least 3 elements to make a valid split
        }
        
        long mod = 1e9 + 7;
        long base = 31;
        
        // Compute prefix hashes
        vector<long> prefixHash(n + 1, 0); // Hash for prefix [0..i)
        vector<long> pow(n + 1, 1); // Store powers of base
        
        for (int i = 0; i < n; i++) 
        {
            pow[i + 1] = (pow[i] * base) % mod;
            prefixHash[i + 1] = (prefixHash[i] * base + nums[i]) % mod;
        }

        int count = 0;

        // Iterate over possible i and j such that 1 <= i < j < n
        for (int i = 1; i < n - 1; i++) 
        {
            for (int j = i + 1; j < n; j++) 
            {
                bool valid = false;

                // Check if nums1 is a prefix of nums2
                if (isPrefix(prefixHash, 0, i, i, j, mod, pow)) 
                {
                    valid = true;
                }
                
                // Check if nums2 is a prefix of nums3
                if (!valid && isPrefix(prefixHash, i, j, j, n, mod, pow)) 
                {
                    valid = true;
                }

                if (valid) 
                {
                    count++;
                }
            }
        }

        return count;
    }
};
```
