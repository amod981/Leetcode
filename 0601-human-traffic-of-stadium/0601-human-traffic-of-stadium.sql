# Write your MySQL query statement below
select id , visit_date, people
from
(select id, visit_date, people,
lead(people,1) over(order by visit_date) as 1st,
lead(people,2) over(order by visit_date) as 2nd,
lag(people,1) over(order by visit_date) as 1st_back,
lag(people,2) over(order by visit_date) as 2nd_back
from stadium
 ) as t
where 
(1st >= 100 and people >= 100 and 1st_back >= 100)
or (1st >= 100 and people >= 100 and 2nd >= 100)
or (1st_back >= 100 and people >= 100 and 2nd_back >= 100)
