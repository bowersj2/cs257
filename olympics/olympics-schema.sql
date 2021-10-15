CREATE TABLE id (
	id_key int PRIMARY KEY,
	id varchar(255) NOT NULL
);
CREATE TABLE name (
	name_key int PRIMARY KEY,
	name varchar(255) NOT NULL
);
CREATE TABLE sex (
	sex_key int PRIMARY KEY,
	sex varchar(255) NOT NULL
);
CREATE TABLE age (
	age_key int PRIMARY KEY,
	age varchar(255) NOT NULL
);
CREATE TABLE height (
	height_key int PRIMARY KEY,
	height_key varchar(255)
);
CREATE TABLE weight (
	weight_key int PRIMARY KEY,
	weight varchar(255) NOT NULL
);
CREATE TABLE team (
	tem_key int PRIMARY KEY,
	team varchar(255) NOT NULL
);
CREATE TABLE noc (
	noc_key int PRIMARY KEY,
	noc varchar(255) NOT NULL
);
CREATE TABLE games (
	games_key int PRIMARY KEY,
	games varchar(255) NOT NULL
);
CREATE TABLE year (
	year_key int PRIMARY KEY,
	year varchar(255) NOT NULL
);
CREATE TABLE season (
	season_key int PRIMARY KEY,
	season varchar(255) NOT NULL
);
CREATE TABLE city (
	city_key int PRIMARY KEY,
	city varchar(255) NOT NULL
);
CREATE TABLE sport (
	sport_key int PRIMARY KEY,
	sport varchar(255) NOT NULL
);
CREATE TABLE event (
	event_key int PRIMARY KEY,
	event varchar(255) NOT NULL
);
CREATE TABLE medal (
	medal_key int PRIMARY KEY,
	medal varchar(255) NOT NULL
);