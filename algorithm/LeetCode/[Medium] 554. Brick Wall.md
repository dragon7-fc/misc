554. Brick Wall

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the **top** to the **bottom** and cross the **least** bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

**You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.**

**Example:**
```
Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation: 
```
![554_brick_wall.png](img/554_brick_wall.png)

**Note:**

* The width sum of bricks in different rows are the same and won't exceed INT_MAX.
* The number of bricks in each row is in range `[1,10,000]`. The height of wall is in range `[1,10,000]`. Total number of bricks of the wall won't exceed `20,000`.

# Submissions
---
**Solution 1: (Counter)**
```
Runtime: 188 ms
Memory Usage: 17.8 MB
```
```python
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        R = len(wall)
        counter = collections.Counter()
        for row in wall:
            pos = 0
            for width in row[:-1]:
                pos += width
                counter[pos] += 1
        return R - counter.most_common(1)[0][1] if counter else R
```

**Solution 2: (Counter, Linked List)**
```
Runtime: 48 ms
Memory Usage: 10.2 MB
```
```c
#define SIZE 1000   
struct HashArray
{
    int key;
    int count;
    struct HashArray* next;
}Hash[SIZE];       
void addHash(int num)    
{
    int temp=abs(num%SIZE);     
    if(Hash[temp].key==0)
    {
        Hash[temp].key=num;
        Hash[temp].count++;
    }else if(Hash[temp].key==num)
    {
        Hash[temp].count++;     
    }else
    {
        struct HashArray *p=&Hash[temp]; 
        while(p->key!=num&&p->next!=NULL)    
        {p=p->next;}
        if(p->key==num)
        {p->count++;}
        else
        {
            p->next=(struct HashArray*)malloc(sizeof(struct HashArray));
            p=p->next;
            p->key=num;
            p->count=1;
            p->next=NULL;
        }
    }   
}

int leastBricks(int** wall, int wallSize, int* wallColSize){
    int maxCount=0;
    int sum=0;
    struct HashArray *p;
    for(int i=0;i<SIZE;i++){
        Hash[i].key=0;
        Hash[i].count=0;
        Hash[i].next=NULL;
    }
    for(int i=0;i<wallSize;i++){
        sum=0;
        for(int j=0;j<wallColSize[i]-1;j++){
            sum=sum+wall[i][j];
            addHash(sum);
        }
    }
    for(int i=0;i<SIZE;i++){
        if(Hash[i].count!=0)
        {  
            if(maxCount<Hash[i].count){
                maxCount=Hash[i].count;
            }
            if(Hash[i].next!=NULL){
                p=&Hash[i];
                while(p->next!=NULL)    
                {
                    p=p->next;
                    if(maxCount<p->count){
                        maxCount=p->count;
                    }
                }
            }  
        }
    }
    return wallSize-maxCount;
}
```

**Solution 3: (Counter)**
```
Runtime: 48 ms
Memory Usage: 23.4 MB
```
```c++
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> cnt;
        int cur;
        for (auto v: wall) {
            cur = 0;
            for (int i = 0; i < v.size()-1; i++) {
                cur += v[i];
                cnt[cur] += 1;
            }
        }
        int mx = 0;
        for (auto[p, c]: cnt)
            mx = max(mx, c);
        return wall.size() - mx;
    }
};
```
