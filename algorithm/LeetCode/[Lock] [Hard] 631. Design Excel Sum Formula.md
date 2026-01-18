631. Design Excel Sum Formula

Your task is to design the basic function of Excel and implement the function of sum formula. Specifically, you need to implement the following functions:

`Excel(int H, char W)`: This is the constructor. The inputs represents the height and width of the Excel form. H is a positive integer, range from 1 to 26. It represents the height. W is a character range from 'A' to 'Z'. It represents that the width is the number of characters from 'A' to W. The Excel form content is represented by a height * width 2D integer array C, it should be initialized to zero. You should assume that the first row of C starts from 1, and the first column of C starts from 'A'.


`void Set(int row, char column, int val)`: Change the value at C(row, column) to be val.


`int Get(int row, char column)`: Return the value at C(row, column).


`int Sum(int row, char column, List of Strings : numbers)`: This function calculate and set the value at `C(row, column)`, where the value should be the sum of cells represented by `numbers`. This function return the sum result at `C(row, column)`. This sum formula should exist until this cell is overlapped by another value or another sum formula.

`numbers` is a list of strings that each string represent a cell or a range of cells. If the string represent a single cell, then it has the following format : `ColRow`. For example, `"F7"` represents the cell at `(7, F).`

If the string represent a range of cells, then it has the following format : `ColRow1:ColRow2`. The range will always be a rectangle, and `ColRow1` represent the position of the top-left cell, and `ColRow2` represents the position of the bottom-right cell.


**Example 1:**
```
Excel(3,"C"); 
// construct a 3*3 2D array with all zero.
//   A B C
// 1 0 0 0
// 2 0 0 0
// 3 0 0 0

Set(1, "A", 2);
// set C(1,"A") to be 2.
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 0

Sum(3, "C", ["A1", "A1:B2"]);
// set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the rectangle range whose top-left cell is C(1,"A") and bottom-right cell is C(2,"B"). Return 4. 
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 4

Set(2, "B", 2);
// set C(2,"B") to be 2. Note C(3, "C") should also be changed.
//   A B C
// 1 2 0 0
// 2 0 2 0
// 3 0 0 6
```

**Note:**

* You could assume that there won't be any circular sum reference. For example, A1 = sum(B1) and B1 = sum(A1).
* The test cases are using double-quotes to represent a character.
* Please remember to **RESET** your class variables declared in class Excel, as static/class variables are **persisted across multiple test cases**. Please see here for more details.

# Submissions
---
**Solution 1: (DFS)**
```
Runtime: 32 ms
Memory Usage: 14.7 MB
```
```python
class Excel:

    def __init__(self, H: int, W: str):
        self.height, self.width = H, self._map(W) + 1
        self.form = [[0]*self.width for _ in range(self.height)]

    def _map(self, char):
        return ord(char) - 65
    
    def set(self, r: int, c: str, v: int) -> None:
        self.form[r-1][self._map(c)] = v

    def get(self, r: int, c: str) -> int:
        r, c = r-1, self._map(c)
        if type(self.form[r][c]) is int:
            return self.form[r][c]
        return sum(self.get(i+1, chr(j+65)) * self.form[r][c][(i, j)] for i, j in self.form[r][c])
    
    def _parse(self, string: str):
        i = int(''.join(char for char in string if char.isdigit())) - 1
        j = self._map([char for char in string if char.isalpha()][0])
        return i, j
    
    def sum(self, r: int, c: str, strs: List[str]) -> int:
        cells = collections.defaultdict(int)
        for string in strs:
            if ':' not in string:
                i, j = self._parse(string)
                cells[(i, j)] += 1
            else:
                start, end = string.split(':')
                i0, j0 = self._parse(start)
                i1, j1 = self._parse(end)
                for i in range(i0, i1+1):
                    for j in range(j0, j1+1):
                        cells[(i, j)] += 1
        self.form[r-1][self._map(c)] = cells
        return self.get(r, c)


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
```

**Solution 2: (DFS)**
```
Runtime: 0 ms, Beats 100.00%
Memory: 15.74 MB, Beats 97.44%
```
```c++
class Excel {
    vector<vector<int>> grid;
    unordered_map<int, unordered_map<int, vector<pair<int,int>>>> sums;
    void removeReferences(int row, int col) {
        for (auto r = sums.begin(); r != sums.end(); r++) {
            for (auto c = r->second.begin(); c != r->second.end(); c++) {
                auto &refs = c->second;
                for (auto itr = refs.begin(); itr != refs.end(); ) {
                    auto &[ref_r, ref_c] = *itr;
                    if (ref_r == row && ref_c == col) {
                        itr = refs.erase(itr);
                    } else {
                        itr++;
                    }
                }
            }
        }
    }
    void dfs(int row, int col, int val) {
        int diff = val - grid[row][col];
        grid[row][col] = val;
        if (sums.count(row) && sums[row].count(col)) {
            auto &refs = sums[row][col];
            for (auto &[ref_r, ref_c]: refs) {
                dfs(ref_r, ref_c, grid[ref_r][ref_c] + diff);
            }
        }
    }
public:
    Excel(int height, char width) {
        grid.assign(height, vector<int>(width - 'A' + 1));
    }
    
    void set(int row, char column, int val) {
        removeReferences(row - 1, column - 'A');
        dfs(row - 1, column - 'A', val);
    }
    
    int get(int row, char column) {
        return grid[row - 1][column - 'A'];
    }
    
    int sum(int row, char column, vector<string> numbers) {
        int val = 0, col = column - 'A';
        
        removeReferences(row - 1, col);
        for (int i = 0, r = 0, c = 0, n = numbers.size(); i < n; i++) {
            auto& str = numbers[i];
            auto pos = str.find(':');
            if (pos == string::npos) {
                r = stoi(str.substr(1)) - 1;
                c = str[0] - 'A';
                val += grid[r][c];
                sums[r][c].push_back({row - 1, col});
            } else {
                for (r = stoi(str.substr(1, pos - 1)) - 1; r <= stoi(str.substr(pos + 2)) - 1; r++) {
                    for (c = str[0] - 'A'; c <= str[pos+1] - 'A'; c++) {
                        val += grid[r][c];
                        sums[r][c].push_back({row - 1, col});
                    }
                }
            }
        }
        dfs(row - 1, col, val);
        return val;
    }
};

/**
 * Your Excel object will be instantiated and called as such:
 * Excel* obj = new Excel(height, width);
 * obj->set(row,column,val);
 * int param_2 = obj->get(row,column);
 * int param_3 = obj->sum(row,column,numbers);
 */
```
