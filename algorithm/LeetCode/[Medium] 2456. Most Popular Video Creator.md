2456. Most Popular Video Creator

You are given two string arrays `creators` and `ids`, and an integer array `views`, all of length `n`. The `i`th video on a platform was created by `creator[i]`, has an id of `ids[i]`, and has `views[i]` views.

The **popularity** of a creator is the **sum** of the number of views on **all** of the creator's videos. Find the creator with the **highest** popularity and the id of their **most** viewed video.

* If multiple creators have the highest popularity, find all of them.
* If multiple videos have the highest view count for a creator, find the lexicographically **smallest** id.

Return a 2D array of strings `answer` where `answer[i] = [creatori, idi]` means that `creatori` has the highest popularity and `idi` is the id of their most popular video. The answer can be returned in any order.

 

**Example 1:**
```
Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
Output: [["alice","one"],["bob","two"]]
Explanation:
The popularity of alice is 5 + 5 = 10.
The popularity of bob is 10.
The popularity of chris is 4.
alice and bob are the most popular creators.
For bob, the video with the highest view count is "two".
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer.
```

**Example 2:**
```
Input: creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
Output: [["alice","b"]]
Explanation:
The videos with id "b" and "c" have the highest view count.
Since "b" is lexicographically smaller than "c", it is included in the answer.
```

**Constraints:**

* `n == creators.length == ids.length == views.length`
* `1 <= n <= 10^5`
* `1 <= creators[i].length, ids[i].length <= 5`
* `creators[i]` and `ids[i]` consist only of lowercase English letters.
* `0 <= views[i] <= 10^5`

# Submissions
---
**Solution 1: (2 Hash Table)**
```
Runtime: 3979 ms
Memory: 73.2 MB
```
```python
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # total views by creator & list of videos by creator
        tot, vid = defaultdict(int), defaultdict(list)                    # Line 1
        
        # [1] compute total views for each creator and prepare
        #     a list of their videos to be searched for maximal
        #     views with lexicographically smallest id 
        #     (if there are several top videos with equal views)
        for c, i, v in zip(creators, ids, views):                         # Line 2
            tot[c] += v                                                   # Line 3
            vid[c].append((-v,i))                                         # Line 4
        m = max(tot.values())                                             # Line 5
        
        # [2] minus sign for views allows to extract needed minimal id
        #     by simply applying min (that will extract max views first,
        #     and, if needed, smallest id afterwards)
        return [[c,min(v)[1]] for c, v in vid.items() if tot[c] == m]     # Line 6
```

**Solution 2: (2 Hash Table)**
```
Runtime: 1068 ms
Memory: 251.1 MB
```
```c++
class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        unordered_map<string,long> tot;
        unordered_map<string,vector<pair<long,string>>> vid;
        
        long m = 0;
        for (int i = 0; i < creators.size(); ++i)
        {
            tot[creators[i]] += views[i]; 
            m = max(m, tot[creators[i]]);
            vid[creators[i]].emplace_back(-views[i], ids[i]);
        }
        
        vector<vector<string>> result;
        for (auto&[c,vv] : vid)
        {
            if (tot[c] != m) continue;
            result.push_back({c, min_element(vv.begin(),vv.end())->second});
        }
        
        return result;
    }
};
```
