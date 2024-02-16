-- select like numbers
SELECT score, SUM(score) AS numbers FROM second_table
GROUP BY score
ORDER BY score DESC;
