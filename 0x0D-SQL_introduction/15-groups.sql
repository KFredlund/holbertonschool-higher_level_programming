-- A script that lists the number of records with
-- the same score in the table
SELECT * FROM second_table WHERE score IN
(
	SELECT score
	FROM second_table
	GROUP BY score
	HAVING COUNT(*) > 1
)
ORDER BY score DESC;
