-- select like numbers
SELECT score, COUNT(score) AS numbers
GROUP BY score
ORDER BY score DESC;
