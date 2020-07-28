386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 116 ms
Memory Usage: 21.2 MB
```
```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int, sorted([str(i) for i in range(1, n+1)]))
```

**Solution 2: (Math)**
```
Runtime: 4 ms
Memory Usage: 11.2 MB
```
```c++
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        if(n==0) return {};
        vector<int> result;
        int current=1; //Initial element
        for(int i=0;i<n;i++){
            result.push_back(current); //Push current to the result.
            current*=10; // Add zero at the end of current.
            while(current>n){ //If current exceeds n.
                current/=10; //Fall back to last element.
                current++; //Get Next in order.
                while(current%10==0) current/=10; //Remove extra trailing zeros.
            }
        }
        return result;
    }
};
```