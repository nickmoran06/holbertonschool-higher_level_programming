-- script that lists the number of records with the same score in a table
SELECT `score`, COUNT(`score`) AS number
FROM `second_table`
GROUP BY `score` DESC;
