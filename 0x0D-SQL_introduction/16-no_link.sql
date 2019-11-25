-- script that lists all records of the table second_table
-- Don’t list rows without a name value
SELECT `score`, `name`
FROM `second_line`
WHERE `name` IS NOT NULL OR `name` != ''
GROUP BY score DESC;
