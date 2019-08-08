# Write your MySQL query statement below


# 使用 not in
select Customers.name as Customers
from Customers
where Customers.Id not in (
  select CustomerId
  from Orders
)

# 使用 left join on 连接两个表来, 通过null来判断
select A.name as Customers
from Customers A left join Orders B
on A.Id = B.CustomerId
where B.Id is null