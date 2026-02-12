/*
Enter your query here.
Query the sum of LAT_N and LONG_W from the STATION table, and round each of these values 
to 2 decimal places.
*/
SELECT Round(sum(LAT_N),2),Round(sum(LONG_W),2) from STATION;