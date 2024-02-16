-- Calculate avg temperature
SELECT city, AVG(*) as avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
