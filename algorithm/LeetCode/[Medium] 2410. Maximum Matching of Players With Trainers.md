2410. Maximum Matching of Players With Trainers

You are given a **0-indexed** integer array `players`, where `players[i]` represents the `ability` of the `i`th player. You are also given a **0-indexed** integer array `trainers`, where `trainers[j]` represents the training `capacity` of the `j`th trainer.

The `i`th player can match with the `j`th trainer if the player's ability is **less than or equal** to the trainer's training capacity. Additionally, the `i`th player can be matched with at most one trainer, and the `j`th trainer can be matched with at most one player.

Return the maximum number of matchings between `players` and `trainers` that satisfy these conditions.

 

**Example 1:**
```
Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.
```

**Example 2:**
```
Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.
```

**Constraints:**

* `1 <= players.length, trainers.length <= 10^5`
* `1 <= players[i], trainers[j] <= 10^9`

# Submissions
---
**Solution 1: (Binary Search)**
```
Runtime: 898 ms
Memory Usage: 29.2 MB
```
```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        match = idx = 0
        for p in sorted(players):
            idx = bisect.bisect_left(trainers, p, idx)
            if idx >= len(trainers):
                return match
            match += 1
            idx += 1
        return match
```

**Solution 2: (Binary Search)**
```
Runtime: 232 ms
Memory Usage: 76.5 MB
```
```c++
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(),players.end());
        sort(trainers.begin(),trainers.end());
        int len1=players.size();
        int len2=  trainers.size();
        
        int i=0;  //POINTER FOR PLAYERS
        int j=0; //POINTER FOR TRAINERS
        int count=0;
        while(i<len1){
            if(j==len2) break;
            
            int num=players[i]; 
            // USE  LOWER BOUND TO KNOW THE INDEX VALUE OF THE TRAINER WHICH IS GREATER OR EQUAL TO             //THE  PLAYERS VALUE
			
             j=lower_bound(trainers.begin()+j,trainers.end(),num)-trainers.begin();
             
            if(j>=len2) break;
            else if(trainers[j]>=num){
                count++;
                i++;
                
            }
            j++;
        }
        return count;
    }
};
```
