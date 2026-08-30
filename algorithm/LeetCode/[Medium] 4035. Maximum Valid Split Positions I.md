4035. Maximum Valid Split Positions I

You are given an integer array `nums`.

You may remove at most one element from `nums`. Let `arr` be the array of remaining elements in their original order, and let m be its length.

A split position `i` of `arr` is **valid** if:

* `0 <= i < m - 1`, and
* `gcd(arr[0..i]) == gcd(arr[i + 1..m - 1])`.

An array of length 1 has no valid split positions.

The **score** of `arr` is the number of valid split positions in it.

Return the **maximum possible score** of `arr`.

Here, `gcd(a)` denotes the **greatest common divisor** of all elements in the array `a`.

 

**Example 1:**
```
Input: nums = [10,30,15,10]

Output: 2

Explanation:

One optimal solution is to remove nums[2] = 15. Then arr = [10, 30, 10].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	10	10
1	10	10
All split positions are valid. Thus, the answer is 2.
```

**Example 2:**
```
Input: nums = [2,10,14]

Output: 1

Explanation:

One optimal solution is to not remove any element. Then arr = [2, 10, 14].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	2	2
1	2	14
Only the split position at index 0 is valid. Thus, the answer is 1.
```

**Example 3:**
```
Input: nums = [2,4]

Output: 0

Explanation:

The only remaining array that has a split position is arr = [2, 4].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	2	4
There are no valid split positions. Thus, the answer is 0.
```
 

**Constraints:**

* `2 <= nums.length <= 1000`
* `1 <= nums[i] <= 10^9`

# Submissions
---
**Solution 1: (Prefix Sum, brute force)**
```
Runtime: 1071 ms, Beats 55.56%
Memory: 29.74 MB, Beats 100.00%
```
```c++
class Solution {
public:
    int maxValidSplits(vector<int>& nums) {
        int n = nums.size();
        vector<int> right(n - 1);
        right[n - 2] = nums[n - 1];
        for (int i = n - 3; i >= 0; i --) {
            right[i] = gcd(nums[i + 1], right[i + 1]);
        }
        int left = -1;
        int ans = 0;
        for (int i = 0; i < n - 1; i ++) {
            if (left == -1) {
                left = nums[i];
            } else {
                left = gcd(left, nums[i]);
            }
            ans += left == right[i];
        }
        for (int i = 0; i < n; i ++) {
            right.clear();
            for (int j = n - 1; j >= 0; j --) {
                if (j == i) {
                    continue;
                }
                if (right.empty()) {
                    right.push_back(nums[j]);
                } else {
                    right.push_back(gcd(right.back(), nums[j]));
                }
            }
            left = -1;
            int cur = 0;
            for (int j = 0; j < n; j ++) {
                if (j == i) {
                    continue;
                }
                cur += left == right.back();
                right.pop_back();
                if (left == -1) {
                    left = nums[j];
                } else {
                    left = gcd(left, nums[j]);
                }
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};
```

**Solution 2: (Prefix Sum, brute force)**
```
Runtime: 1477 ms, Beats 11.11%
Memory: 571.38 MB, Beats 33.33%
```
```c++
class Solution {
public:
    int maxValidSplits(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;

        for(int i = -1; i < n; i++){

            vector<int> arr;

            for(int j = 0; j < n; j++){
                if(i == j) continue;
                arr.push_back(nums[j]);
            }

            int m = arr.size();

            if(m < 2) continue;

            vector<int> prefix(m);
            vector<int> suffix(m);

            prefix[0] = arr[0];

            for(int j = 1; j < m; j++){
                prefix[j] = gcd(prefix[j - 1], arr[j]);
            }

            suffix[m - 1] = arr[m - 1];

            for(int j = m - 2; j >= 0; j--){
                suffix[j] = gcd(suffix[j + 1], arr[j]);
            }

            int score = 0;

            for(int j = 0; j < m - 1; j++){
                if(prefix[j] == suffix[j + 1]){
                    score++;
                }
            }

            ans = max(ans, score);
        }

        return ans;
    }
};
```
