-- .read schema.sql

create table Users(
	id integer primary key,
	name varchar(64) not null,
	email varchar(64) not null,
	password varchar(64) not null
);