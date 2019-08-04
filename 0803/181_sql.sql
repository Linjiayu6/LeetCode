# 1. 使用 WHERE 语句
# Write your MySQL query statement below
select A.Name as Employee
from 
Employee as A,
Employee as B

where A.ManagerId = B.Id
and A.Salary > B.Salary


# 2. 使用 JOIN 语句
select A.Name as Employee
from Employee as A 
join Employee as B

on A.ManagerId = B.id
and A.Salary > B.Salary