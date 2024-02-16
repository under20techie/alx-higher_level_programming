-- calculate max temperature for each state 
SELECT state, MAX(values) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
