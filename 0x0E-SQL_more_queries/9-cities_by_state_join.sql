-- A script that lists all the cities in Califorinia
-- that can be found in the db
SELECT cities.id, cities.name, states.name
FROM states, cities WHERE states.id IS NOT NULL
AND states.id = cities.state_id
ORDER BY cities.id;
