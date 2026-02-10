/*
Enter your query here.
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
Your result cannot contain duplicates.
*/

SELECT Distinct CITY FROM STATION where RIGHT(CITY,1) IN ('a','e','i','o','u');