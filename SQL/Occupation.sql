/*
Enter your query here.
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output should consist of four columns (Doctor, Professor, Singer, and Actor) in that specific order, with their respective names listed alphabetically under each column.

Note: Print NULL when there are no more names corresponding to an occupation.
*/
SET @row1 = 0, @row2 = 0, @row3 = 0, @row4 = 0;

SELECT
    MAX(Doctor),
    MAX(Professor),
    MAX(Singer),
    MAX(Actor)
FROM (
    SELECT
        IF(Occupation = 'Doctor', Name, NULL) AS Doctor,
        IF(Occupation = 'Professor', Name, NULL) AS Professor,
        IF(Occupation = 'Singer', Name, NULL) AS Singer,
        IF(Occupation = 'Actor', Name, NULL) AS Actor,

        CASE 
            WHEN Occupation = 'Doctor' THEN @row1 := @row1 + 1
            WHEN Occupation = 'Professor' THEN @row2 := @row2 + 1
            WHEN Occupation = 'Singer' THEN @row3 := @row3 + 1
            WHEN Occupation = 'Actor' THEN @row4 := @row4 + 1
        END AS rn

    FROM OCCUPATIONS
    ORDER BY Name
) x
GROUP BY rn;