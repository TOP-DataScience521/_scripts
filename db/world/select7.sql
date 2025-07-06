   select cn.name,
          c.name
     from country as cn
left join city as c
       on cn.code = c.countrycode
    where c.name is null

-- +----------------------------------------------+------+
-- | name                                         | name |
-- +----------------------------------------------+------+
-- | Antarctica                                   | NULL |
-- | French Southern territories                  | NULL |
-- | Bouvet Island                                | NULL |
-- | Heard Island and McDonald Islands            | NULL |
-- | British Indian Ocean Territory               | NULL |
-- | South Georgia and the South Sandwich Islands | NULL |
-- | United States Minor Outlying Islands         | NULL |
-- +----------------------------------------------+------+
-- 7 rows in set (0.0035 sec)



