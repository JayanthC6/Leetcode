/*
Enter your query here.
Query the list of CITY names starting with vowels 
(i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Note: The LEFT(CITY,1) is used to get the first character of the city names from left side and 1 is used to
grab exactly 1 character i.e; If the city is "London", LEFT('London', 1) returns 'L'. 
If the city is "Austin", it returns 'A'
*/

SELECT Distinct CITY from STATION where LEFT(CITY,1) IN ('a','e','i','o','u');