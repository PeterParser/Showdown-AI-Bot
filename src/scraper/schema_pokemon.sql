CREATE DATABASE showdown_db;

USE showdown_db;


CREATE TABLE Pokemon (
num INT(6) UNSIGNED NOT NULL,
name VARCHAR(30) PRIMARY KEY,
hp INT(4) NOT NULL,
atk INT(4) NOT NULL,
def INT(4) NOT NULL,
spa INT(4) NOT NULL,
spd INT(4) NOT NULL,
spe INT(4) NOT NULL,
type_1 VARCHAR(15) NOT NULL,
type_2 VARCHAR(15),
ability_1 VARCHAR(30) NOT NULL,
ability_2 VARCHAR(30),
ability_hidden VARCHAR(30),
weight FLOAT NOT NULL
);
