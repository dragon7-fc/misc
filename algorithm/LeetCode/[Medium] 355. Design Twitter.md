355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

* **postTweet(userId, tweetId):** Compose a new tweet.
* **getNewsFeed(userId):** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
* **follow(followerId, followeeId):** Follower follows a followee.
* **unfollow(followerId, followeeId):** Follower unfollows a followee.

**Example:**
```
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
```

# Submissions
---
**Solution 1: (Hash Table, Heap)**

The key is to give each tweet a timestamp. I use the globalcount variable to accomplish the job.
As we are using a min-heap (poping out min key value at each heaqpop), we want the timestamp to be decreasing. So I use -1,-2,-3, ... as the timestamp for each tweetId.
One thing to keep in mind is that we don't want to add duplicate followers. Set can be used to address this issue.
For the getNewsFeed function, we first add all the desired tweets (the user's tweet and the tweets he follows) to the heap. Then we do the heapify. Then we pop out at most 10 tweets.

I think this question is very straight forward on the heapq concept.
Need to pay special attention to the corner cases, like repeated following.

* Time: O(nlogn)
* Space: O(n)

```
Runtime: 88 ms
Memory Usage: 18.2 MB
```
```python
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)
        self.globalcount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.globalcount -= 1 
        self.tweetMap[userId].append((self.globalcount,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        if userId in self.tweetMap: 
            heap.extend(self.tweetMap[userId]) 
        for id in self.following.get(userId,[]):
            if id != userId: 
                heap.extend(self.tweetMap.get(id,[]))
        
        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10: 
            item = heapq.heappop(heap)
            res.append(item[1])
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.following: 
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

**Solution 2: (Linked List)**
```
Runtime: 4 ms
Memory Usage: 9 MB
```
```c


int Time=0;
typedef struct tweets{
    int tweetId;
    int time;
    struct tweets* next;
}tweets;

typedef struct {
    int friends[1000][30];
    int totalFriends;
    int friendsCount[1000];
    tweets** news;
} Twitter;

Twitter* twitterCreate() {
    Twitter* obj=calloc(sizeof(Twitter),1);
    obj->news =calloc(sizeof(tweets *),1000);
    return obj;
}

typedef struct cmpItem{
    int time;
    int tweetId;
}cmpItem;

int cmpfunc (const void * a, const void * b)
{   
    cmpItem A=*(cmpItem*)a;
    cmpItem B=*(cmpItem*)b;
    
   return  A.time - B.time ;
}

void twitterPostTweet(Twitter* obj, int userId, int tweetId) {
    twitterFollow(obj,userId,userId);  //follow himself to get himself tweets.
    tweets* tmp=obj->news[userId];
    tweets* newnode=malloc(sizeof(tweets));
    newnode->tweetId=tweetId;
    newnode->time=Time++;
    newnode->next=NULL;
    if(!tmp)
    {
        obj->news[userId]=newnode;
        return;
    }
    while(tmp->next)
        tmp=tmp->next;
    
    tmp->next=newnode;
    return;
}

int* twitterGetNewsFeed(Twitter* obj, int userId, int* retSize) {
    int count=0,idx=0;
    int *ans=malloc(sizeof(int)*10);
    cmpItem *item=malloc(sizeof(cmpItem)*500);
    
    for(int i=0;i<obj->friendsCount[userId];i++)
    {
        int id=obj->friends[userId][i];
        tweets *tmp=obj->news[id];
        while(tmp)
        {
            item[count].time=tmp->time;             //store all related tweets and sort later.
            item[count++].tweetId=tmp->tweetId;
            tmp=tmp->next;
        }
        
    }
    qsort(item, count, sizeof(cmpItem), cmpfunc);
    for(int i=count-1;i>=count-10&&i>=0;i--)
        ans[idx++]=item[i].tweetId;
    
    *retSize=idx;
    return ans;
}

void twitterFollow(Twitter* obj, int followerId, int followeeId) {
    for(int i=0;i<obj->friendsCount[followerId];i++)
        if(obj->friends[followerId][i]==followeeId)   //if followed someone, don't follow again.
            return;
    obj->friends[followerId][obj->friendsCount[followerId]++]=followeeId;
}

void twitterUnfollow(Twitter* obj, int followerId, int followeeId) {
    int i;
    if(followerId!=followeeId)
    {
        for(i=0;i<obj->friendsCount[followerId];i++)
            if(obj->friends[followerId][i]==followeeId)
                break;
        if(i==obj->friendsCount[followerId]) return;    //no one match. 
        for(int j=i+1;j<obj->friendsCount[followerId];j++)
            obj->friends[followerId][j-1]=obj->friends[followerId][j];
        obj->friendsCount[followerId]--;
    }

}

void twitterFree(Twitter* obj) {
    free(obj);
}

/**
 * Your Twitter struct will be instantiated and called as such:
 * Twitter* obj = twitterCreate();
 * twitterPostTweet(obj, userId, tweetId);
 
 * int* param_2 = twitterGetNewsFeed(obj, userId, retSize);
 
 * twitterFollow(obj, followerId, followeeId);
 
 * twitterUnfollow(obj, followerId, followeeId);
 
 * twitterFree(obj);
*/
```
