-- select like numbers
SELECT score, COUNT(score) AS numbers
WHERE LIKE '%'
ORDER BY score DESC;
