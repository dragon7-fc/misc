2115. Find All Possible Recipes from Given Supplies

You have information about n different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The `i`th recipe has the name `recipes[i]`, and you can create it if you have all the needed ingredients from `ingredients[i]`. Ingredients to a recipe may need to be created from other recipes, i.e., `ingredients[i]` may contain a string that is in recipes.

You are also given a string array `supplies` containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in **any order**.

Note that two recipes may contain each other in their ingredients.

 

**Example 1:**
```
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
```

**Example 2:**
```
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
```

**Example 3:**
```
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
```

**Constraints:**

* `n == recipes.length == ingredients.length`
* `1 <= n <= 100`
* `1 <= ingredients[i].length, supplies.length <= 100`
* `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
* `recipes[i]`, `ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
* All the values of `recipes` and `supplies` combined are unique.
* Each `ingredients[i]` does not contain any duplicate values.

# Submissions
---
**Solution 1: (Topological Sort)**
```
Runtime: 932 ms
Memory: 17.4 MB
```
```python
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Construct directed graph and count the in-degrees
        ingredient_to_recipe, in_degree = defaultdict(set), Counter()
        for rcp, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ingredient_to_recipe[ing].add(rcp)
            in_degree[rcp] = len(ingredient)
        # Topological sort.    
        available, ans = deque(supplies), []
        while available:
            ing = available.popleft()
            for rcp in ingredient_to_recipe.pop(ing, set()):
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    available.append(rcp)
                    ans.append(rcp)
        return ans
```

**Solution 2: (DFS)**
```
Runtime: 2098 ms
Memory: 22.6 MB
```
```python
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = {}
        visited = set()
        res = []

        for recipe, ingredient in zip(recipes, ingredients):
            graph[recipe] = ingredient

        def dfs(node: str) -> bool:
            if node in visited:
                return False

            visited.add(node)

            if node not in graph:
                return False

            for dependency in graph[node]:
                # if ingredient of recipe exist in supplies, it's good to go
                # if ingredient of recipe doesn't exist in supplies, then use dfs to check if
                # it hasn't been used(visited) and exist on graph means it comes from another recipies then good to go
                # if ingredient of recipe doesn't exist and ( already used (visited) or doesn't come from another recipes then 
                # we need to return false since we don't have enough ingredient to follow current recipe
                if dependency not in supplies and not dfs(dependency):
                    return False

            res.append(node)
            supplies.add(node)
            return True

        for recipe in recipes:
            dfs(recipe)

        return res
```

**Solution 3: (DFS)**
```
Runtime: 2686 ms
Memory: 23.7 MB
```
```python
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        def dfs(r):
            if r not in can_make:
                can_make[r] = False
                if r in graph:
                    can_make[r] = all([dfs(i) for i in graph[r]])
            return can_make[r]
        
        can_make = {s: True for s in supplies}
        graph = {r: ings for r, ings in zip(recipes, ingredients)}
        return [r for r in recipes if dfs(r)]
```

**Solution 4: (DFS)**
```
Runtime: 27 ms, Beats 97.53%
Memory: 102.27 MB, Beats 86.05%
```
```c++
class Solution {
    void checkRecipe(const string& recipe, vector<vector<string>>& ingredients,
                     unordered_set<string>& visited,
                     unordered_map<string, bool>& canMake,
                     unordered_map<string, int>& recipeToIndex) {
        // Return if we already know if recipe can be made
        if (canMake.find(recipe) != canMake.end()) {
            return;
        }

        // Not a valid recipe or cycle detected
        auto idxIt = recipeToIndex.find(recipe);
        if (idxIt == recipeToIndex.end() || visited.count(recipe)) {
            canMake[recipe] = false;
            return;
        }

        visited.insert(recipe);

        // Check if we can make all required ingredients
        for (const string& ingredient : ingredients[idxIt->second]) {
            checkRecipe(ingredient, ingredients, visited, canMake,
                        recipeToIndex);
            if (!canMake[ingredient]) {
                canMake[recipe] = false;
                return;
            }
        }

        // All ingredients can be made
        canMake[recipe] = true;
    }
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        vector<string> possibleRecipes;
        // Track if ingredient/recipe can be made
        unordered_map<string, bool> canMake;
        // Map recipe name to its index in ingredients list
        unordered_map<string, int> recipeToIndex;

        // Mark all initial supplies as available
        for (const string& supply : supplies) {
            canMake[supply] = true;
        }

        // Create recipe to index mapping
        for (int idx = 0; idx < recipes.size(); idx++) {
            recipeToIndex[recipes[idx]] = idx;
        }

        // Try to make each recipe using DFS
        for (const string& recipe : recipes) {
            unordered_set<string> visited;
            checkRecipe(recipe, ingredients, visited, canMake, recipeToIndex);
            if (canMake[recipe]) {
                possibleRecipes.push_back(recipe);
            }
        }

        return possibleRecipes;
    }
};
```

