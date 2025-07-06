   select title as `film title`,
          count(inventory_id) as `total disks`
     from film
left join inventory
    using (film_id)
 group by `film title`
 order by `total disks`;

-- +-----------------------------+-------------+
-- | film title                  | total disks |
-- +-----------------------------+-------------+
-- | ALICE FANTASIA              |           0 |
-- | APOLLO TEEN                 |           0 |
-- | ARGONAUTS TOWN              |           0 |
-- | ARK RIDGEMONT               |           0 |
-- | ARSENIC INDEPENDENCE        |           0 |
-- .............................................
-- | TORQUE BOUND                |           8 |
-- | TRIP NEWTON                 |           8 |
-- | VIRGINIAN PLUTO             |           8 |
-- | WIFE TURN                   |           8 |
-- | ZORRO ARK                   |           8 |
-- +-----------------------------+-------------+
-- 1000 rows in set (0.0285 sec)


select 
  concat(first_name, " ", last_name) as `name`, 
  count(rental_id) as `total rents` 
from 
  customer 
left join 
  rental 
  using (customer_id) 
group by `name` 
order by `name`;

-- +-----------------------+-------------+
-- | name                  | total rents |
-- +-----------------------+-------------+
-- | AARON SELBY           |          24 |
-- | ADAM GOOCH            |          22 |
-- | ADRIAN CLARY          |          19 |
-- | AGNES BISHOP          |          23 |
-- | ALAN KAHN             |          26 |
-- .......................................
-- | WILLIE MARKHAM        |          25 |
-- | WILMA RICHARDS        |          20 |
-- | YOLANDA WEAVER        |          27 |
-- | YVONNE WATKINS        |          21 |
-- | ZACHARY HITE          |          31 |
-- +-----------------------+-------------+
-- 599 rows in set (0.0221 sec)


select 
  concat(first_name, " ", last_name) as `name`, 
  count(rental_id) as `total rents` 
from 
  customer 
left join 
  rental 
  using (customer_id) 
group by 
  `name` 
having 
  `total rents` = 0 
order by 
  `name`;

-- Empty set (0.0303 sec)

