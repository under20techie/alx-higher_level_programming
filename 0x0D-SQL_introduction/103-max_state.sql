-- calculate max temperature for each state 
SELECT state, MAX(*) as max_temp FROM temperatures
GROUP BY state
ORDER BY state;
