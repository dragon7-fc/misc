306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain **at least** three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits `'0'-'9'`, write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence `1, 2, 03` or `1, 02, 3` is invalid.

 

**Example 1:**
```
Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

**Example 2:**
```
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
```

**Constraints:**

* num consists only of digits `'0'-'9'`.
* `1 <= num.length <= 35`

**Follow up:**

* How would you handle overflow for very large input integers?

# Submissions
---
**Solution 1: (Backtracking)**
```
Runtime: 32 ms
Memory Usage: 12.8 MB
```
```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = False
        maxLen = len(num) // 2
        def backtrack(prev, curr, numStr, maxLen):
            nonlocal ans
            currLen = len(curr)
            if len(numStr) < currLen:
                return
            for i in range(1, maxLen+1):
                nextWord = numStr[:i]
                nextNumStr = numStr[i:]
                if nextWord[0] == "0" and len(nextWord) > 1:
                    continue
                elif prev != -1 and int(prev)+int(curr) == int(nextWord) and nextNumStr == "":
                    ans = True
                    return
                elif prev == -1 or int(prev)+int(curr) == int(nextWord):
                    backtrack(curr, nextWord, nextNumStr, maxLen)
        for i in range(1, maxLen+1):
            if ans:
                break
            startWord = num[:i]
            if not (startWord[0] == "0" and len(startWord) > 1):
                backtrack(-1, num[:i], num[i:], maxLen)
        
        return ans
```

**Solution 2: (Backtracking)**
```
Runtime: 4 ms
Memory Usage: 6.2 MB
```
```c++
class Solution {
    bool ans=false;

    void fun(vector<long long int> &arr, string &num, long long int i)
    {
        if(i==num.length())
        {
            if(arr.size()>2)
                ans=true;
            return;
        }
        for(int j=i;j<num.length();j++) 
        { // First/Each number can be of length 1-17 so we call recursion after considering all cases of first number
            string s=num.substr(i,j-i+1);
            if(s.length()>17) //Max length of string is 35 and there should be minimum 3 numbers right? Think of the largest number in the sequence..
                break;        //99999999999999999+0+99999999999999999, right? So we don't need to consider values greater than length 17. 
            if(s.length()>=2 && s[0]=='0') 
                break; // Condition to avoid leading zeros
            long long int val=stoll(s);
            if(arr.size()<2 || (arr.back()+arr[arr.size()-2]==val)) // we store the number only if the array has less than 2 numbers or the value we have got
            {                                                       // is equal to the sum of preceding two numbers.
                arr.push_back(val);
                fun(arr,num,j+1);
                arr.pop_back();
            }
        }
    }
    
public:
    bool isAdditiveNumber(string num) {
        vector<long long int> arr; // stores the additive sequence
        fun(arr,num,0);
        return ans;
    }
};
```
