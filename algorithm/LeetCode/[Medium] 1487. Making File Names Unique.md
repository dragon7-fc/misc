1487. Making File Names Unique

Given an array of strings `names` of size `n`. You will create `n` folders in your file system such that, at the `i`th minute, you will create a folder with the name `names[i]`.

Since two files **cannot** have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of `(k)`, where, `k` is the **smallest positive integer** such that the obtained name remains unique.

Return an array of strings of length `n` where `ans[i]` is the actual name the system will assign to the `i`th folder when you create it.

 

**Example 1:**
```
Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]
Explanation: Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"
```

**Example 2:**
```
Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
Explanation: Let's see how the file system creates folder names:
"gta" --> not assigned before, remains "gta"
"gta(1)" --> not assigned before, remains "gta(1)"
"gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --> not assigned before, remains "avalon"
```

**Example 3:**
```
Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".
```

**Example 4:**
```
Input: names = ["wano","wano","wano","wano"]
Output: ["wano","wano(1)","wano(2)","wano(3)"]
Explanation: Just increase the value of k each time you create folder "wano".
```

**Example 5:**
```
Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.
```

**Constraints:**

* `1 <= names.length <= 5 * 10^4`
* `1 <= names[i].length <= 20`
* `names[i]` consists of lower case English letters, digits and/or round brackets.

# Submissions
---
**Solution 1: (Hash Table)**
```
Runtime: 424 ms
Memory Usage: 27.5 MB
```
```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nameMap = {} # baseName : largest k suffix
        res = []
        for n in names:
            if n in nameMap:
                # find k
                k = nameMap[n] + 1
                while ( n + "(" + str(k) + ")" ) in nameMap:
                    k += 1
                nameMap[n] = k
                n = n + "(" + str(k) + ")" # with suffix is now considered a base name
                
            nameMap[n] = 0 # first time seeing this base name
            res.append(n)
            
        return res
```

**Solution 2: (Hash Table)**
```
Runtime: 388 ms
Memory Usage: 58.8 MB
```
```c++
class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {
        unordered_map<string,int> m;// A map to store whether the particular name occurs how many times already
        for (int i=0; i < names.size(); i++)
        {
            if(m.find(names[i]) != m.end())// if the name already came
            {
                int k = m[names[i]];// it contains the number in brackets
                while (m.find(names[i] + "(" + to_string(k) + ")") != m.end())
                {
                    k ++;// Increase number until that didn't exist
                    m[names[i]]++;//mean while update in the map too
                }
                m[names[i]]++;// Recently we will use one more number so increment
                names[i] = names[i] + "(" + to_string(k) + ")";
            }
            m[names[i]] = 1;// Here we are storing  for example ...abc(1)=1 and abc(2)=1 it means abc(1) occcured one time, and abc=2 it means abc occured 2 times.
            /*
            Suppose you have a file named ABC occurring twice, we will store ABC with occurrence =2 and ABC(1) with occurrence =1... It helps when we get another file with name ABC(1) we can store like ABC(1)(1)
            */

        }
        return names;
    }
};
```