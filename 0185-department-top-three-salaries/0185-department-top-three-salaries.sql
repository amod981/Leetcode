# Write your MySQL query statement below


select 
dep as Department,
name as Employee,
salary as Salary
from
(select 

department.name as dep, employee.name, salary,
dense_rank() over(partition by department.id order by salary desc) as r

from
employee
left join
department
on employee.departmentid = department.id
) as t 
where r <= 3