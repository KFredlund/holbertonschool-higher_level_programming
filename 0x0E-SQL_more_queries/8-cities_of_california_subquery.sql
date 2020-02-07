-- A script that lists all the cities in Califorinia
-- that can be found in the db
SELECT cities.id, cities.name
FROM states, cities WHERE states.name = 'California'
AND states.id = cities.state_id
ORDER BY cities.id;
