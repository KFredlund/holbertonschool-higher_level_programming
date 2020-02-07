-- A script that creates the db hbtn_0d_2
-- and the user user_0d_2
IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'hbtn_0d_2')
CREATE DATABASE hbtn_0d_2;
DROP USER 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
CREATE USER IF 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';
GRANT SELECT ON * . * TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
