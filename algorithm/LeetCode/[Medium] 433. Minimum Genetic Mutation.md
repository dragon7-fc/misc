433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from `"A"`, `"C"`, `"G"`, `"T"`.

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, `"AACCGGTT"` -> `"AACCGGTA"` is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

**Note:**

* Starting point is assumed to be valid, so it might not be included in the bank.
* If multiple mutations are needed, all mutations during in the sequence must be valid.
* You may assume start and end string is not the same.
 

**Example 1:**
```
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
```

**Example 2:**
```
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
```

**Example 3:**
```
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
```

# Submissions
---
**Solution 1: (BFS)**

Every time change one letter

```
Runtime: 24 ms
Memory Usage: 13.8 MB
```
```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank, queue = set(bank) ,[[start,0]]
        if end not in bank: return -1
        while queue:
            current_word, steps = queue.pop(0)
            if current_word == end: return steps
            for i in range(len(current_word)):
                for letter in ["A","C","G","T"]:
                    if letter != current_word[i]:
                        temp = current_word[:i] + letter + current_word[i+1:]
                        if temp in bank:
                            queue.append([temp, steps+1])
                            bank.remove(temp)
        return -1
```

**Solution 2: (BFS)**
```
Runtime: 0 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        vector<char>choices({'A','C','G','T'});
         //For fast lookup store the bank in a set
         unordered_set<string>s;
         for(string st:bank) s.insert(st);
         int mutations=0;
         queue<string>q;
         q.push(start);
         //BFS
         while(!q.empty())
         {
             int size=q.size();
             for(int i=0;i<size;i++)
             {
                 string f=q.front();
                 for(int j=0;j<f.length();j++)
                 {
                     for(char ch:choices)
                     {
                         if(f[j]==ch) continue;
                         string temp=f;
                         temp[j]=ch;
                         if(s.find(temp)==s.end()) continue;
                         s.erase(temp);
                         if(temp==end) return mutations+1;
                         q.push(temp);
                     }
                 }
                 q.pop();
             }
             mutations++;
         }
        return -1;  
    }
};
```
