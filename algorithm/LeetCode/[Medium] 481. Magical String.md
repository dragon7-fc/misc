481. Magical String

A magical string **S** consists of only '1' and '2' and obeys the following rules:

The string **S** is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string **S** itself.

The first few elements of string **S** is the following: **S** = "1221121221221121122……"

If we group the consecutive '1's and '2's in **S**, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the **S** itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string **S**.

**Note:** N will not exceed 100,000.
```
Example 1:
Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
```

# Submissions
---
**Solution 1: (Queue)**

initialize num = 1, cnt = 0, and a empty queue q
in each step, operate as following:

1. q append current num, cnt increment by 1. if current num is 1, ans++
1. if cnt is same with length of current num which is q[0] as defination, then reset num with XOR mask, and reset cnt as 0
operator n times, then the number of 1's appending to q will be the result

```
Runtime: 168 ms
Memory Usage: 14 MB
```
```python
class Solution:
    def magicalString(self, n: int) -> int:
        q = collections.deque()
        mask = 1 ^ 2
        cnt, num, res = 0, 1, 0
        for _ in range(n):
            q.append(num)
            res += num == 1
            cnt += 1
            if cnt == q[0]:
                q.popleft()
                cnt = 0
                num ^= mask
        return res
```

**Solution 2: (String)**
```
Runtime: 8 ms
Memory Usage: 7.7 MB
```
```c++
class Solution {
public:
    int magicalString(int n) {
        int a = 1^2;
        string magic = "122";
        int i = 2, j = 2;
        while(j < n) {
            char ch = a^(magic[j]-'0')+'0';
            int times = magic[i]-'0';
            for(int k = 0; k < times; k++) {
                magic += ch;
                j++;
            }
            
            i++;
        }
        
        // cout << magic << endl;
        int cnt = 0;
        for(int i = 0; i < n; i++) 
            if(magic[i] == '1') cnt++;
        
        return cnt;
    }
};
```

**Solution 3: (String, Greedy)**
```
Runtime: 9 ms
Memory: 8.94 MB
```
```c++
class Solution {
public:
    int magicalString(int n) {
        if( n <= 3) return 1;
        string s = "122";
        int i = 2;
        while (s.size() < n)
        {
            if (s[i]=='1') {
                if (s[s.size()-1] == '2') s.push_back('1');
                else s.push_back('2');
            } else {
                if (s[s.size()-1] == '2') s += "11";
                else s += "22";
            }
            i++;
        }
        int cnt = count(s.begin(),s.begin() + n,'1');

        return cnt;
    }
};
```
