388. Longest Absolute File Path

Suppose we abstract our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:
```
dir
    subdir1
    subdir2
        file.ext
```
The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is `32` (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return `0`.

**Note:**

* The name of a file contains at least a `.` and an extension.
* The name of a directory or sub-directory will not contain a `..`
* Time complexity required: `O(n)` where `n` is the size of the input string.

Notice that `a/aa/aaa/file1.txt` is not the longest file path, if there is another path `aaaaaaaaaaaaaaaaaaaaa/sth.png`.

# Submissions
---
**Solution 1: (String)**
```
Runtime: 40 ms
Memory Usage: 13.9 MB
```
```python
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if input.count(".") == 0 or input.index(".") == len(input)-1:
            return 0
        s = input.split("\n")
        path = list()
        best = 0
        for d in s:
            if not path:
                path.append(d)
            else:
                c = d.count("\t")
                d = d.replace("\t", "")
                path = path[:c] + [d]
            if d.count(".") >= 1:
                best = max(best, len("/".join(path)))
        return best
```

**Solution 2: (Stack)**
```
Runtime: 2 ms
Memory Usage: 6.4 MB
```
```c++
class Solution {
public:
    int lengthLongestPath(string input) {
        int depth(0), res(0);
        stack<pair<string, int>> pile;
        string str="";
        for (int i=0; i < input.size(); i++) {
            bool isfile = 0;
            while (input[i] == '\n') {
                i += 1;
            }
            while (input[i] == '\t') {
                depth += 1;
                i += 1;
            }
            while (i < input.size() && input[i] != '\n' && input[i] != '\t') {
                str.push_back(input[i]);
                isfile |= (input[i]=='.');
                i += 1 ;
            }
            int rem = pile.size() - depth;
            while (rem--) pile.pop();
            pile.push({str, (pile.empty()? 0 : pile.top().second) + str.size() + 1});
            if (isfile) res = max(res, pile.top().second);
            depth = 0;
            str.erase();
        }
        return max(0, res-1);
    }
};
```

**Solution 3: (Stack)**
```
Runtime: 0 ms
Memory Usage: 6.6 MB
```
```c++
class Solution {
public:
    int lengthLongestPath(string input) {
        int depth(0), res(0);
        stack<pair<string, int>> pile;
        stringstream ss(input);
        string line, cur;
        while (getline(ss, line, '\n')) {
            bool isfile = 0;
            int i = 0;
            while (line[i] == '\t') {
                depth += 1;
                i += 1;
            }
            while (i < line.size()) {
                cur.push_back(line[i]);
                isfile |= (line[i]=='.');
                i += 1 ;
            }
            int rem = pile.size() - depth;
            while (rem--) pile.pop();
            pile.push({cur, (pile.empty()? 0 : pile.top().second) + cur.size() + 1});
            if (isfile) res = max(res, pile.top().second);
            depth = 0;
            cur.erase();
        }
        return max(0, res-1);
    }
};
```
