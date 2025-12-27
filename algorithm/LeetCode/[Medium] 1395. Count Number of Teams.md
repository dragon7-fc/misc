1395. Count Number of Teams

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

* Choose 3 soldiers with index `(i, j, k)` with rating `(rating[i], rating[j], rating[k])`.
* A team is valid if:  `(rating[i] < rating[j] < rating[k])` or `(rating[i] > rating[j] > rating[k])` where (`0 <= i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

**Example 1:**
```
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
```

**Example 2:**
```
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
```

**Example 3:**
```
Input: rating = [1,2,3,4]
Output: 4
```

**Constraints:**

* `n == rating.length`
* `1 <= n <= 200`
* `1 <= rating[i] <= 10^5`

# Submissions
---
**Solution 1: (itertools)**
```
Runtime: 1820 ms
Memory Usage: 29.2 MB
```
```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return sum([i > j > k or i < j < k for i, j, k in itertools.combinations(rating, 3)])
```

**Solution 2: (Dynamic Programming (Memoization))**
```
Runtime: 106 ms
Memory: 14.31 MB
```
```c++
class Solution {
     int countIncreasingTeams(const vector<int>& rating, int currentIndex,
                             int teamSize,
                             vector<vector<int>>& increasingCache) {
        int n = rating.size();

        // Base case: reached end of array
        if (currentIndex == n) return 0;

        // Base case: found a valid team of size 3
        if (teamSize == 3) return 1;

        // Return cached result if available
        if (increasingCache[currentIndex][teamSize] != -1) {
            return increasingCache[currentIndex][teamSize];
        }

        int validTeams = 0;

        // Recursively count teams with increasing ratings
        for (int nextIndex = currentIndex + 1; nextIndex < n; nextIndex++) {
            if (rating[nextIndex] > rating[currentIndex]) {
                validTeams += countIncreasingTeams(
                    rating, nextIndex, teamSize + 1, increasingCache);
            }
        }

        // Cache and return the result
        return increasingCache[currentIndex][teamSize] = validTeams;
    }

    int countDecreasingTeams(const vector<int>& rating, int currentIndex,
                             int teamSize,
                             vector<vector<int>>& decreasingCache) {
        int n = rating.size();

        // Base case: reached end of array
        if (currentIndex == n) return 0;

        // Base case: found a valid team of size 3
        if (teamSize == 3) return 1;

        // Return cached result if available
        if (decreasingCache[currentIndex][teamSize] != -1) {
            return decreasingCache[currentIndex][teamSize];
        }

        int validTeams = 0;

        // Recursively count teams with decreasing ratings
        for (int nextIndex = currentIndex + 1; nextIndex < n; nextIndex++) {
            if (rating[nextIndex] < rating[currentIndex]) {
                validTeams += countDecreasingTeams(
                    rating, nextIndex, teamSize + 1, decreasingCache);
            }
        }

        // Cache and return the result
        return decreasingCache[currentIndex][teamSize] = validTeams;
    }
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int teams = 0;
        vector<vector<int>> increasingCache(n, vector<int>(4, -1));
        vector<vector<int>> decreasingCache(n, vector<int>(4, -1));

        // Calculate total teams by considering each soldier as a starting point
        for (int startIndex = 0; startIndex < n; startIndex++) {
            teams +=
                countIncreasingTeams(rating, startIndex, 1, increasingCache) +
                countDecreasingTeams(rating, startIndex, 1, decreasingCache);
        }

        return teams;
    }
};
```

**Solution 3: (Dynamic Programming (Tabulation))**
```
Runtime: 83 ms
Memory: 14.42 MB
```
```c++
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int teams = 0;

        // Tables for increasing and decreasing sequences
        vector<vector<int>> increasingTeams(n, vector<int>(4, 0));
        vector<vector<int>> decreasingTeams(n, vector<int>(4, 0));

        // Fill the base cases. (Each soldier is a sequence of length 1)
        for (int i = 0; i < n; i++) {
            increasingTeams[i][1] = 1;
            decreasingTeams[i][1] = 1;
        }

        // Fill the tables
        for (int count = 2; count <= 3; count++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (rating[j] > rating[i]) {
                        increasingTeams[j][count] +=
                            increasingTeams[i][count - 1];
                    }
                    if (rating[j] < rating[i]) {
                        decreasingTeams[j][count] +=
                            decreasingTeams[i][count - 1];
                    }
                }
            }
        }

        // Sum up the results (All sequences of length 3)
        for (int i = 0; i < n; i++) {
            teams += increasingTeams[i][3] + decreasingTeams[i][3];
        }

        return teams;
    }
};
```

**Solution 4: (DP Bottom-Up)**
```
Runtime: 20 ms
Memory: 12.41 MB
```
```c++
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size(), dp[1000][2] = {0}, ans = 0;
        for (int j = 1; j < n; j ++) {
            for (int i = 0; i < j; i ++) {
                if (rating[i] > rating[j]) {
                    ans += dp[i][0];
                    dp[j][0] += 1;
                } else {
                    ans += dp[i][1];
                    dp[j][1] += 1;
                }
            }
        }
        return ans;
    }
};
```

**Solution 5: (Dynamic Programming (Optimized))**
```
Runtime: 28 ms
Memory: 11.71 MB
```
```c++
class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int teams = 0;

        // Iterate through each soldier as the middle soldier
        for (int mid = 0; mid < n; mid++) {
            int leftSmaller = 0;
            int rightLarger = 0;

            // Count soldiers with smaller ratings on the left side of the
            // current soldier
            for (int left = mid - 1; left >= 0; left--) {
                if (rating[left] < rating[mid]) {
                    leftSmaller++;
                }
            }

            // Count soldiers with larger ratings on the right side of the
            // current soldier
            for (int right = mid + 1; right < n; right++) {
                if (rating[right] > rating[mid]) {
                    rightLarger++;
                }
            }

            // Calculate and add the number of ascending rating teams
            // (small-mid-large)
            teams += leftSmaller * rightLarger;

            // Calculate soldiers with larger ratings on the left and smaller
            // ratings on the right
            int leftLarger = mid - leftSmaller;
            int rightSmaller = n - mid - 1 - rightLarger;

            // Calculate and add the number of descending rating teams
            // (large-mid-small)
            teams += leftLarger * rightSmaller;
        }

        // Return the total number of valid teams
        return teams;
    }
};
```

**Solution 6: (Binary Indexed Tree (Fenwick Tree), left right)**
```
Runtime: 8 ms
Memory: 21.25 MB
```
```c++
class Solution {
    // Update the Binary Indexed Tree
    void updateBIT(vector<int>& BIT, int index, int value) {
        while (index < BIT.size()) {
            BIT[index] += value;
            index +=
                index & (-index);  // Move to the next relevant index in BIT
        }
    }

