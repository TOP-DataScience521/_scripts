drop schema if exists library;
create schema library;
use library;

create table authors (
  id smallint unsigned auto_increment primary key,
  last_name varchar(30) not null,
  first_name varchar(30) not null
);

create table books (
  id smallint unsigned auto_increment primary key,
  author_id smallint unsigned not null,
  title varchar(50) not null,
  foreign key (author_id) references authors (id)
);

create table publishers (
  id tinyint unsigned auto_increment primary key,
  name varchar(40) not null unique
);

create table books_publishers (
  isbn char(13) primary key,
  book_id smallint unsigned not null 
    references books (id),
  publisher_id tinyint unsigned not null 
    references publishers (id)
);
