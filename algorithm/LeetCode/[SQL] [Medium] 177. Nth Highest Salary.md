177. Nth Highest Salary

Write a SQL query to get the nth highest salary from the Employee table.
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
For example, given the above Employee table, the nth highest salary where n = 2 is `200`. If there is no nth highest salary, then the query should return null.
```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

# Submissions
---
**Solution 1: (SQL)**

**MySQL**

```
Runtime: 354 ms
Memory Usage: 0B
```
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET  N = N-1;
  RETURN (
      SELECT Distinct Salary
      from Employee
          UNION ALL (SELECT null AS Salary)
        order by Salary desc 
        limit 1 offset N
  );
END
```