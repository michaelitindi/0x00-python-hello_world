-- lists cities contained in database
-- using only one select statement
SELECT cities.id, cities.name, states.name AS state_name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
