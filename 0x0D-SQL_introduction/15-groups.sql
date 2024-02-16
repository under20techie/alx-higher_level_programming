-- select like numbers
SELECT score, COUNT(score) AS numbers
WHERE score LIKE '%'
ORDER BY score DESC;
