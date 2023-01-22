131. Palindrome Partitioning

Given a string `s`, partition s such that every substring of the partition is a **palindrome**.

Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

**Example 1:**
```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

**Example 2:**
```
Input: s = "a"
Output: [["a"]]
```

# Submissions
---
**Solution: (Backtracking)**
```
Runtime: 161 ms
Memory Usage: 49.2 MB
```
```c++
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> currentList;
        dfs(result, s, 0, currentList);
        return result;
    }
    
    void dfs(vector<vector<string>> &result, string &s, int start, vector<string> &currentList) {
        if (start >= s.length()) result.push_back(currentList);
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                // add current substring in the currentList
                currentList.push_back(s.substr(start, end - start + 1));
                dfs(result, s, end + 1, currentList);
                // backtrack and remove the current substring from currentList
                currentList.pop_back();
            }
        }
    }

    bool isPalindrome(string &s, int low, int high) {
        while (low < high) {
            if (s[low++] != s[high--]) return false;
        }
        return true;
    }
};
```

**Solution: (Backtracking with Dynamic Programming)**
```
Runtime: 206 ms
Memory Usage: 49.3 MB
```
```c++
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int len = s.length();
        vector<vector<bool>> dp (len, vector <bool> (len, false));
        vector<vector<string>> result;
        vector<string> currentList;
        dfs(result, s, 0, currentList, dp);
        return result;
    }
    
    void dfs(vector<vector<string>> &result, string &s, int start, vector<string> &currentList, vector<vector<bool>> &dp) {
        if (start >= s.length()) result.push_back(currentList);
        for (int end = start; end < s.length(); end++) {
            if (s[start] == s[end] && (end - start <= 2 || dp[start + 1][end - 1])) {
                dp[start][end] = true;
                currentList.push_back(s.substr(start, end - start + 1));
                dfs(result, s, end + 1, currentList, dp);
                currentList.pop_back();
            }
        }
    }
};
```

**Solution 1: (Backtracking)**
```
Runtime: 80 ms
Memory Usage: 13 MB
```
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:    
        def backtrack(s, candidate):
            if not s: res.append(candidate[:]); return
            for i in range(1, len(s)+1):
                #equal to s[:i] == s[:i][::-1]
                if s[:i] == s[i-1::-1]:
                    candidate.append(s[:i])
                    backtrack(s[i:], candidate)
                    candidate.pop()
        res = []
        backtrack(s, [])
        
        return res
```

**Solution 2: (DFS)**
```
Runtime: 493 ms
Memory Usage: 85.6 MB
```
```c
bool palindrome (char* s, int head, int end){
    for (int i = head ; head < end ; head++){
        if (s[head] != s[end]){
            return false;
        }
        end--;
    }
    return true;
}

void inputlist (char* s, int head, int end, char** list,int count, int* LONG){
    int listnow = 0;
    for (int i = head ; i <= end ; i++){
        list[count][listnow] = s[i];
        listnow++;
    }
    list[count][listnow] = '\0';
    LONG[count] = listnow;
}

void inputans (char* s, char** list,int count, int* LONG, char*** ans, int* returnSize, int** returnColumnSizes, int now, int len) {
    if (now == len){
        ans[*returnSize] = malloc(sizeof(char*)*count);
        for (int k = 0 ; k < count ; k++){
            ans[*returnSize][k] = malloc(sizeof(char)*(LONG[k]+1));
            for (int i = 0 ; i < LONG[k] ; i++){
                ans[*returnSize][k][i] = list[k][i];
            }
             ans[*returnSize][k][LONG[k]] = '\0';
        }
        (*returnColumnSizes)[*returnSize] = count;
        *returnSize += 1;
        return;
    }
    for (int i = now ; i < len ; i++){
        if (s[now] == s[i] && palindrome(s,now,i)){
            inputlist ( s, now, i, list, count, LONG);
            inputans ( s, list, count+1, LONG, ans, returnSize, returnColumnSizes, i+1, len);
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char *** partition(char * s, int* returnSize, int** returnColumnSizes){
    int len = strlen(s);
    int LONG[16] = {0};
    char*** ans = malloc(sizeof(char**)*40000);
    *returnSize = 0;
    (*returnColumnSizes) = malloc(sizeof(int)*40000);
    char** list = malloc(sizeof(char*)*16);
    for(int i = 0 ; i < 16 ; i++){
        list[i] = malloc(sizeof(char)*17);
    }
    for (int i = 0 ; i < len ; i++){
        if (s[0] == s[i] && palindrome(s,0,i)){
            inputlist ( s, 0, i, list, 0, LONG);
            inputans ( s, list, 1, LONG, ans, returnSize, returnColumnSizes, i+1, len);
        }
    }
    return ans;
}
```

**Solution 3: (Backtracking)**
```
Runtime: 850 ms
Memory: 31.1 MB
```
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def bt(cur, p):
            nonlocal ans
            if not cur:
                ans += [p]
                return
            for i in range(1, len(cur)+1):
                if cur[:i] == cur[:i][::-1]:
                    bt(cur[i:], p+[cur[:i]])

        bt(s, [])
        return ans
```

**Solution 5: (Backtracking)**
```
Runtime: 840 ms
Memory: 30.3 MB
```
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []

        def bt(i, p):
            nonlocal ans
            if i == N:
                ans += [p]
                return
            for ni in range(i+1, N+1):
                if s[i:ni] == s[i:ni][::-1]:
                    bt(ni, p+[s[i:ni]])

        bt(0, [])
        return ans
```

**Solution 6: (DP Top-Down)**
```
Runtime: 664 ms
Memory: 41.2 MB
```
```python
class Solution:
    @cache  # the memory trick can save some time
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
```
