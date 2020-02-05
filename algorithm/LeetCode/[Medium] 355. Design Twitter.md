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
**Solution 1: (Hash table)**

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