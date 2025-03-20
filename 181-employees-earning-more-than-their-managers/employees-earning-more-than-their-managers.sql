# Write your MySQL query statement below
select E1.name as Employee
FROM Employee E1
join Employee E2
on E1.managerId = E2.id 
where E1.salary > E2.salary

/*

 1  | Joe   | 70000  | 3         |  Sam   | 60000  | Null  

*/