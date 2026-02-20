/* Write your MySQL query statement below
Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

The employee has a bonus less than 1000.
The employee did not get any bonus.
Return the result table in any order.*/
select e.name,b.bonus from Employee e left join Bonus b on e.empId=b.empID 
where b.bonus<1000 or b.bonus is null;