    // Get the sum of all elements up to the given index in the BIT
    int getPrefixSum(vector<int>& BIT, int index) {
        int sum = 0;
        while (index > 0) {
            sum += BIT[index];
            index -= index & (-index);  // Move to the parent node in BIT
        }
        return sum;
    }
public:
    int numTeams(vector<int>& rating) {
        // Find the maximum rating
        int maxRating = 0;
        for (int r : rating) {
            maxRating = max(maxRating, r);
        }

        // Initialize Binary Indexed Trees for left and right sides
        vector<int> leftBIT(maxRating + 1, 0);
        vector<int> rightBIT(maxRating + 1, 0);

        // Populate the right BIT with all ratings initially
        for (int r : rating) {
            updateBIT(rightBIT, r, 1);
        }

        int teams = 0;
        for (int currentRating : rating) {
            // Remove current rating from right BIT
            updateBIT(rightBIT, currentRating, -1);

            // Count soldiers with smaller and larger ratings on both sides
            int smallerRatingsLeft = getPrefixSum(leftBIT, currentRating - 1);
            int smallerRatingsRight = getPrefixSum(rightBIT, currentRating - 1);
            int largerRatingsLeft = getPrefixSum(leftBIT, maxRating) -
                                    getPrefixSum(leftBIT, currentRating);
            int largerRatingsRight = getPrefixSum(rightBIT, maxRating) -
                                     getPrefixSum(rightBIT, currentRating);

            // Count increasing and decreasing sequences
            teams += (smallerRatingsLeft * largerRatingsRight);
            teams += (largerRatingsLeft * smallerRatingsRight);

            // Add current rating to left BIT
            updateBIT(leftBIT, currentRating, 1);
        }

        return teams;
    }
};
```
