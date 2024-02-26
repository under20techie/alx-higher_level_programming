-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name FROM cities
WHERE cities.id = (
	SELECT id FROM states
	WHERE name = Carlifornia
)
ORDER BY cities.id;
