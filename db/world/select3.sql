select name from country where continent = "Europe" and population > 10000000;

-- +--------------------+
-- | name               |
-- +--------------------+
-- | Belgium            |
-- | Belarus            |
-- | Czech Republic     |
-- | Germany            |
-- | Spain              |
-- | France             |
-- | United Kingdom     |
-- | Greece             |
-- | Hungary            |
-- | Italy              |
-- | Netherlands        |
-- | Poland             |
-- | Romania            |
-- | Russian Federation |
-- | Ukraine            |
-- | Yugoslavia         |
-- +--------------------+
-- 16 rows in set (0.0007 sec)


select name 
  from country 
 where continent = "Europe" 
   and indepyear is null;

-- +------------------------+
-- | name                   |
-- +------------------------+
-- | Faroe Islands          |
-- | Gibraltar              |
-- | Svalbard and Jan Mayen |
-- +------------------------+
-- 3 rows in set (0.0007 sec)


select name from country;

-- +----------------------------------------------+
-- | name                                         |
-- +----------------------------------------------+
-- | Aruba                                        |
-- | Afghanistan                                  |
-- | Angola                                       |
-- ................................................
-- | South Africa                                 |
-- | Zambia                                       |
-- | Zimbabwe                                     |
-- +----------------------------------------------+
-- 239 rows in set (0.0007 sec)


select name from country limit 10;

-- +----------------------+
-- | name                 |
-- +----------------------+
-- | Aruba                |
-- | Afghanistan          |
-- | Angola               |
-- ........................
-- | United Arab Emirates |
-- | Argentina            |
-- | Armenia              |
-- +----------------------+
-- 10 rows in set (0.0005 sec)


select name from country order by name;

-- +----------------------------------------------+
-- | name                                         |
-- +----------------------------------------------+
-- | Afghanistan                                  |
-- | Albania                                      |
-- | Algeria                                      |
-- ................................................
-- | Yugoslavia                                   |
-- | Zambia                                       |
-- | Zimbabwe                                     |
-- +----------------------------------------------+
-- 239 rows in set (0.0009 sec)


select name from country order by name limit 10;

-- +---------------------+
-- | name                |
-- +---------------------+
-- | Afghanistan         |
-- | Albania             |
-- | Algeria             |
-- .......................
-- | Antarctica          |
-- | Antigua and Barbuda |
-- | Argentina           |
-- +---------------------+
-- 10 rows in set (0.0024 sec)


  select name, 
         population 
    from country 
order by population desc 
   limit 1;

-- другой способ форматирования
-- select 
--   name, 
--   population 
-- from 
--   country 
-- order by 
--   population desc 
-- limit 
--   1; 

-- +-------+------------+
-- | name  | population |
-- +-------+------------+
-- | China | 1277558000 |
-- +-------+------------+
-- 1 row in set (0.0009 sec)

