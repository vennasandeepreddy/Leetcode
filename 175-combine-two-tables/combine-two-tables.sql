# Write your MySQL query statement below
select P.firstName, P.lastName, A.city, A.state
FROM Person as P
left join Address as A
ON P.personId = A.personId