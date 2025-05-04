353. Design Snake Game

Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

**Example:**
```
Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
```

# Submissions
---
**Solution 1: (Stack)**
```
Runtime: 300 ms
Memory Usage: 15.2 MB
```
```python
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.d = {'U':(-1, 0) ,'L': (0, -1), 'R': (0, 1), 'D':(1, 0)}
        self.positions:List[List[int]] = [[0,0]] #this will act like a queue for the snake body. It always starts from 0,0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """    
        head = self.positions[0]        #We find the next position where head of the snake moves. Head is always first in the queue
        newHead = [head[0] + self.d[direction][0], head[1] + self.d[direction][1]]
                
        if self.positions and newHead in self.positions:    #If next location is already occupied by its body and that part is before tail, then it bites itself and it's a game over
            if self.positions[-1] != newHead:
                return -1
        
        if newHead[0] == -1 or newHead[0] == self.height or newHead[1] == -1 or newHead[1] == self.width:
            return -1                                   #If snake head crosses the screen boundary, game over
        
        self.positions.insert(0, newHead)               #If snake didn't kill itself, then it's good to move to new location
        if self.food and newHead == self.food[0]:       #Now check if the new position is where food is found
            self.food.pop(0)                            #If food is found, remove the food from the positions
            self.score += 1
        else:        
            self.positions.pop()                        #If food not found, then the length of snake didn't increase and hence tail will move forward
        
        return self.score
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
```

**Solution 2: (Stack)**
```
Runtime: 256 ms
Memory Usage: 70.1 MB
```
```python
class SnakeGame {
public:
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    list<pair<int, int>> pos;
    int w, h;
    vector<vector<int>> fd;
    SnakeGame(int width, int height, vector<vector<int>>& food) {
        pos.push_back(make_pair(0, 0));
        w = width;
        h = height;
        fd = food;
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    int move(string direction) {
        int x = 0, y = 0;
        if (direction == "U")   x -= 1;
        else if (direction == "D")  x += 1;
        else if (direction == "R")  y += 1;
        else if (direction == "L")  y -= 1;
        int x1, y1;
        x1 = pos.front().first;
        y1 = pos.front().second;
        x1 += x;
        y1 += y;
        //cout << x1 << "::" << y1 << endl;
        pair<int, int> back = pos.back();
        pos.pop_back();
        if (x1 < 0 || x1 >= h || y1 < 0 || y1 >= w) return -1;
        if (find(pos.begin(), pos.end(), make_pair(x1, y1)) != pos.end())   return -1;
        
        if (fd.size() > 0 && x1 == fd[0][0] && y1 == fd[0][1]) {
            pos.push_front(make_pair(x1, y1));
            pos.push_back(back);
            fd.erase(fd.begin());
        } else {
            pos.push_front(make_pair(x1, y1));
            //pos.pop_back();
        }
        return pos.size() - 1;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame* obj = new SnakeGame(width, height, food);
 * int param_1 = obj->move(direction);
 */
```

**Solution 3: (Double Eneded Queue)**
```
Runtime: 90 ms, Beats 67.07%
Memory: 66.38 MB, Beats 89.43%
```
```c++
class SnakeGame {
    unordered_map<string, pair<int,int>> d = {
        {"U", {-1,0}},
        {"D", {1,0}},
        {"L", {0,-1}},
        {"R", {0,1}}
    };
    int m, n, i = 0, score = 0;
    pair<int,int> cur;
    vector<vector<int>> dp;
    deque<pair<int,int>> dq;
public:
    SnakeGame(int width, int height, vector<vector<int>>& food) {
        m = height, n = width;
        cur = {0,0};
        dq.push_back(cur);
        dp = food;
    }
    
    int move(string direction) {
        auto [r, c] = cur;
        int nr, nc;
        nr = r + d[direction].first;
        nc = c + d[direction].second;
        cur = {nr, nc};
        if (i < dp.size() && nr == dp[i][0] && nc == dp[i][1]) {
            score += 1;
            i += 1;
        } else {
            dq.pop_front();
        }
        if (nr < 0 || nr >= m || nc < 0 || nc >= n || find(dq.begin(), dq.end(), cur) != dq.end()) {
            return -1;
        }
        dq.push_back(cur);
        return score;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame* obj = new SnakeGame(width, height, food);
 * int param_1 = obj->move(direction);
 */
```
