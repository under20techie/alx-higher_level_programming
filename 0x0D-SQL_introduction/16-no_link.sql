-- Lists records only if they have name column
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
