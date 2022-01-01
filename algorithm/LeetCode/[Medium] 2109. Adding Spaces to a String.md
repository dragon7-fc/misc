2109. Adding Spaces to a String

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

* For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy Your Coffee"`.
Return the modified string after the spaces have been added.

 

**Example 1:**
```
Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation: 
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.
```

**Example 2:**
```
Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.
```

**Example 3:**
```
Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
```

**Constraints:**

* `1 <= s.length <= 3 * 10^5`
* `s` consists only of lowercase and uppercase English letters.
* `1 <= spaces.length <= 3 * 10^5`
* `0 <= spaces[i] <= s.length - 1`
* All the values of `spaces` are **strictly increasing**.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 104 ms
Memory Usage: 26 MB
```
```c


char * addSpaces(char * s, int* spaces, int spacesSize){
    int n = strlen(s) + 1 + spacesSize, i = 0, j = 0, k = 0;
    char *ans = calloc(1, n*sizeof(char));
    while (s[i] && j < spacesSize) {
        if (i == spaces[j]) {
            ans[k] = ' ';
            j += 1;
        } else {
            ans[k] = s[i];
            i += 1;
        }
        k += 1;
    }
    while (s[i]) {
        ans[k] = s[i];
        i += 1;
        k += 1;
    }
    return ans;
}
```

**Solution 2: (String)**
```
Runtime: 100 ms
Memory Usage: 25.9 MB
```
```c


char * addSpaces(char * s, int* spaces, int spacesSize){
    int len = strlen(s);
    
    // allocate: length of s + null + number of space
    char* s_new = (char*) malloc(len + 1 + spacesSize);
    
    // copy entire s to s_new including null
    for(int i=0, j=0; i<len+1; i++){
        if(spacesSize > 0){
          if(i == *spaces){
            s_new[j++] = ' ';
            spacesSize--;
            spaces++;
          }
        } 
        s_new[j++] = s[i];
    }

    return s_new;
}
```
