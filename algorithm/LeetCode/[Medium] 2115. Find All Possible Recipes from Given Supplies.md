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
