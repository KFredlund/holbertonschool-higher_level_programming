-- A script that computes the score average of all records in
-- the table second_table of db
SELECT AVG(score) FROM second_table AS average;
ALTER TABLE second_table ADD average INT(10);
SELECT DISTINCT average FROM second_table;
