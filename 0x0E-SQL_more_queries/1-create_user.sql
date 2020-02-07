-- A script that creates the My SQL server
-- user user_0d_1
DROP USER 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

