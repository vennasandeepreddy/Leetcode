# Write your MySQL query statement below
select firstName, lastName, city, state
FROM Person as P
left join Address as A
ON P.personId = A.personId