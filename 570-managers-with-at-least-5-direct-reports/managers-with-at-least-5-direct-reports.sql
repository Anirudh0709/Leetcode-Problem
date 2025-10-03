# Write your MySQL query statement below

SELECT a.name FROM Employee A
join Employee B
On A.id = B.managerId
group by B.managerId
HAVING count(*)>=5
