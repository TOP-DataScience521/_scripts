select store_id,
       country,
       city,
       address
  from store
  join address
 using (address_id)
  join city
 using (city_id)
  join country
 using (country_id)
 where address_id in (1, 2);
-- +----------+-----------+------------+--------------------+
-- | store_id | country   | city       | address            |
-- +----------+-----------+------------+--------------------+
-- |        1 | Canada    | Lethbridge | 47 MySakila Drive  |
-- |        2 | Australia | Woodridge  | 28 MySQL Boulevard |
-- +----------+-----------+------------+--------------------+
-- 2 rows in set (0.0022 sec)


  select title,
         count(*) as `rents count`
    from rental
    join inventory
   using (inventory_id)
    join film
   using (film_id)
group by title
order by `rents count` desc;
-- +-----------------------------+-------------+
-- | title                       | rents count |
-- +-----------------------------+-------------+
-- | BUCKET BROTHERHOOD          |          34 |
-- | ROCKETEER MOTHER            |          33 |
-- | FORWARD TEMPLE              |          32 |
-- | GRIT CLOCKWORK              |          32 |
-- | JUGGLER HARDLY              |          32 |
-- .............................................
-- | SEVEN SWARM                 |           5 |
-- | TRAFFIC HOBBIT              |           5 |
-- | HARDLY ROBBERS              |           4 |
-- | MIXED DOORS                 |           4 |
-- | TRAIN BUNCH                 |           4 |
-- +-----------------------------+-------------+
-- 958 rows in set (0.0325 sec)

