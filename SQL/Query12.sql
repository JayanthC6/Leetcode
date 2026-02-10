/*
Enter your query here.
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. 
Your result cannot contain duplicates.
*/

SELECT Distinct CITY FROM STATION where LEFT(CITY,1) not in ('a','e','i','o','u') 
or RIGHT(CITY,1) not in ('a','e','i','o','u');