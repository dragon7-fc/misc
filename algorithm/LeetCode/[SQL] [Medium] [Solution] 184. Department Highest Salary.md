184. Department Highest Salary

SQL Schema
The `Employee` table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

```
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```
The `Department` table holds all departments of the company.
```
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).
```
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```
**Explanation:**

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

---
# Solution
---
## Approach: Using `JOIN` and `IN` clause [Accepted]
**Algorithm**

Since the Employee table contains the Salary and DepartmentId information, we can query the highest salary in a department.
```sql
SELECT
    DepartmentId, MAX(Salary)
FROM
    Employee
GROUP BY DepartmentId;
```
>Note: There might be multiple employees having the same highest salary, so it is safe not to include the employee name information in this query.
```
| DepartmentId | MAX(Salary) |
|--------------|-------------|
| 1            | 90000       |
| 2            | 80000       |
```
Then, we can join table Employee and Department, and query the (DepartmentId, Salary) are in the temp table using IN statement as below.

**MySQL**
```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;
```
```
| Department | Employee | Salary |
|------------|----------|--------|
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
```

# Submissions
---
**Solution 1: (Using `JOIN` and `IN` clause)**

```
Runtime: 616 ms
Memory Usage: 0B
```
```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;
```