**Solution 5: (Topological Sort (Kahn's Algorithm))**
```
Runtime: 31 ms, Beats 95.55%
Memory: 107.36 MB, Beats 79.62%
```
```c++
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        // Store available supplies
        unordered_set<string> availableSupplies;
        // Map recipe to its index
        unordered_map<string, int> recipeToIndex;
        // Map ingredient to recipes that need it
        unordered_map<string, vector<string>> dependencyGraph;

        // Initialize available supplies
        for (string& supply : supplies) {
            availableSupplies.insert(supply);
        }

        // Create recipe to index mapping
        for (int idx = 0; idx < recipes.size(); idx++) {
            recipeToIndex[recipes[idx]] = idx;
        }

        // Count of non-supply ingredients needed for each recipe
        vector<int> inDegree(recipes.size(), 0);

        // Build dependency graph
        for (int recipeIdx = 0; recipeIdx < recipes.size(); recipeIdx++) {
            for (string& ingredient : ingredients[recipeIdx]) {
                if (!availableSupplies.count(ingredient)) {
                    // Add edge: ingredient -> recipe
                    dependencyGraph[ingredient].push_back(recipes[recipeIdx]);
                    inDegree[recipeIdx]++;
                }
            }
        }

        // Start with recipes that only need supplies
        queue<int> queue;
        for (int recipeIdx = 0; recipeIdx < recipes.size(); recipeIdx++) {
            if (inDegree[recipeIdx] == 0) {
                queue.push(recipeIdx);
            }
        }

        // Process recipes in topological order
        vector<string> createdRecipes;
        while (!queue.empty()) {
            int recipeIdx = queue.front();
            queue.pop();
            string recipe = recipes[recipeIdx];
            createdRecipes.push_back(recipe);

            // Skip if no recipes depend on this one
            if (!dependencyGraph.count(recipe)) continue;

            // Update recipes that depend on current recipe
            for (string& dependentRecipe : dependencyGraph[recipe]) {
                if (--inDegree[recipeToIndex[dependentRecipe]] == 0) {
                    queue.push(recipeToIndex[dependentRecipe]);
                }
            }
        }

        return createdRecipes;
    }
};
```

**Solution 6: (DP Bottom-Up)**

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]

   (bu)
      \
       (s)
       / \
    (br)  m
     / \
    y   f

```
Runtime: 548 ms, Beats 13.06%
Memory: 159.77 MB, Beats 51.83%
```
```c++
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size(), i;
        unordered_map<string, unordered_set<string>> m;
        for (i = 0; i < n; i ++) {
            m[recipes[i]].insert(ingredients[i].begin(), ingredients[i].end());
        }
        unordered_set<string> cur, rem(recipes.begin(), recipes.end()), st(supplies.begin(), supplies.end());
        vector<string> dp;
        do {
            while (dp.size()) {
                rem.erase(dp.back());
                dp.pop_back();
            }
            for (auto r: rem) {
                if (all_of(m[r].begin(), m[r].end(), [&](string ci){
                    return cur.count(ci) || st.count(ci);
                })) {
                    cur.insert(r);
                    dp.push_back(r);
                }
            }
        } while (dp.size());
        return vector<string>(cur.begin(), cur.end());
    }
};
```

**Solution 7: (DFS, DP Top-Down)**
```
Runtime: 24 ms, Beats 98.62%
Memory: 102.24 MB, Beats 86.05%
```
```c++
class Solution {
    bool dfs(int i, unordered_map<string, int> &m, vector<vector<string>> &ingredients, vector<int> &dp) {
        dp[i] = 0;
        for (auto ci: ingredients[i]) {
            if (!m.count(ci)) {
                return false;
            }
            if (m[ci] == -1) {
                continue;
            }
            if (dp[m[ci]] == 0 || dp[m[ci]] == -1 && !dfs(m[ci], m, ingredients, dp)) {
                return false;
            }
        }
        dp[i] = 1;
        return true;
    }
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size(), i;
        unordered_map<string, int> m;
        vector<int> dp(n);
        for (i = 0; i < n; i ++) {
            m[recipes[i]] = i;
            dp[i] = -1;
        }
        
        for (auto supply: supplies) {
            m[supply] = -1;
        }
        vector<string> ans;
        for (i = 0; i < n; i ++) {
            if (dp[i] == -1) {
                dfs(i, m, ingredients, dp);
            }
            if (dp[i]) {
                ans.push_back(recipes[i]);
            }
        }
        return ans;
    }
};
```

**Solution 8: (Topological Sort)**
```
Runtime: 35 ms, Beats 93.87%
Memory: 102.41 MB, Beats 84.57%
```
```c++
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        int n = recipes.size(), i;
        unordered_map<string, int> m;
        unordered_map<string, vector<int>> g;
        vector<int> indeg(n);
        unordered_set<string> st;
        queue<int> q;
        vector<string> ans;
        for (i = 0; i < n; i ++) {
            m[recipes[i]] = i;
        }
        for (auto supply: supplies) {
            st.insert(supply);
        }
        for (i = 0; i < n; i ++) {
            for (auto ingredient: ingredients[i]) {
                if (!st.count(ingredient)) {
                    g[ingredient].push_back(i);
                    indeg[i] += 1;
                }
            }
        }
        for (i = 0; i < n; i ++) {
            if (indeg[i] == 0) {
                q.push(i);
            }
        }
        while (q.size()) {
            auto r = q.front();
            q.pop();
            ans.push_back(recipes[r]);
            for (auto nr: g[recipes[r]]) {
                indeg[nr] -= 1;
                if (indeg[nr] == 0) {
                    q.push(nr);
                }
            }
        }
        return ans;
    }
};
```
