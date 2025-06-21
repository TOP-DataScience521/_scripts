\c postgres
drop database if exists hospital;
create database hospital;
\c hospital


create table departments (
    id smallserial primary key,
    name text not null unique,
    check (name <> '')
);

create table wards (
    id smallserial primary key,
    name text not null unique,
    dep_id smallint not null,
    check (name <> '')
);

create table specializations (
    id smallserial primary key,
    name text not null unique,
    check (name <> '')
);

create table doctors (
    id smallserial primary key,
    dep_id smallint not null,
    last_name text not null,
    first_name text not null,
    patr_name text not null,
    -- от -999,999.99 до 999,999.99
    salary numeric(8,2) not null,
    premium numeric(8,2) not null default 0,
    check (last_name <> ''),
    check (first_name <> ''),
    check (patr_name <> ''),
    check (salary > 0),
    check (premium >= 0)
);

create table doctors_specs (
    doctor_id smallint not null,
    spec_id smallint not null,
    primary key (doctor_id, spec_id)
);

-- +-----------+---------+
-- | doctor_id | spec_id |
-- +-----------+---------+
-- |     1     |    1    |
-- |     1     |    2    |
-- |     2     |    1    |
-- |     3     |    3    |
-- .......................
-- +-----------+---------+

create table vacations (
    id serial primary key,
    doctor_id smallint not null,
    start_date date not null,
    end_date date not null,
    check (start_date < end_date)
);

create table sponsors (
    id smallserial primary key,
    name text not null unique,
    check (name <> '')
);

create table donations (
    id serial primary key,
    sponsor_id smallint not null,
    dep_id smallint not null,
    date date not null default current_date,
    -- от -999,999,999.99 до 999,999,999.99
    amount numeric(11,2) not null,
    check (amount > 0),
    check (date <= current_date)
);


alter table wards
    add foreign key (dep_id) references departments (id);

alter table doctors
    add foreign key (dep_id) references departments (id);

alter table doctors_specs
    add foreign key (doctor_id) references doctors (id),
    add foreign key (spec_id) references specializations (id);

alter table vacations
    add foreign key (doctor_id) references doctors (id);

alter table donations
    add foreign key (dep_id) references departments (id),
    add foreign key (sponsor_id) references sponsors (id);

