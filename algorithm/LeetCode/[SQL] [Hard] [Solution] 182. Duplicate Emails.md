182. Duplicate Emails

SQL Schema
Write a SQL query to find all duplicate emails in a table named `Person`.
```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```
For example, your query should return the following for the above table:
```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```
**Note:** All emails are in lowercase.

# Solution
---
## Approach I: Using `GROUP BY` and a temporary table [Accepted]
**Algorithm**

Duplicated emails existed more than one time. To count the times each email exists, we can use the following code.
```sql
select Email, count(Email) as num
from Person
group by Email;
```
```
| Email   | num |
|---------|-----|
| a@b.com | 2   |
| c@d.com | 1   |
```
Taking this as a temporary table, we can get a solution as below.
```sql
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;
```
## Approach II: Using `GROUP BY` and `HAVING` condition [Accepted]
A more common used way to add a condition to a GROUP BY is to use the HAVING clause, which is much simpler and more efficient.

So we can rewrite the above solution to this one.

**MySQL**
```sql
select Email
from Person
group by Email
having count(Email) > 1;
```

# Submissions
---
**Solution 1: (Using `GROUP BY` and `HAVING` condition)**
```
Runtime: 334 ms
Memory Usage: 0B
```
```sql
# Write your MySQL query statement below
select Email
from Person
group by Email
having count(Email) > 1;
```