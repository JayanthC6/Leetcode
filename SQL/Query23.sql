/*
Enter your query here.
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) 
in STATION that is less than . Round your answer to  decimal places.
*/
SELECT ROUND(LONG_W,4) from STATION where LAT_N<137.2345 order BY LAT_N desc limit 1;