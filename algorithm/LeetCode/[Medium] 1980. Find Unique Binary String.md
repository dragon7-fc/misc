1980. Find Unique Binary String

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return a binary string of length `n` that does not appear in `nums`. If there are multiple answers, you may return any of them.

 

**Example 1:**
```
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
```

**Example 2:**
```
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
```

**Example 3:**
```
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 16`
* `nums[i].length == n`
* `nums[i]` is either `'0'` or `'1'`.

# Submissikons
---
**Solution 1: (String)**
```
Runtime: 28 ms
Memory Usage: 14.2 MB
```
```python
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        for start in range(17):
            bina = bin(start)[2:].zfill(length)
            if(bina not in nums):
                return bina
        return ""
```

**Solution 2: (Backtracking, Recursively Generate All Strings, Time: O(N^2))**
```
Runtime: 3 ms
Memory: 10.6 MB
```
```c++
class Solution {
    string bt(int i, int n, string &path, unordered_set<string> &st) {
        if (i == n) {
            if (!st.count(path)) {
                return path;
            }
            return "";
        }
        path.push_back('0');
        string rst = bt(i+1, n, path, st);
        if (rst != "") {
            return rst;
        }
        path.pop_back();
        path.push_back('1');
        rst = bt(i+1, n, path, st);
        if (rst != "") {
            return rst;
        }
        path.pop_back();
        return "";
    }
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        unordered_set<string> st(nums.begin(), nums.end());
        string path;
        return bt(0, n, path, st);
    }
};
```
