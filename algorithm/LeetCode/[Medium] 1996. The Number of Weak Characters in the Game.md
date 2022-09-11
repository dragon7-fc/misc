1996. The Number of Weak Characters in the Game

You are playing a game that contains multiple characters, and each of the characters has two main properties: **attack** and **defense**. You are given a 2D integer array `properties` where `properties[i] = [attacki, defensei]` represents the properties of the `i`th character in the game.

A character is said to be **weak** if any other character has **both** attack and defense levels **strictly greater** than this character's attack and defense levels. More formally, a character `i` is said to be **weak** if there exists another character `j` where `attackj > attacki` and `defensej > defensei`.

Return the number of **weak** characters.

 

**Example 1:**
```
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
```
**Example 2:**
```
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
```

**Example 3:**
```
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
```

**Constraints:**

* `2 <= properties.length <= 10^5`
* `properties[i].length == 2`
* `1 <= attacki, defensei <= 10^5`

# Submissions
---
**Solution 1: (Sort, Greedy)**
```
Runtime: 2168 ms
Memory Usage: 67.7 MB
```
```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1][1] < d:
                stack.pop()
                ans += 1
            stack.append((a, d))
        return ans
```

**Solution 2: (Sort, Greedy)**
```
Runtime: 2128 ms
Memory Usage: 67.8 MB
```
```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        
        ans = 0
        curr_max = 0
        
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans
```

**Solution 3: (Sort, Greedy)**
```
Runtime: 803 ms
Memory Usage: 125.2 MB
```
```c++
class Solution {
    static bool comp(vector<int> &a,vector<int> &b){
        if(a[0]!=b[0])
            return a[0]>b[0];
        return a[1]<b[1];
    }
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(), properties.end(),comp);
        int maxTillNow = INT_MIN;
        int ans = 0;
        for(auto &p: properties){
            if (maxTillNow > p[1]) ans ++;
            else maxTillNow = p[1];
        }
        return ans;
    }
};
```
