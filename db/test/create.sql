drop table if exists t2;
drop table if exists t1;

create table t1 (
  t1_id integer primary key autoincrement,
  test1 varchar(255) not null check (test1 <> '')
);

create table t2 (
  t2_id integer primary key autoincrement,
  t1_id integer references t1 (t1_id),
  test2 varchar(255)
);

