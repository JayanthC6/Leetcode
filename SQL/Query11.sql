/*
Enter your query here.
Query the list of CITY names from STATION that do not end with vowels. 
Your result cannot contain duplicates.
*/

SELECT Distinct CITY FROM STATION where RIGHT(CITY,1) NOT IN ('a', 'e', 'i', 'o', 'u');