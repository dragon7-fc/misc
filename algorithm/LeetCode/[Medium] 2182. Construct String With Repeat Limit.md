2182. Construct String With Repeat Limit

You are given a string `s` and an integer `repeatLimit`. Construct a new string `repeatLimitedString` using the characters of `s` such that no letter appears more than `repeatLimit` times in a row. You do not have to use all characters from `s`.

Return the **lexicographically largest** `repeatLimitedString` possible.

A string `a` is **lexicographically larger** than a string `b` if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`. If the first `min(a.length, b.length)` characters do not differ, then the longer string is the lexicographically larger one.

 

**Example 1:**
```
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
```

**Example 2:**
```
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
```

**Constraints:**

* `1 <= repeatLimit <= s.length <= 10^5`
* `s` consists of lowercase English letters.

# Submissions
---
**Solution 1: (Heap)**
```
Runtime: 1128 ms
Memory Usage: 16.8 MB
```
```python
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()] 
        heapify(pq)
        ans = []
        cnt = 0 
        while pq: 
            k, v = heappop(pq)
            if ans and ans[-1] == k and cnt == repeatLimit: 
                if not pq: break 
                kk, vv = heappop(pq)
                ans.append(kk)
                cnt = 1
                if vv-1: heappush(pq, (kk, vv-1))
                heappush(pq, (k, v))
            else: 
                if not ans or ans[-1] != k: cnt = 0 
                cnt += 1
                ans.append(k)
                if v-1: heappush(pq, (k, v-1))
        return "".join(chr(-x) for x in ans)
```

**Solution 2: (Heap)**
```
Runtime: 226 ms
Memory Usage: 24.9 MB
```
```c++
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        int n = s.length();
        unordered_map<char,int> m;
        for(int i=0;i<n;i++){
            m[s[i]]++;
        }
        priority_queue<pair<char,int>> pq;
        for(auto i: m){
            pq.push({i.first,i.second}); // pushing the characters with their frequencies.
        }
        
        string ans = "";
        while(!pq.empty()){
            char c1 = pq.top().first;
            int n1 = pq.top().second;
            pq.pop();
                
            int len = min(repeatLimit,n1); // Adding characters upto minimum of repeatLimit and present character count.
            for(int i=0;i<len;i++){ // adding the highest priority element to the ans.
                ans += c1;
            }
            
            char c2;
            int n2=0;
            if(n1-len>0){ // If the cnt of present character is more than the limit.
                if(!pq.empty()){ //Getting the next priority character.
                    c2 = pq.top().first;
                    n2 = pq.top().second;
                    pq.pop();
                }
                else{
                    return ans; // if there is no another letter to add, we just return ans.
                }
                ans += c2; // Adding next priority character to ans.
                
                // If the elements are left out, pushing them back into priority queue for next use.
                pq.push({c1,n1-len});
                if(n2-1>0){
                    pq.push({c2,n2-1});
                } 
            }
        }
        return ans;
    }
};
```
