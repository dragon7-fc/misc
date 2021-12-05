415. Add Strings

Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.

**Note:**

* The length of both `num1` and `num2` is < `5100`.
* Both `num1` and `num2` contains only digits `0-9`.
* Both `num1` and `num2` does not contain any leading zero.
* You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

# Submissions
---
**Solution 1: (String, Hash Table)**
```
Runtime: 52 ms
Memory Usage: 12.9 MB
```
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {str(i) + str(j): str(i + j) for i in range(10) for j in range(10)}
        carry = 0
        maxlen = max(len(num1), len(num2))
        n1, n2 = num1.zfill(maxlen), num2.zfill(maxlen)
        result = ''
        for i, j in zip(n1[::-1], n2[::-1]):
            s = d[i + j] 
            if carry: 
                s = ('1' if len(s) == 2 else '') + d['1' + s[-1]] 
            result = s[-1] + result  
            if len(s) == 2: carry = True
            else: carry = False
        if carry: 
            result = '1' + result 
        return result
```

**Solution 2: (String)**
```
Runtime: 4 ms
Memory Usage: 6.1 MB
```
```c


char * addStrings(char * num1, char * num2){
    int num1_len = strlen(num1);
    int num2_len = strlen(num2);
    int carry = 0;
    int i,j;
    
    char* ret;
    int ret_idx = 0;
        
    ret = (char*)malloc(sizeof(char) * (num1_len+num2_len+1+1)); /* +1 for overflow, +1 for '\0' */
    
    i = num1_len-1;
    j = num2_len-1;
    
    while (i >= 0 && j >= 0) {
        int sum = num1[i--]-'0' + num2[j--]-'0' + carry;
        carry = sum / 10;
        ret[ret_idx++] = sum % 10 + '0';
    }
    
    while (i >= 0) {
        int sum = num1[i--]-'0' + carry;
        carry = sum / 10;
        ret[ret_idx++] = sum % 10 + '0';
    }

    while (j >= 0) {
        int sum = num2[j--]-'0' + carry;
        carry = sum / 10;
        ret[ret_idx++] = sum % 10 + '0';
    }
    
    if (carry) {
        ret[ret_idx++] = '1';
    }
    
    ret[ret_idx] = '\0';
    
    i = 0;
    j = ret_idx -1;
    
    while (i < j) {
        char tmp;
        tmp = ret[i];
        ret[i] = ret[j];
        ret[j] = tmp;
        i++;
        j--;
    } 

    return ret;
}
```
