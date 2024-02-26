-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.nane, states.name
FROM cities
INNER JOIN ON cities.state_id = states.id
ORDER BY cities.id;
