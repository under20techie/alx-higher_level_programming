-- calculate max temperature for each state 
SELECT state, MAX(*) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
