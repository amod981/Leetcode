# Write your MySQL query statement below


select request_at as Day, round(total_cancelled/ total_requested,2) as "Cancellation Rate"
from
(
select 
request_at
, sum(case when status like '%cancelled%' then 1 else 0 end) as total_cancelled,
sum(1) as total_requested
from 
(select * from trips where request_at between '2013-10-01' and '2013-10-03') as trips 
left join 
(select * from users) as b
on (trips.client_id = b.users_id) 
left join 
(select * from users) as c
on (trips.driver_id = c.users_id)
where b.banned = 'No' and c.banned = 'No'

group by request_at
) as t




