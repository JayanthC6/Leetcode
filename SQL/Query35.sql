/*
Enter your query here.
Write a query to find the number of employees in each company, grouped by the company code and founder. 
The output should include the company code, founder, and the count of employees in each company. 
Order the results by company code in ascending order.
*/
SELECT 
    c.company_code, 
    c.founder, 
    COUNT(DISTINCT e.lead_manager_code), 
    COUNT(DISTINCT e.senior_manager_code), 
    COUNT(DISTINCT e.manager_code), 
    COUNT(DISTINCT e.employee_code)
FROM Company c
JOIN Employee e ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;