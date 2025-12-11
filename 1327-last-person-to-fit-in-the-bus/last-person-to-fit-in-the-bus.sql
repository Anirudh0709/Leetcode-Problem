# Write your MySQL query statement below
Select person_name
from (
    Select person_name,
    Sum(weight)Over(order by turn) As total_w
    From Queue
) q
Where total_w <=1000
Order by total_w DESC
Limit 1

