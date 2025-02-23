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

**Solution 2: (Backtracking, Recursively Generate All Strings, O(N^2))**
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
        // O(n^2)
        unordered_set<string> st(nums.begin(), nums.end());
        string path;
        // O(n)
        return bt(0, n, path, st);
    }
};
```

**Solution 3: (Iterate Over Integer Equivalents, O(n^2))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 13.01 MB, Beats 38.12%
```
```c++
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> integers;
        // O9n^2)
        for (string num : nums) {
            integers.insert(stoi(num, 0, 2));
        }
        
        int n = nums.size();
        for (int num = 0; num <= n; num++) {
            if (integers.find(num) == integers.end()) {
                // O9n)
                string ans = bitset<16>(num).to_string();
                return ans.substr(16 - n);
            }
        }
        
        return "";
    }
};
```

**Solution 4: (Random O(~))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 13.22 MB, Beats 31.65%
```
```c++
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> integers;
        for (string num : nums) {
            integers.insert(stoi(num, 0, 2));
        }
        
        int ans = stoi(nums[0], 0, 2);
        int n = nums.size();
        
        while (integers.find(ans) != integers.end()) {
            ans = rand() % (int) pow(2, n);
        }
        
        return bitset<16>(ans).to_string().substr(16 - n);
    }
};
```

**Solution 5: (Cantor's Diagonal Argument, O(n))**
```
Runtime: 0 ms, Beats 100.00%
Memory: 12.35 MB, Beats 99.65%
```
```c++
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string ans;
        for (int i = 0; i < nums.size(); i++) {
            char curr = nums[i][i];
            ans += curr == '0' ? '1' : '0';
        }
        
        return ans;
    }
};
```
