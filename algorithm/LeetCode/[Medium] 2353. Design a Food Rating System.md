2353. Design a Food Rating System

Design a food rating system that can do the following:

* **Modify** the rating of a food item listed in the system.
* Return the highest-rated food item for a type of cuisine in the system.
Implement the `FoodRatings` class:

* `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.
    * `foods[i]` is the name of the `i`th food,
    * `cuisines[i]` is the type of cuisine of the `i`th food, and
    * `ratings[i]` is the initial rating of the `i`th food.
* `void changeRating(String food, int newRating)` Changes the rating of the food item with the name food.
* `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

 

**Example 1:**
```
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".
```

**Constraints:**

* `1 <= n <= 2 * 10^4`
* `n == foods.length == cuisines.length == ratings.length`
* `1 <= foods[i].length, cuisines[i].length <= 10`
* `foods[i]`, `cuisines[i]` consist of lowercase English letters.
* `1 <= ratings[i] <= 10^8`
* All the strings in foods are **distinct**.
* `food` will be the name of a food item in the system across all calls to `changeRating`.
* `cuisine` will be a type of cuisine of at least one food item in the system across all calls to `highestRated`.
* At most 2 * 10^4 calls in total will be made to `changeRating` and `highestRated`.

# Submissions
---
**Solution 1: (Hash Table, Heap)**
```
Runtime: 832 ms
Memory Usage: 44.3 MB
```
```python
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine = defaultdict(str)
        self.food_rating = defaultdict(int)
        for i, f in enumerate(foods):
            self.food_cuisine[f] = cuisines[i]
            self.food_rating[f] = ratings[i]
        self.cuisines_heap = defaultdict(list)
        for i, c in enumerate(cuisines):
            heappush(self.cuisines_heap[c], (-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        heappush(self.cuisines_heap[self.food_cuisine[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisines_heap[cuisine] and self.food_rating[self.cuisines_heap[cuisine][0][1]] != -self.cuisines_heap[cuisine][0][0]:
            heappop(self.cuisines_heap[cuisine])
        return self.cuisines_heap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```

**Solution 2: (3 Maps)**
```
Runtime: 824 ms
Memory Usage: 165.8 MB
```
```c++
class FoodRatings {
    unordered_map<string, set<pair<int, string>>> cuisine_ratings;
    unordered_map<string, string> food_cuisine;
    unordered_map<string, int> food_rating;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); ++i) {
            cuisine_ratings[cuisines[i]].insert({ -ratings[i], foods[i] });
            food_cuisine[foods[i]] = cuisines[i];
            food_rating[foods[i]] = ratings[i];
        }
    }
    
    void changeRating(string food, int newRating) {
        auto &cuisine = food_cuisine.find(food)->second;
        cuisine_ratings[cuisine].erase({ -food_rating[food], food });
        cuisine_ratings[cuisine].insert({ -newRating, food });
        food_rating[food] = newRating;
    }
    
    string highestRated(string cuisine) {
        return begin(cuisine_ratings[cuisine])->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
```
