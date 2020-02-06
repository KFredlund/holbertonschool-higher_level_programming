-- A script that prints the full description of the 
-- table first_table from db hbtn_0c_0 in your server
SELECT *
from information_schema.columns
WHERE table_name = 'first_table'
