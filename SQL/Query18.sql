/*
Enter your query here.
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, 
but did not realize her keyboard's  key was broken until after completing the calculation. 
She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), 
and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), 
and round it up to the next integer.

REPLACE(Salary, '0', ''): Takes each salary and removes the zeros. (2000 becomes 2, 1000 becomes 1).

SUM(...): Adds up these "broken" numbers.

Example: 2 + 1 = 3.
*/

SELECT ceil((sum(Salary) - sum(replace(Salary,'0',''))) / count(ID)) from Employees;