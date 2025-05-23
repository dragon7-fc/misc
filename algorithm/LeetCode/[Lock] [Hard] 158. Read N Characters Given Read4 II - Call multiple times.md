158. Read N Characters Given Read4 II - Call multiple times

Given a file and assume that you can only read the file using a given method `read4`, implement a method read to read n characters. **Your method** `read` **may be called multiple times**.

 

**Method read4:**

The API `read4` reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that `read4()` has its own file pointer, much like `FILE *fp` in C.

**Definition of read4:**
```
    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:
```

![158_157_example.png](img/158_157_example.png)

```
File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file
``` 

**Method read:**

By using the `read4` method, implement the method `read` that reads n characters from the file and store it in the buffer array buf. Consider that you **cannot** manipulate the file directly.

The return value is the number of actual characters read.

**Definition of read:**
```
    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
```

**Example 1:**
```
File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
```

**Example 2:**
```
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
```

**Note:**

* Consider that you **cannot** manipulate the file directly, the file is only accesible for `read4` but not for `read`.
* The `read` function may be called multiple times.
* Please remember to **RESET** your class variables declared in Solution, as static/class variables are **persisted across multiple test cases**. Please see here for more details.
* You may assume the destination buffer array, `buf`, is guaranteed to have enough space for storing n characters.
* It is guaranteed that in a given test case the same buffer `buf` is called by `read`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 36 ms
Memory Usage: 14 MB
```
```python
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    READ_SIZE = 4
    def __init__(self):
        self.buffer = [""] * self.READ_SIZE
        self.bufferIdx = 0
        self.bufferSize = 0
        
    def read(self, buf: List[str], n: int) -> int:
        idx = 0                                                     # Position of current char to read in buffer
        isEof = False                                               # Flag to detect "end of file" case
        
        while idx < n and not isEof:
            # copy from read4 to self.buffer
            if self.bufferIdx >= self.bufferSize:                   # Check if there is still data in the internal buffer
                self.bufferSize = read4(self.buffer)                # If not, read data into the internal buffer
                self.bufferIdx = 0                                  # Set the index to starting position
                if self.bufferSize < self.READ_SIZE:                # If read returned less than 4 characters
                    isEof = True                                    # Set "end of file" flag
            
            # copy form self.buffer to buf
            while self.bufferIdx < self.bufferSize and idx < n:     # While indexes of both buffers are valid
                buf[idx] = self.buffer[self.bufferIdx]           # Save character from the internal buffer
                idx += 1                                            # Increment both indexes
                self.bufferIdx += 1
        
        return idx
```

**Solution 2: (Array)**
```
Runtime: 0 ms
Memory Usage: 6.5 MB
```
```c++
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    char arr[4] = {'!','!','!','!'};
    int index=0;
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int i=0;
        while(i<n && index < 4 && arr[index]!='!')
            buf[i++] = arr[index++];
        if(i == n)
            return i;
        while(i < n){
            index = 0;
            arr[0] = '!'; arr[1] = {'!'}; arr[2] = {'!'}; arr[3] = '!';
            int len = read4(arr);
            if(len == 0)
                break;
            while(i<n && index < 4 && arr[index]!='!')
                buf[i++] = arr[index++];
        }
        return i;
    }
};
```

**Solution 3: (Deque)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 9.11 MB, Beats 4.35%
```
```c++
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
    deque<char> dp;
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int i, k;
        char buf4[4] = {0};
        while (dp.size() < n) {
            k = read4(buf4);
            if (k == 0) {
                break;
            }
            for (i = 0; i < k; i ++) {
                dp.push_back(buf4[i]);
            }
        }
        cout << dp.size() << endl;
        i = 0;
        while (i < n && dp.size()) {
            buf[i] = dp.front();
            dp.pop_front();
            i += 1;
        }
        return i;
    }
};
```
