68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

**Note:**

* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
* The input array words contains at least one word.

**Example 1:**
```
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:**
```
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
```

**Example 3:**
```
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

# Submissions
---
**Solution 1: (String, Greedy)**
```
Runtime: 28 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst, arr, curlen = [], [], 0
        for word in words:
            if curlen + len(word) <= maxWidth:
                arr.append(word)
                curlen += len(word) + 1
            else:
                if len(arr) == 1: line = arr[0] + ' ' * (maxWidth-curlen+1)
                else:
                    div, mod = divmod(maxWidth - curlen + len(arr), len(arr)-1)
                    line = ''
                    for i in range(len(arr)-1):
                        line += arr[i]
                        line += ' ' * div
                        if i < mod: line += ' '
                    line += arr[-1]
                rst.append(line)
                arr, curlen = [word], len(word) + 1
        if arr: rst.append(' '.join(arr) + ' ' * (maxWidth-curlen+1))
        return rst
```

**Solution 2: (String)**
```
Runtime: 0 ms
Memory Usage: 6.2 MB
```
```c
int getLen(char *s){
    int len = 0;
    while (s[len]) len++;
    return len;
}

char *centerJustify(char **words, int wordsSize, int *len, int startIndex, int endIndex, int maxWidth){
    int width = 0;
    for (int i=startIndex; i<=endIndex; i++) width += len[i];
    int totalSpace = maxWidth - width;
    int space = totalSpace / (endIndex - startIndex);
    int bonusSpace = totalSpace % (endIndex - startIndex);
    char *line = (char*)malloc(sizeof(char)*(maxWidth + 1));
    int index = 0;
    for (int i=startIndex; i<=endIndex; i++){
        // add space characters from the second word.
        if (i > startIndex){
            for (int j=0; j<space; j++) line[index++] = ' ';
            if (bonusSpace-- > 0) line[index++] = ' ';
        }
        // add the word to the line
        for (int j=0; j<len[i]; j++){
            line[index++] = words[i][j];
        }
    }
    line[index] = 0;
    
    return line;
}

char *leftJustify(char **words, int wordsSize, int *len, int startIndex, int endIndex, int maxWidth){
    char *line = (char*)malloc(sizeof(char)*(maxWidth + 1));
    int index = 0;
    for (int i=startIndex; i<=endIndex; i++){
        // add space characters from the second word.
        if (i > startIndex) line[index++] = ' ';
        // add the word to the line
        for (int j=0; j<len[i]; j++){
            line[index++] = words[i][j];
        }
    }
    for(int i = index; i<maxWidth; i++) line[index++] = ' ';
    line[index] = 0;
    
    return line;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** fullJustify(char ** words, int wordsSize, int maxWidth, int* returnSize){
    if (wordsSize == 0){
		// return a line with all space charaters
		char **out = (char**)malloc(sizeof(char*));
		out[0] = (char*)malloc(sizeof(char) * maxWidth + 1);
		int index = 0;
		for (int i=0; i<maxWidth; i++) out[0][index++] = ' ';
		out[0][index] = 0;
		*returnSize = 1;
		return out;
	}
    int *len = (int*)calloc(wordsSize, sizeof(int));
    for (int i=0; i<wordsSize; i++){
        len[i] = getLen(words[i]);
    }
        
    int *startIndex = (int*)malloc(sizeof(int) * wordsSize);
    int startLen = 0;
    int width = 0, newWidth;
    startIndex[startLen++] = 0;
    for (int i=0; i<wordsSize; i++){
        newWidth = width + len[i];
        if (width > 0) newWidth++;
        
        if (newWidth > maxWidth){
        	startIndex[startLen++] = i;
        	width = len[i];
		}
        else width = newWidth;
    }
        
    char **out = (char**)malloc(sizeof(char*) * startLen);
    int index = 0;
    for (int i=0; i<startLen - 1; i++){
    	if (startIndex[i + 1] - startIndex[i] >= 2)
        	out[index++] = centerJustify(words, wordsSize, len, startIndex[i], startIndex[i + 1] - 1, maxWidth);
        else
        	out[index++] = leftJustify(words, wordsSize, len, startIndex[i], startIndex[i + 1] - 1, maxWidth);
    }
    out[index] = leftJustify(words, wordsSize, len, startIndex[startLen - 1], wordsSize - 1, maxWidth);
    
    free(startIndex);
    *returnSize = startLen;
    return out;
}
```
