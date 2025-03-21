# Write your MySQL query statement below

with dup_CTO AS (select MIN(id)
From Person 
group by Email)
DELETE FROM PERSON
where id not in (select * from dup_CTO)