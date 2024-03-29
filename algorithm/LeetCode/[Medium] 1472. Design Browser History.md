1472. Design Browser History

You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

* `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
* `void visit(string url)` visits `url` from the current page. It clears up all the forward history.
* `string back(int steps)` Move steps back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history at most steps.
* `string forward(int steps)` Move steps forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history at most steps.
 

**Example:**
```
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
```

**Constraints:**

* `1 <= homepage.length <= 20`
* `1 <= url.length <= 20`
* `1 <= steps <= 100`
* `homepage` and `url` consist of  '.' or lower case English letters.
* At most `5000` calls will be made to `visit`, `back`, and `forward`.

# Submissions
---
**Solution 1: (Array)**
```
Runtime: 240 ms
Memory Usage: 16.1 MB
```
```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.sz = 1
        self.p = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.p+1] + [url]
        self.p += 1
        self.sz = self.p + 1

    def back(self, steps: int) -> str:
        self.p = max(0, self.p-steps)
        return self.history[self.p]

    def forward(self, steps: int) -> str:
        self.p = min(self.sz-1, self.p+steps)
        return self.history[self.p]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

**Solution 2: (Array)**
```
Runtime: 120 ms
Memory Usage: 33.3 MB
```
```c

typedef struct {
    int cur;
    int size;
    char **url;
} BrowserHistory;


BrowserHistory* browserHistoryCreate(char * homepage) {
    BrowserHistory *rst = calloc(1, sizeof(BrowserHistory));
    rst->url = malloc(101*sizeof(char *));
    for (int i = 0; i < 101; i ++)
        rst->url[i] = calloc(1, 21*sizeof(char));
    rst->cur = 0;
    rst->size = 1;
    strcpy(rst->url[rst->cur], homepage);
    return rst;
}

void browserHistoryVisit(BrowserHistory* obj, char * url) {
    obj->cur += 1;
    obj->size = obj->cur + 1;
    strcpy(obj->url[obj->cur], url);
}

char * browserHistoryBack(BrowserHistory* obj, int steps) {
    obj->cur = obj->cur - steps <= 0 ? 0 : obj->cur - steps;
    return obj->url[obj->cur];
}

char * browserHistoryForward(BrowserHistory* obj, int steps) {
    obj->cur = obj->cur + steps >= obj->size - 1 ? obj->size - 1 : obj->cur + steps;
    return obj->url[obj->cur];
}

void browserHistoryFree(BrowserHistory* obj) {
    for (int i = 0; i < 101; i++)
        free(obj->url[i]);
    free(obj->url);
    free(obj);
}

/**
 * Your BrowserHistory struct will be instantiated and called as such:
 * BrowserHistory* obj = browserHistoryCreate(homepage);
 * browserHistoryVisit(obj, url);
 
 * char * param_2 = browserHistoryBack(obj, steps);
 
 * char * param_3 = browserHistoryForward(obj, steps);
 
 * browserHistoryFree(obj);
*/
```

**Solution 3: (Array)**
```
Runtime: 137 ms
Memory: 57.8 MB
```
```c++
class BrowserHistory {
    string history[500];
    int cur, head;
public:
    BrowserHistory(string homepage) {
        cur = head = 0;
        history[head] = homepage;
    }
    
    void visit(string url) {
        cur += 1;
        head = cur;
        history[head] = url;
    }
    
    string back(int steps) {
        cur = cur-steps < 0? 0: cur-steps;
        return history[cur];
    }
    
    string forward(int steps) {
        cur = cur+steps > head? head: cur+steps;
        return history[cur];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
```
