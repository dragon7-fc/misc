451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

**Example 1:**
```
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:**
```
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:**
```
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 36 ms
Memory Usage: 14.5 MB
```
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        count = collections.Counter(s)
        for el, c in count.most_common():
            ans += [el] * c
            
        return ''.join(ans)
```

**Solution 2: (Heap)**
```
Runtime: 36 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def frequencySort(self, s: str) -> str:
        # count for char
        char2count = collections.Counter(s)
        
        # max heap, by - count
        heap = []
        for char, count in char2count.items():
            heapq.heappush(heap,(-count,char))
            
        # concatenate
        res = ''
        while heap:
            neg_c, char = heapq.heappop(heap)
            res += char*(-neg_c)
            
        return res
```

**Solution 3: (Sort)**
```
Runtime: 16 ms
Memory Usage: 8.5 MB
```
```c++
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> m;
        for (auto c: s) 
            m[c] += 1;
        vector<pair<char,int>>v;
        for(auto el : m)
            v.push_back(el);
        sort(v.begin(), v.end(), [](pair<char,int>& pa, pair<char,int>& pb){ return pa.second > pb.second;});
        string ans = "";
        for (auto el : v)
            for(int j=0; j<el.second; j++) ans += el.first;
        return ans;
    }
};
```

**Solution 4: (Heap)**
```
Runtime: 12 ms
Memory Usage: 8.5 MB
```
```c++
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> m;
        for (auto c: s) 
            m[c] += 1;
        priority_queue<pair<int,char>> pq;
        for (auto [a, cnt]: m)
            pq.push({cnt, a});
        string ans = "";
        while (!pq.empty()) {
            auto [cnt, a] = pq.top();
            pq.pop();
            while (cnt-- > 0)
                ans.push_back(a);
        }
        return ans;
    }
};
```

**Solution 5: (Sort)**
```
Runtime: 30 ms
Memory: 10.23 MB
```
```c++
class Solution {
public:
    string frequencySort(string s) {
        vector<int> cnt(256);
        for (auto &c: s) {
            cnt[c] += 1;
        }
        sort(s.begin(), s.end(), [&](char a, char b) {
            if (cnt[a] != cnt[b])
                return cnt[a] > cnt[b];
            else
                return a > b;
        });
        return s;
    }
};
```
